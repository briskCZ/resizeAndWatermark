#!/usr/bin/env python

from gimpfu import *
import math, os

def do_stuff(img, drw, wtm_toggle,w_offset,h_offset, path) :
    pdb.gimp_undo_push_group_start(img)


    if wtm_toggle == 1:
        watermark =  pdb.gimp_file_load_layer(img,path)
        pdb.gimp_image_insert_layer(img, watermark, None, 0)
	
        img_width = pdb.gimp_image_width(img)
        img_height = pdb.gimp_image_height(img)
        wtm_width = pdb.gimp_drawable_width(watermark)
        wtm_height = pdb.gimp_drawable_height(watermark)
	
        watermark = pdb.gimp_item_transform_2d(watermark, wtm_width, wtm_height, 1, 1, 0, img_width - w_offset, img_height - h_offset)
    
    pdb.gimp_undo_push_group_end(img)


register(
    "python_fu_resize_and_watermark",
    "Resize and watermark",
    "Resizes image and/or adds watermark",
    "Marek Nesvadba",
    "Marek Nesvabda",
    "2018",
    "Resize and watermark...",
    "*",
    [
        (PF_IMAGE, "img", "Input image", None),
        (PF_DRAWABLE, "drw", "Input layer", None),
        (PF_TOGGLE, "wtm_toggle", "Add watermark.", 1),
        (PF_INT, "w_offset", "Offset of watermark from the right side.", 25),
        (PF_INT, "h_offset", "Offset of watermark from the bottom.", 30),
        (PF_FILE, "path", "Watermark file:", os.getcwd()),
    ],
    [],
    do_stuff,
    menu="<Image>/Filters"
    )

main()