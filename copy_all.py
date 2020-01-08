import os
import subprocess
import argparse

parser = argparse.ArgumentParser(
    description = "Copy all images to or from the thumbnail container."
)

parser.add_argument('-d', type = str, required = True)
args = vars(parser.parse_args())

img_types = [
    ".png", ".jpg", ".jpeg"
]

to_variants = [
    "to", "To"
]

from_variants = [
    "From", 'from'
]

def access_volume():
    ls_out = subprocess.run(args = ["docker", "exec", "thumbnail", "ls"],
    universal_newlines = True, stdout = subprocess.PIPE)
    lines = ls_out.stdout.splitlines()
    return lines

def access_directory():
    return os.listdir(".")

def return_images(code):
    image_list = []
    for items in code:
        for img_type in img_types:
            if img_type in items:
                image_list.append(items)
    return image_list

def remove_whitespace(code):
    for item in return_images(code):
        for i in item:
            if ord(i) == 32:
                try:
                    os.rename(item, item.replace(" ", "_"))
                    remove_whitespace(code)
                except FileNotFoundError as e:
                    print(f"Excepted {e} as {item}. Renaming ok.")


def copy_to_container(image):
    subprocess.run(
        f"docker cp ./{image} thumbnail:/application"
    )

def copy_from_container(image):
    subprocess.run(
        f"docker cp thumbnail:/application/{image} ."
    )

def runner():
    if args['d'] in to_variants:
        remove_whitespace(access_directory())
        for image in return_images(access_directory()):
            copy_to_container(image)
    elif args['d'] in from_variants:
        for image in return_images(access_volume()):
            copy_from_container(image)

runner()



