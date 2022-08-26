import os
import random
from PIL import Image
from tqdm import tqdm
from utils import putting, meta_json, logging_info, open_json
from utils import get_links, init_log, update_logs
from itertools import product

def generate_random(numbers=10000):

	log = init_log()
	total = list(product(l1,l2,l3,l4,l5))
	random.shuffle(total) 
	images = total[:numbers]
	del total # Free up memory

	count = 0
	print(len(images))
	for layers in tqdm(images):

		values = logging_info(count, _layers)
		update_logs(log, value)

		image = putting(_layers)
		image.save(f"./Outputs/{count}.png")
		count += 1

if __name__ == "__main__":

	links = get_links()
	keys = list(links.keys())
	l0 = links[keys[0]]
	l1 = links[keys[1]]
	l2 = links[keys[2]]
	l3 = links[keys[3]]
	l4 = links[keys[4]]
	l5 = links[keys[5]]
	l6 = links[keys[6]]
	l7 = links[keys[7]]
	l8 = links[keys[8]]
	l9 = links[keys[9]]

	generate_random(10000)