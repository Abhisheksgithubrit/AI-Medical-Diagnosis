import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Set image size
IMG_SIZE = 224  # Resize images to 224x224
BATCH_SIZE = 32  # Number of images processed at once

# Define dataset paths
TRAIN_DIR = "dataset/train/"
TEST_DIR = "dataset/test/"

# Data Augmentation
datagen = ImageDataGenerator(
    rescale=1./255,      # Normalize pixel values
    rotation_range=10,   # Rotate images slightly
    width_shift_range=0.1,  
    height_shift_range=0.1,  
    shear_range=0.1,  
    zoom_range=0.1,  
    horizontal_flip=True,  
    fill_mode="nearest"
)

# Load Training Data
train_generator = datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical'  # Use 'binary' if only two classes (NORMAL/PNEUMONIA)
)

# Load Testing Data
test_generator = datagen.flow_from_directory(
    TEST_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=False
)
