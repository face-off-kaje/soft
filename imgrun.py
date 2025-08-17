from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

img = Image.open("C:/Users/ROSHA/Desktop/sent-sw/img/main.png")

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 60)

texts = [
(1650, 480, "خانم رضائی"), (570, 690, "فاقد هرگونه وسایل"), (470, 763, "کارت گرافیک ایراد داره"), (600, 990, "فاقد پیچ و مهره")
]


for x, y, text in texts:
    fate = arabic_reshaper.reshape(text)
    otext = get_display(fate)
    draw.text((x,y), otext, font=font, fill="black")


img.save("C:/Users/ROSHA/Desktop/sent-sw/result/output.png")
