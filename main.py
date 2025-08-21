import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

INPUT_PATH = "C:/Users/ROSHA/Desktop/sent-sw/img/main.png"
OUTPUT_PATH = "C:/Users/ROSHA/Desktop/sent-sw/result/output.png"
TEXTS_POS = [
    (1650, 480, "client"), (570, 690, "ach"), (470, 763, "bugClien"), (600, 990, "bugFace"), (200, 230, "serialNum"),
    (1450, 1340, "client"), (120, 1520, "ach"), (110, 1680, "bugClien"), (110, 1880, "bugFace"), (150, 1210, "serialNum"),
    (1300, 2250, "client"), (482, 2485, "ach"), (420, 2560, "bugClien"), (505, 2750, "bugFace"), (1350, 2100, "serialNum"),
]

entries = {}

def save_image():
    client = entries["client"].get()
    ach = entries["ach"].get()
    bugClien = entries["bugClien"].get()
    bugFace = entries["bugFace"].get()
    serialNum = entries["serialNum"].get()

    img = Image.open(INPUT_PATH)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 60)
    for x, y, key in TEXTS_POS:
        text = locals()[key]
        if text.strip():
            fate = arabic_reshaper.reshape(text)
            otext = get_display(fate)
            draw.text((x, y), otext, font=font, fill="black")

    img.save(OUTPUT_PATH)
    messagebox.showinfo("موفقیت", f"عکس با موفقیت ذخیره شد در:\n{OUTPUT_PATH}")

root = tk.Tk()
root.title("ثبت رسید")
root.geometry("500x500")
labels = {
    "client": "نام مشتری",
    "ach": "اقلام همراه دستگاه",
    "bugClien": "ایراد به اظهار مشتری",
    "bugFace": "ایراد ظاهری",
    "serialNum": "سریال"
}

for key, text in labels.items():
    lbl = tk.Label(root, text=text, anchor="e", width=20)
    lbl.pack()
    ent = tk.Entry(root, width=40, justify="right")
    ent.pack(pady=2)
    entries[key] = ent
btn_save = tk.Button(root, text="💾 Save", command=save_image, bg="lightgreen")
btn_save.pack(pady=20)

root.mainloop()
