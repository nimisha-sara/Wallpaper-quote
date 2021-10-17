from os import write
from PIL import Image, ImageFont, ImageDraw
from random import choice
import textwrap


# importing image
image = Image.open("path\\files\\wallpaper.jpg")

# importing font style
font_style = ImageFont.truetype('path\\files\\Alegreya-SemiBoldItalic.ttf', 60)

# reading quotes in data.txt file and storing each as a list item.
with open('path\\files\\data.txt', encoding="utf8") as data_file:
    quotes = [line.rstrip() for line in data_file]

# selecting a random quote from list
title_text = choice(quotes)

# wrapping the text in image

title_text = "\n".join(textwrap.wrap(title_text, width=37)) # 35

# converting image to a editable format
image_editable = ImageDraw.Draw(image)

# rendering image - (Starting Coordinates with (0,0) in the upper left corner,
#                    text, color, font)
if title_text.count('\n') >= 4:
    cor = (1350,400) # 900, 100
else:
    cor = (1350, 450) # 900, 200
image_editable.text(cor, title_text, (230, 230, 230), font=font_style)

# saving rendered image
image.save(r"path\\result.jpg")
image.close()
