import cv2
from utils.apply import apply
import os
import random
from utils.progress_bar import ProgressBar
from multiprocessing import Pool


class Processor(object):

    def __init__(self, config):
        self.config = config
        print("Build Processor...")

    def process(self, img_list, process_list):
        for key, val in self.config.items():
            print("{} : {}".format(key, val))
        pbar = ProgressBar(len(process_list))

        # multi-thread process
        # TODO: optimize?
        if self.config["multi-thread"]:
            n_thread = 10

            def update(arg):
                pbar.update(arg)

            pool = Pool(n_thread)

            for img_info, p in zip(img_list, process_list):
                if not img_info[0].endswith('png'):
                    continue
                pool.apply_async(self.process_single_image, args=(img_info, p), callback=update)

            pool.close()
            pool.join()
            print('All subprocesses done')

        # single-thread
        elif self.config["is_random"]:
            for img_info, p in zip(img_list, process_list):
                if not img_info[0].endswith('png'):
                    continue
                self.process_single_image_random(img_info, p)
                pbar.update()

        elif self.config["is_random_dropout"]:
            for img_info, p in zip(img_list, process_list):
                if not img_info[0].endswith('png'):
                    continue
                self.process_single_image_random_dropout(img_info, p)
                pbar.update()

        else:
            for img_info, p in zip(img_list, process_list):
                if not img_info[0].endswith('png'):
                    continue
                self.process_single_image(img_info, p)
                pbar.update()

    def process_single_image(self, img_info, process_type):
        out_path = self.config['out_path']
        config_total = self.config
        if not os.path.exists(out_path):
            os.mkdir(out_path)
        img_path, img_name = img_info[0], img_info[1]
        cfg = self.config["process"][process_type]
        # print("img: ", img_path, "using pipline ", process_type, ":", cfg["pipline"])
        # print("img: {} using pipline {} : {}".format(img_path, process_type, cfg["pipline"]))
        img = cv2.imread(img_path)
        for method in cfg["pipline"]:
            # print("using method " + method)
            img = apply(img, cfg, config_total, method)
        # out_path = os.path.join(out_path, img_name)
        out_path = os.path.join(out_path, img_name.split('.')[0] + '.png')
        cv2.imwrite(out_path, img)

    def process_single_image_random_dropout(self, img_info, process_type):
        # random model for random degration
        out_path = self.config['out_path']
        config_total = self.config
        if not os.path.exists(out_path):
            os.mkdir(out_path)
        img_path, img_name = img_info[0], img_info[1]
        cfg = self.config["process"][process_type]
        # print("img: ", img_path, "using pipline ", process_type, ":", cfg["pipline"])
        # print("img: {} using pipline {} : {}".format(img_path, process_type, cfg["pipline"]))
        img = cv2.imread(img_path)
        random_pipline = [_ for _ in cfg["pipline"]]
        random.shuffle(random_pipline)
        dropout_downsample_pro = random.random()
        dropout_noise_pro = random.random()
        dropout_jpeg_pro = random.random()
        dropout_blur_pro = random.random()
        dropout_rot_pro = random.random()
        if dropout_downsample_pro > cfg["dropout_downsample_pro"]:
            key = random_pipline.index("downsample")
            random_pipline[key] = 'fixed_downsample'
            key = random_pipline.index("downsample")
            random_pipline[key] = 'fixed_upsample'

        random_dropout_pipline = []
        degradation_set = set()
        for degra in random_pipline:
            if degra not in degradation_set:
                degradation_set.add(degra)
                random_dropout_pipline.append(degra)
            else:
                if degra == 'noise':
                    if dropout_noise_pro > cfg["dropout_noise_pro"]:
                        random_dropout_pipline.append(degra)
                elif degra == 'blur':
                    if dropout_blur_pro > cfg["dropout_blur_pro"]:
                        random_dropout_pipline.append(degra)
                elif degra == 'jpeg':
                    if dropout_jpeg_pro > cfg["dropout_jpeg_pro"]:
                        random_dropout_pipline.append(degra)
                elif degra == 'rotate':
                    if dropout_rot_pro > cfg["dropout_rot_pro"]:
                        random_dropout_pipline.append(degra)
                
        random_dropout_pipline.append('jpeg')
        # print(random_pipline)
        # print(random_dropout_pipline)
        # exit()
        for method in random_dropout_pipline:
            # print("using method " + method)
            img = apply(img, cfg, config_total, method)
        # out_path = os.path.join(out_path, img_name)
        out_path = os.path.join(out_path, img_name.split('.')[0] + '.png')
        cv2.imwrite(out_path, img)
        
    def process_single_image_random(self, img_info, process_type):
        # random model for random degration
        out_path = self.config['out_path']
        config_total = self.config
        if not os.path.exists(out_path):
            os.mkdir(out_path)
        img_path, img_name = img_info[0], img_info[1]
        cfg = self.config["process"][process_type]
        # print("img: ", img_path, "using pipline ", process_type, ":", cfg["pipline"])
        # print("img: {} using pipline {} : {}".format(img_path, process_type, cfg["pipline"]))
        img = cv2.imread(img_path)
        random_pipline = [_ for _ in cfg["pipline"]]
        random.shuffle(random_pipline)
        key = random_pipline.index("downsample")
        random_pipline[key] = 'fixed_downsample'
        key = random_pipline.index("downsample")
        random_pipline[key] = 'fixed_upsample'
        random_pipline.append('jpeg')
        # print(random_pipline)
        for method in random_pipline:
            # print("using method " + method)
            img = apply(img, cfg, config_total, method)
        # out_path = os.path.join(out_path, img_name)
        out_path = os.path.join(out_path, img_name.split('.')[0] + '.png')
        cv2.imwrite(out_path, img)

    def get_process_list(self, num_img):
        # divide the image ratio
        # TODO: optimize?
        p_dict = self.config["process"]
        ratio_list = []
        p_name_list = []
        process_list = [0] * num_img

        for p_name, pipline_dict in p_dict.items():
            p_name_list.append(p_name)
            ratio_list.append(pipline_dict["data_num_ratio"])

        ratio_list = [ratio / sum(ratio_list) for ratio in ratio_list]
        ratio_interval = []
        temp = 0
        for ratio in ratio_list:
            temp += ratio
            ratio_interval.append(temp)
        # print(ratio_interval)
        # ratio_interval is the ratio prefix of the list
        # TODO:optimize?
        begin = 0
        for itv, p_name in zip(ratio_interval, p_name_list):
            # print(num_img)
            # print(itv, itv * num_img, int(itv * num_img))
            for i in range(begin, int(itv * num_img)):
                process_list[i] = p_name
            begin = int(itv * num_img)
        # fill up the missing process
        for i, v in enumerate(process_list):
            if v == 0:
                process_list[i] = p_name_list[-1]
        return process_list
