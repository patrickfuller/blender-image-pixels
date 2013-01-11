Image Pixel Visualization in Blender
=====================================

Generates 3D depictions of images in Blender. Intended for use in computer-vision education and such.

This depends on the Python Image Library for image parsing.
```bash
pip install PIL
```

Usage
-----

```bash
sh draw_image.sh my_image.png
```

Without the command line, you can copy and paste the contents of `json_image_to_blender.py` into Blender, update the path to `pixels.json`, and run.

This is intended to work only with grayscale images. But, by messing with the `image_to_json.py` file, you can do multi-channel visualizations easily enough.

The `blender_filter_sampler.py` file generates json for common convolution kernels. Open the file, comment/uncomment whatever functions you want, and then run `python blender_filter_sampler.py > pixels.json`.

######Warning: The script cannot handle images larger than ~10,000 pixels. Scale input images down before running.

Samples
-------

####My living room, one channel

![](http://www.patrick-fuller.com/wp-content/uploads/2012/10/living_room_100x75.png)

####My living room after being passed through a Gaussian filter

![](http://www.patrick-fuller.com/wp-content/uploads/2012/11/gauss10.png)

####A visualization of a 21x21 Gaussian kernel

![](http://www.patrick-fuller.com/wp-content/uploads/2012/11/gauss.png)

####A visualization of a 21x21 Gabor kernel

![](http://www.patrick-fuller.com/wp-content/uploads/2012/11/gabor.png)

####Red, green, and blue channels of Lenna

![](http://www.patrick-fuller.com/wp-content/uploads/2012/11/colored_rgb_lenna.png)
