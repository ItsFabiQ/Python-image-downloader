﻿# Image Downloader Script

This Python script downloads a series of images from a specified URL format and saves them in the same directory as the script.

## Features

- Downloads images from a specified URL format.
- Saves images in the same directory as the script.
- Allows customization of the range of images to download.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the script.
2. Install the required library using pip:
   ```bash
   pip install requests
   ```

## Configuration

1. Set the `base_url` variable in the script to the base URL of your images. Replace the `#` with your actual base URL.
2. Set the `start_image` and `end_image` variables to define the range of images you want to download.

## Usage

1. Run the script:
   ```bash
   python program.py
   ```
2. The script will download the images and save them in the same directory as the script.

## Code Explanation

### Main Script

```python
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
        image_url = f"{base_url}/{image_number}.jpg"
        save_path = os.path.join(current_directory, f"{image_number}.jpg")
        download_image(image_url, save_path)


base_url = "#"  # Replace this with your actual base URL
start_image = 1
end_image = 486

download_images(base_url, start_image, end_image)
```

### Explanation

- **Imports**: The script imports necessary libraries including `requests` and `os`.
- **download_image Function**: This function downloads an image from a given URL and saves it to the specified path.
- **download_images Function**: This function iterates over a range of image numbers, constructs the image URLs, and calls `download_image` to download each image.
- **Example Usage**: The script sets the `base_url`, `start_image`, and `end_image` variables and calls `download_images` to download the images.

## License

This project is licensed under the MIT License.



