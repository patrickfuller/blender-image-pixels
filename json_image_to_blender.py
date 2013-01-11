#!/usr/bin/env python
"""
Loads a file of pixel values and converts to bar heights for use in Blender.
"""

import bpy
import json

# Initialize scene and primitive
bpy.ops.object.select_all(action="DESELECT")
bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.object
cube.scale = (0.1, 0.1, 0.1)

# Add colors in the user-specified map
for i in range(256):
    key = "L%d" % i
    bpy.data.materials.new(name=key)
    # Convert [0, 255] to (r, g, b)
    bpy.data.materials[key].diffuse_color = (i / 255.0,) * 3
    bpy.data.materials[key].specular_intensity = 0.02


def pixels_to_blender(pixels, z_scale=0.05):
    """ Iterates through pixels and draws vertical bars """

    # Keep references to all pixels
    shapes = []

    # Iterate through data an make bars
    for y, row in enumerate(pixels):
        print("Processing column %d" % (y + 1))
        for x, pixel in enumerate(row):

            # Copy a cube primitive
            bar = cube.copy()
            bar.data = cube.data.copy()
            size = cube.scale.z

            # Move and scale
            bar.location = (2 * size * x, -2 * size * y,
                            size * pixel * z_scale)
            bar.data.materials.append(bpy.data.materials["L%d" % pixel])
            bar.scale.z *= pixel * z_scale

            # Link to scene and save
            shapes.append(bar)
            bpy.context.scene.objects.link(bar)

    # Remove primitive meshes
    bpy.ops.object.select_all(action='DESELECT')
    cube.select = True
    # If the starting cube is there, remove it
    if "Cube" in bpy.data.objects.keys():
        bpy.data.objects.get("Cube").select = True
    bpy.ops.object.delete()

    # Join pixel shapes
    for shape in shapes:
        shape.select = True
    bpy.context.scene.objects.active = shapes[0]
    bpy.ops.object.join()

    # Update scene and exit function
    bpy.context.scene.update()

# Read json data and run through Blender
if __name__ == "__main__":
    with open("pixels.json") as indata:
        pixels = json.load(indata)
    pixels_to_blender(pixels)
