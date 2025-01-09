#!/usr/bin/env python3

import os
from PIL import Image

def get_current_dir():
    return os.path.dirname(os.path.realpath(__file__))

def get_image_path(path):
  with open(path) as _in:
    return(_in.readline().strip())

def make_table_from_image(path, width):
    color_rows = []
    column_count = 0
    image = Image.open(path)
    initial_width, initial_height = image.size
    ratio = initial_height / initial_width
    height = int(width * ratio)
    image = image.resize((width, height))

    pixels = list(image.getdata())
    pixel_rows = [pixels[i * width:(i + 1) * width] for i in range(height)]

    for pixel_row in pixel_rows: 
        new_row = []
        for pixel in pixel_row:
            hex_string = ''.join([hex(value)[2:].zfill(2) for value in pixel])
            new_row.append(f'#{hex_string}')
        color_rows.append(new_row)

    with open('table.html', 'w') as _f:
        _f.write('<table>')
        for color_row in color_rows:
            _f.write('<tr>')
            for color_cell in color_row:
                _f.write(f'<td width="6" height="6" bgcolor="{color_cell}"></td>')
            _f.write('</tr>')
            _f.write("\n")
        _f.write('</table>')

    return [len(color_rows), column_count]

if __name__ == '__main__':
    output_width = 100
    current_dir = get_current_dir()
    image_path = get_image_path(f"{current_dir}/source-path.txt")
    details = make_table_from_image(image_path, output_width)
    print(details)




