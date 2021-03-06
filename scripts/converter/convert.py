#!/usr/bin/env python3

from PIL import Image


def make_table_from_image(path, width):

    image = Image.open(path)
    initial_width, initial_height = image.size
    ratio = initial_height / initial_width
    height = int(width * ratio)
    image = image.resize((width, height))

    pixels = list(image.getdata())
    pixel_rows = [pixels[i * width:(i + 1) * width] for i in range(height)]

    color_rows = []

    for pixel_row in pixel_rows: 
        new_row = []
        for pixel in pixel_row:
            hex_string = ''.join([hex(value)[2:].zfill(2) for value in pixel])
            new_row.append(f'#{hex_string}')
        color_rows.append(new_row)
    print(color_rows)

    with open('index.html', 'w') as _f:
        _f.write('<table>')
        for color_row in color_rows:
            _f.write('<tr>')
            for color_cell in color_row:
                _f.write(f'<td width="6" height="6" bgcolor="{color_cell}"></td>')
            _f.write('</tr>')
            _f.write("\n")
        _f.write('</table>')


if __name__ == '__main__':

    make_table_from_image(
        '/Users/alan/Graphics/magritte-son-of-man-1964.jpg',
        100
    )



