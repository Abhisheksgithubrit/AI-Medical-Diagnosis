from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image

app = Flask(__name__, static_folder="static")

# Load trained model
model = tf.keras.models.load_model("medical_diagnosis_model.h5")

# Define image size
IMG_SIZE = (150, 150)

# Serve the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filepath = os.path.join("static", file.filename)
    file.save(filepath)

    # Load image
    img = image.load_img(filepath, target_size=IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Predict
    prediction = model.predict(img_array)[0][0]
    result = "Pneumonia" if prediction > 0.5 else "Normal"

    return jsonify({"filepath": filepath, "prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
