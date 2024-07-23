from PIL import Image, ImageEnhance, ImageFilter
import os

path = "/content/pics"
pathOut = "/content/editedpics"

for filename in os.listdir(path):
    if filename.endswith(('.jpg', '.jpeg', '.png')): # Check if file is an image
        img = Image.open(f"{path}/{filename}")
        # sharpening, BW
        edit = img.filter(ImageFilter.SHARPEN)
        # contrast
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(1.0)
        # brightness
        enhancer = ImageEnhance.Brightness(edit)
        edit = enhancer.enhance(1.1)
        # blur
        edit = edit.filter(ImageFilter.BLUR)

        clean_name = os.path.splitext(filename)[0]
        edit.save(f'{pathOut}/{clean_name}_edited.jpg')
