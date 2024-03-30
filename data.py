import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_cat_images(num_images, output_folder):
    url = "https://www.pexels.com/search/cat/"
    os.makedirs(output_folder, exist_ok=True)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    image_tags = soup.find_all("img", class_="photo-item__img")

    for i, img_tag in enumerate(image_tags[:num_images]):
        image_url = urljoin(url, img_tag["src"])
        image_path = os.path.join(output_folder, f"{i}.jpg")
        response = requests.get(image_url)
        with open(image_path, "wb") as f:
            f.write(response.content)
            print(f"Downloaded: {image_path}")

if __name__ == "__main__":
    num_images = int(input("Enter the number of cat images to download: "))
    output_folder = "cat_images"
    download_cat_images(num_images, output_folder)
