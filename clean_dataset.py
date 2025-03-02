from PIL import Image
import os

# Define dataset directories
train_dir = "dataset/train"
test_dir = "dataset/test"

def remove_corrupt_images(directory):
    for category in os.listdir(directory):  # Loop through NORMAL and PNEUMONIA folders
        category_path = os.path.join(directory, category)
        if os.path.isdir(category_path):
            for img_name in os.listdir(category_path):
                img_path = os.path.join(category_path, img_name)
                try:
                    with Image.open(img_path) as img:
                        img.verify()  # Verify if the image can be opened
                except (IOError, SyntaxError):
                    print(f"🚨 Removing corrupt image: {img_path}")
                    os.remove(img_path)  # Delete the corrupt image

# Clean train and test datasets
remove_corrupt_images(train_dir)
remove_corrupt_images(test_dir)

print("✅ Corrupt images removed successfully!")
