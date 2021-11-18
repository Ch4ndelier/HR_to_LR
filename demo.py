import random
from utils.load_data import get_img_list, load_config
from processor import Processor
import argparse


parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("-opt", type=str, default=None)
# TODO: add support for second order
# parser.add_argument("-sopt", type=str, default=None)
args = parser.parse_args()

# get config
config = load_config(args.opt)
# get image list
img_list = get_img_list(config["in_path"])
random.shuffle(img_list)
processor = Processor(config)
# get process list
process_list = processor.get_process_list(len(img_list))
# process image
processor.process(img_list, process_list)
