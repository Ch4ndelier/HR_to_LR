import random
from utils.load_data import get_img_list, load_config
from processor import Processor


config = load_config()
img_list = get_img_list(config["in_path"])
random.shuffle(img_list)
processor = Processor(config)
process_list = processor.get_process_list(len(img_list))
processor.process(img_list, process_list)
