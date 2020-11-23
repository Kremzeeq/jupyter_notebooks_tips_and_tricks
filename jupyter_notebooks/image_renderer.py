from PIL import Image               # to load images
from IPython.display import display # to display images


def image_renderer(basewidth, image_path):
	pil_img = Image.open(image_path)
	wpercent = (basewidth/float(pil_img.size[0]))
	hsize = int((float(pil_img.size[1])*float(wpercent)))
	pil_img = pil_img.resize((basewidth,hsize), Image.ANTIALIAS)
	return display(pil_img)
