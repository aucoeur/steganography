"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://make.sc/bew2.3-gradescope)
    - Lesson Plan: https://make-school-courses.github.io/BEW-2.3-Web-Security/#/Lessons/Steganography

Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""
# TODO: Run `pip3 install Pillow` before running the code.
from PIL import Image

def decode_image(path_to_png):
    """
    Checks red channel for LSB(least significant bit) to output hidden text from encoded png
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]
    red_pixels = red_channel.load()

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size


    # Using the variables declared above, replace `print(red_channel)` with a complete implementation:
    # print(red_channel)

    for x in range(0, x_size):
        for y in range(0, y_size):
            # print(f"{red_pixels[x, y]:08b}", red_pixels[x, y])

            if red_pixels[x, y] & 1 == 1:
                pixels[x,y] = (255, 255, 255)
            elif red_pixels[x, y] & 1 == 0:
                pixels[x,y] = (0, 0, 0)

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png):
    """
    Encodes an image with a secret message on the red channel by tweaking its LSB
    """
    pass


def write_text(text_to_write):
    """
    Creates temp image of given text to use when encoding image with secret message
    """
    pass

decode_image('bear_dog.png')
