Image Pixel Visualization in Blender
=====================================

Generates 3D depictions of images in Blender. Intended for use in
computer-vision education and such.

Samples
-------

####My living room, one channel

![](http://www.patrick-fuller.com/img/living_room_3d.png)

####My living room after being passed through a Gaussian filter

![](http://www.patrick-fuller.com/img/gauss_room.png)

####A visualization of a 21x21 Gaussian kernel

![](http://www.patrick-fuller.com/img/gauss_kernel.png)

####A visualization of a 21x21 Gabor kernel

![](http://www.patrick-fuller.com/img/gabor_kernel.png)

Dependencies
------------

This depends on the Python Image Library for image parsing.

```bash
pip install PIL
```

Usage
-----

```bash
sh draw_image.sh my_image.png
```

Without the command line, you can copy and paste the contents of
`json_image_to_blender.py` into Blender, update the path to `pixels.json`, and run.

This is intended to work only with grayscale images. But, by messing with the
`image_to_json.py` file, you can do multi-channel visualizations easily enough.

The `blender_filter_sampler.py` file generates json for common convolutio
kernels. Open the file, comment/uncomment whatever functions you want, and then
run `python blender_filter_sampler.py > pixels.json`.

######Warning: The script cannot handle images larger than ~50,000 pixels. Scale input images down before running.
