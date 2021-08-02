import random
from utils.load_data import get_img_list, load_config
from processor import Processor
import argparse


parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("-opt", type=str, default=None)
args = parser.parse_args()


config = load_config(args.opt)
img_list = get_img_list(config["in_path"])
random.shuffle(img_list)
processor = Processor(config)
process_list = processor.get_process_list(len(img_list))
processor.process(img_list, process_list)
