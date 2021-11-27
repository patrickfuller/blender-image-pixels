# Convert image to JSON and save to file
python image_to_json.py -i $1 -o pixels.json

# Run script in blender (reads pixels.json)
if [[ $(uname -s) == "Darwin" ]]; then
    # Mac version, assumes no blender link
    /Applications/blender.app/Contents/MacOS/./blender pixels.blend -P json_image_to_blender.py
else
    blender pixels.blend -P json_image_to_blender.py
fi
