# Convert image to JSON and save to file
python image_to_json.py living_room_100x75_L.png > pixels.json
# Run script in blender (reads pixels.json)
blender image.blend -P json_image_to_blender.py
