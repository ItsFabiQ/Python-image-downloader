import requests
import os

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {save_path}")
    else:
        print(f"Failed to download: {url}")

def download_images(base_url, start, end):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    for i in range(start, end + 1):
        image_number = str(i).zfill(3)  
        image_url = f"{base_url}/z{image_number}.jpg"
        save_path = os.path.join(current_directory, f"z{image_number}.jpg")
        download_image(image_url, save_path)


base_url = "#"
start_image = 1
end_image = 486

download_images(base_url, start_image, end_image)
