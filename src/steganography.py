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
from PIL import Image, ImageDraw, ImageFont

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
            # nb. LSB for odd numbers always 1, even numbers always 0
            if red_pixels[x, y] & 1 == 0:
                pixels[x,y] = (255, 255, 255)
            else:
                # if red_pixels[x, y] & 1 == 0:
                pixels[x,y] = (0, 0, 0)

    # DO NOT MODIFY. Save the decoded image to disk:
    # decoded_image.save("decoded_image.png")
    decoded_filename = path_to_png.split('.')
    decoded_image.save(f'{decoded_filename[0]}-decoded.png')


def encode_image(path_to_png, msg):
    """
    Encodes an image with a secret message on the red channel by tweaking its LSB
    """
    base_image = Image.open(path_to_png)
    pixels = base_image.load()

    redc = base_image.split()[0]
    greenc = base_image.split()[1]
    bluec = base_image.split()[2]

    red = redc.load()
    green = greenc.load()
    blue = bluec.load()

    x_width, y_height = base_image.size

    hiddenText = write_text(msg, base_image.size)

    secret_red = hiddenText.split()[0]
    secret_pixel = secret_red.load()

    for x in range(x_width):
        for y in range(y_height):
            red_flag = bin(red[x,y])[-1]
            text_flag = bin(secret_pixel[x,y])[-1]

            if int(text_flag[-1]) & 1 == 1:
                red[x,y] = int(bin(red[x,y])[:-1]+"1", 2)
            elif int(text_flag[-1]) & 1 == 0:
                red[x,y] = int(bin(red[x,y])[:-1]+"0", 2)


            pixels[x,y] = (red[x, y], green[x,y], blue[x,y])

    new_filename = path_to_png.split('.')
    base_image.save(f'{new_filename[0]}-encoded.png')

def write_text(text_to_write, size):
    """
    Creates temp image of given text to use when encoding image with secret message
    """
    image = Image.new("RGB", size, (0, 0, 0))

    font = ImageFont.truetype('/Library/Fonts/AvenirLTStd-Black.otf', 24)

    draw = ImageDraw.Draw(im=image)

    draw.text((25, 200), text_to_write, font=font, fill=(255, 255, 255, 255))

    return image


if __name__ == "__main__":
    # decode_image('src/bear_dog.png')
    msg = 'candy camouflage!'
    encode_image('src/over_the_garden_wall.png', msg)
    decode_image('src/over_the_garden_wall-encoded.png')
