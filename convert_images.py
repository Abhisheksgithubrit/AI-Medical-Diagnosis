from PIL import Image
import os

def convert_images(directory):
    for category in os.listdir(directory):
        category_path = os.path.join(directory, category)
        if os.path.isdir(category_path):
            for img_name in os.listdir(category_path):
                img_path = os.path.join(category_path, img_name)
                try:
                    with Image.open(img_path) as img:
                        rgb_img = img.convert("RGB")  # Convert to JPG format
                        new_img_path = img_path.rsplit(".", 1)[0] + ".jpg"
                        rgb_img.save(new_img_path, "JPEG")
                        if img_path != new_img_path:
                            os.remove(img_path)  # Delete the old image
                except Exception as e:
                    print(f"Error processing {img_path}: {e}")

# Convert images in train and test datasets
convert_images("dataset/train")
convert_images("dataset/test")

print("✅ All images converted to JPG successfully!")
