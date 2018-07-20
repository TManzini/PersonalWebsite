from pdf2image import convert_from_path
from PIL import Image
import os 

PAPERS_DIR = "./data/papers/"
PAPERS_IMG_DIR =  "./data/paper_img/"

IM_SIZE = 256, 256

papers = os.listdir(PAPERS_DIR)

for paper in papers:
	images = convert_from_path(PAPERS_DIR + paper)
	for im in images:
		im.thumbnail(IM_SIZE, Image.ANTIALIAS) 
	widths, heights = zip(*(i.size for i in images))

	total_width = sum(widths)
	max_height = max(heights)

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	for im in images:
	  new_im.paste(im, (x_offset,0))
	  x_offset += im.size[0]

	new_im.save(PAPERS_IMG_DIR + paper +'.jpg')
