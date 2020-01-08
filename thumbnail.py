from PIL import Image
import sys
import os

path = ""
quality_val = None
height = None
width = None

values = [
    "quality_val",
    "height",
    "width",
]

def set_val(val):
    try:
        user_input = int(input(f"\nSet {val} (default = 100): "))
        globals()[val] = user_input
    except ValueError:
        globals()[val] = int(100)

def display_info():
    sys.stdout.write(
        "\nRun the script from the directory containing the picture."
    )

def set_path():
    global path
    pth = str(input("\nEnter filename: "))
    pth_current_directory = f"./{pth}"
    path += pth_current_directory

def resize():
    try:
        img = Image.open(path)
        new_img = img.resize((height, width), Image.ANTIALIAS)
        new_image_re_1 = path[2:].split(".")[0]
        new_image_re_2 = f"{new_image_re_1}_resized.jpg"
        new_img.save(new_image_re_2, "JPEG", quality = quality_val)
        ##########################################################
        os.remove(path)
        return True
    except FileNotFoundError:
        sys.stderr.write(
            "Incorrect path"
        )
        sys.exit()

def runner():
    display_info()
    set_path()
    for value in values:
        set_val(value)
    resize()

runner()