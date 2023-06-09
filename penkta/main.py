from PIL import Image, ImageEnhance
import requests

url = "https://cataas.com/cat"
img_name = "cat.jpg"
new_img_name = "cat_updated.jpg"


def save_image(name, data):
    with open(name, "wb") as cat_img:
        cat_img.write(data)


def get_image(img_url, name):
    response = requests.get(img_url)
    if response.ok:
        save_image(name, response.content)


get_image(url, img_name)

image = Image.open(img_name)
contrast = ImageEnhance.Contrast(image)
new_img = contrast.enhance(5)

new_img.show()
new_img.save(new_img_name)
