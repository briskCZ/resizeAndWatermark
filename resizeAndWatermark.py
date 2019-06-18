#!/usr/bin/env python

from gimpfu import *
import math, os

def do_stuff(img, drw, wtm_toggle, side_radio, w_offset, h_offset, path, rsz_toggle, exp_toggle, exp_path):
	pdb.gimp_undo_push_group_start(img)
		
	img_width = pdb.gimp_image_width(img)
	img_height = pdb.gimp_image_height(img)
	
	if wtm_toggle == 1:
		try:
			watermark = pdb.gimp_file_load_layer(img,path)

			pdb.gimp_image_insert_layer(img, watermark, None, 0)

			wtm_width = pdb.gimp_drawable_width(watermark)
			wtm_height = pdb.gimp_drawable_height(watermark)
			
			if(side_radio == 0):
				watermark = pdb.gimp_item_transform_2d(watermark, wtm_width, wtm_height, 1, 1, 0, img_width - w_offset, img_height - h_offset)
			if(side_radio == 1):
				watermark = pdb.gimp_item_transform_2d(watermark, wtm_width, wtm_height, 1, 1, 0, w_offset + wtm_width, img_height - h_offset)

			
			drw = pdb.gimp_image_flatten(img)
			
		except Exception as e:
			pdb.gimp_message("Wrong file entered!")

	
	if rsz_toggle == 1: #TODO pridat zadavani velikosti
		if img_width >= img_height:
			pdb.gimp_image_scale(img, 2000, 1335)
		
		if img_width < img_height:
			pdb.gimp_image_scale(img, 1335, 2000)

	if exp_toggle == 1:
		filename = pdb.gimp_image_get_filename(img)
		if filename == None:
			filename = "new_file.jpg"
		else:
			filename = os.path.split(filename)[1]

		fullpath = os.path.join(exp_path, filename)
		#pdb.file_jpeg_save(image, drawable, filename, raw_filename, quality, smoothing, optimize, progressive, comment, subsmp, baseline, restart, dct)
		pdb.file_jpeg_save(img, drw, fullpath, "wtf.jpg", 0.98, 0, 1, 1, "", 2, 1, 0, 0)

	pdb.gimp_undo_push_group_end(img)

def test():
	return os.getcwd()

register(
	"python_fu_resize_and_watermark",
	"Resize and watermark",
	"Resizes image and adds watermark",
	"Marek Nesvadba",
	"Marek Nesvabda",
	"2019",
	"Resize and watermark...",
	"*",
	[
		(PF_IMAGE, "img", "Input image", None),
		(PF_DRAWABLE, "drw", "Input layer", None),
		(PF_TOGGLE, "wtm_toggle", "Add watermark.", 0),
		(PF_RADIO, "side_radio", "Side: ", 0,
			(
				("Right", 0),
				("Left", 1)
			)
		),
		(PF_INT, "w_offset", "Offset of watermark from the side.", 25),
		(PF_INT, "h_offset", "Offset of watermark from the bottom.", 30),
		(PF_FILE, "path", "Watermark file:", ""),
		(PF_TOGGLE, "rsz_toggle", "Resize.", 1),
		(PF_TOGGLE, "exp_toggle", "Export.", 1),
		(PF_DIRNAME, "exp_path", "Output directory:", test()),
	],
	[],
	do_stuff,
	menu="<Image>/Filters"
	)

main()