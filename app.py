import os

internal_dir = "/Users/danielmulatarancon/Desktop/Documents/HACKING TIME/Brainnest /Week 03/Advance Tasks/Internal_directory"

file_path = 'example.txt'

new_file_path = os.path.join(internal_dir, os.path.basename(file_path))

os.rename(file_path, new_file_path)
