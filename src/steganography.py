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
from PIL import Image, ImageChops, ImageDraw, ImageFont

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

            # bitwise AND operator (&) returns a 1 in each bit position for which the corresponding bits of both operands are 1
            # note: LSB for odd numbers always 1, even numbers always 0 (ie. n % 2)
            if red_pixels[x, y] & 1 == 0:
                pixels[x,y] = (255, 255, 255)
            else:
                # if red_pixels[x, y] & 1 == 1:
                pixels[x,y] = (0, 0, 0)

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")

    # decoded_filename = path_to_png.split('.')
    # decoded_image.save(f'{decoded_filename[0]}-decoded.png')

def encode_image(path_to_png, msg):
    """
    Encodes an image with a secret message on the red channel by tweaking its LSB
    """
    base_image = Image.open(path_to_png)
    x_width, y_height = base_image.size

    pixels = base_image.load()

    hidden_text = write_text(msg, base_image.size)
    secret_pixels = hidden_text.load()

    for x in range(x_width):
        for y in range(y_height):

            red, green, blue, alpha = pixels[x,y]
            text_flag =  secret_pixels[x,y]

            if text_flag == 1:
                # print(red, text_flag, red | text_flag)
                red = red | text_flag
            else:
                # note: LSB for odd numbers always 1, even numbers always 0 (ie. n % 2)
                if red % 2 == 1:
                    red = red ^ 1

            pixels[x,y] = (red, green, blue, alpha)

    new_filename = path_to_png.split('.')
    base_image.save(f'{new_filename[0]}-encoded.png')


def write_text(text_to_write, size):
    """
    Creates temp image of given text to use when encoding image with secret message
    """
    image = Image.new('RGBA', size, (255, 255, 255, 0))

    font = ImageFont.truetype('/Library/Fonts/AvenirLTStd-Black.otf', 24)

    draw = ImageDraw.Draw(im=image)

    draw.text((25, 200), text_to_write, font=font, fill=(255, 255, 255, 1))

    return image.getchannel("A")


if __name__ == "__main__":
    # decode_image('src/bear_dog.png')
    # msg = 'candy camouflage!'
    msg = 'yessir young man!'
    encode_image('src/otgw.png', msg)
    decode_image('src/otgw-encoded.png')
