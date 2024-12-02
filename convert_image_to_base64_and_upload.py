import requests
import base64
from pathlib import Path


def image_to_base64(image_path):
    """
    Convert an image to a base64-encoded string.
    :param image_path: Path to the image file.
    :return: Base64-encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def upload_image(url, image_path):
    """
    Upload a base64-encoded image to the specified URL.
    :param url: The API endpoint to upload the image.
    :param image_path: Path to the image file.
    :return: Response from the server.
    """
    # Convert the image to a base64 string
    base64_image = image_to_base64(image_path)

    # Prepare the JSON payload
    payload = {
        "file": f"data:image/jpg;base64,{base64_image}",  # Add the base64 image string
        "filename": image_path.split("/")[-1],  # Include the filename (optional)
    }

    # Set headers (if required)
    headers = {
        "Content-Type": "application/json"
    }

    # Send the POST request
    response = requests.post(url, json=payload, headers=headers)

    return response

# Example usage
url = "http://127.0.0.1:8000/api/upload/"  # Replace with your API endpoint
input_dir = "input"
for image_path in Path(input_dir).glob("*.jpg"):
    response = upload_image(url, str(image_path))

# Print the server's response
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
