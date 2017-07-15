#!/usr/bin/env python

import os
from gimpfu import *

# highlight cut out window with the guides
def display_cutoff( img, border_lr, border_tb, w_cutoff, h_cutoff ) :
    # display vertical guides
    g1 = border_lr
    g2 = img.width - border_lr

    if( w_cutoff > 0 ) :
        g1 += w_cutoff
        g2 -= w_cutoff

    pdb.gimp_image_add_vguide( img, int( g1 ))
    pdb.gimp_image_add_vguide( img, int( g2 ))

    # display horizontal guides
    g1 = border_tb
    g2 = img.height - border_tb

    if( h_cutoff > 0 ) :
        g1 += h_cutoff
        g2 -= h_cutoff

    pdb.gimp_image_add_hguide( img, int( g1 ))
    pdb.gimp_image_add_hguide( img, int( g2 ))


def print_borders( timg, tdrawable, print_w, print_h, window_w, window_h, cutoff ):
    image_w = tdrawable.width
    image_h = tdrawable.height

    # If the image ratio is greater than window ratio
    # we have to scale the image vertically. The image
    # will cover the window top to bottom, but the sides
    # may be cut off. If the window ratio is greater
    # the horizontal scale will be used.
    image_ratio = image_w / image_h
    window_ratio = window_w / window_h

    if( image_ratio > window_ratio ) :
        scale = image_h / window_h
    else :
        scale = image_w / window_w

    # Calculate new image dimentions.
    print_w_pix = print_w * scale
    print_h_pix = print_h * scale

    # Calculate the number of white pixels to be added
    # on each side.
    border_lr = ( print_w_pix - image_w ) / 2
    border_tb = ( print_h_pix - image_h ) / 2

    timg.disable_undo()

    # Make a copy of the existing image and flatten it.
    newimg = timg.duplicate()
    newimg.flatten()

    # Resize the image and place the existing layer
    # to the center. The white frame will be added
    # around it.
    newimg.resize( int( print_w_pix ), int( print_h_pix ),
                   int( border_lr ), int( border_tb ))

    # Make a white solid layer 
    frame_layer = gimp.Layer( newimg, "frame", int( print_w_pix ), int( print_h_pix ),
                                           RGB_IMAGE, 100, NORMAL_MODE )
    newimg.add_layer( frame_layer, 1 )
    pdb.gimp_edit_fill( frame_layer, WHITE_FILL )
    layer = newimg.flatten()

    # highlight cut out window with the guides
    width_cutoff = (image_w - image_h * window_ratio ) / 2
    height_cutoff = (image_h - image_w / window_ratio ) / 2

    if( cutoff == TRUE ) :
        display_cutoff( newimg, border_lr, border_tb, width_cutoff, height_cutoff )

    name = os.path.splitext( timg.name )[0]
    pdb.gimp_layer_set_name( layer, name )
    pdb.gimp_image_set_filename( newimg, name )

    timg.enable_undo()

    gimp.Display( newimg )
    gimp.displays_flush()

register(
        "python_fu_print_borders",
        "Adds the outside borders to fit certain print size",
        "Adds the outside borders to fit certain print size",
        "Serge Yuschenko",
        "Serge Yuschenko",
        "2015",
        "<Image>/Image/Add Print Borders...",
        "*",
        [
            ( PF_INT, "print_w", "Print Width (in)", 18 ),
            ( PF_INT, "print_h", "Print Height (in)", 12 ),
            ( PF_FLOAT, "window_w", "Window Width (in)", 15.5 ),
            ( PF_FLOAT, "window_h", "Window Height (in)", 10.5 ),
            ( PF_TOGGLE, "cutoff", "Display cutoff lines", True ),
        ],
        [],
        print_borders)

main()
