import random
from PIL import Image

# List of image file paths
image_files = ["image1.jpg", "image2.jpg", "image3.jpg"]

def generate_slot_images():
    # Generate three random images from the list
    slot_images = random.sample(image_files, 3)
    return slot_images

def display_slot_images(slot_images):
    # Display the generated slot images
    print("Slot Machine Images:")
    print("---------------------")
    for image_path in slot_images:
        image = Image.open(image_path)
        image.show()
        print("---------------------")


slot_images = generate_slot_images()
display_slot_images(slot_images)
