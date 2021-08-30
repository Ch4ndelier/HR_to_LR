import cv2
from utils.apply import apply
import os
from utils.progress_bar import ProgressBar


class Processor(object):

    def __init__(self, config):
        self.config = config
        print("Build Processor...")

    def process(self, img_list, process_list):
        for key, val in self.config.items():
            print("{} : {}".format(key, val))
        pbar = ProgressBar(len(process_list))
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
        out_path = os.path.join(out_path, img_name.split('.')[0] + 'x1.png')
        cv2.imwrite(out_path, img)

    def get_process_list(self, num_img):
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
        # fix 0
        for i, v in enumerate(process_list):
            if v == 0:
                process_list[i] = p_name_list[-1]
        # print(process_list)
        # exit()
        return process_list
