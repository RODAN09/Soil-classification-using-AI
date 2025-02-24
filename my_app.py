from flask import Flask,render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

model = load_model('advance_model.h5') 

# Classes for prediction
soil_types = [ 'Black Soil', 'Sandy Soil', 'Loamy Soil', 'Yellow Soil', 'Cinder Soil']

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    """Handle the prediction of soil type."""
    soil_image = request.files.get('soil_image')
    soil_video = request.files.get('soil_video')

    # Check if both files are uploaded
    if soil_image and soil_video:
        return render_template('index.html')

    # Handle soil image prediction
    if soil_image:
        # Save the uploaded image
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], soil_image.filename)
        soil_image.save(file_path)

        # Preprocess the image
        img = image.load_img(file_path, target_size=(224, 224))  # Adjust target size to your model
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict the soil type
        prediction = model.predict(img_array)
        soil_type = soil_types[np.argmax(prediction)]

        # # Cleanup uploaded file
        os.remove(file_path)

        # Redirect to the appropriate HTML template based on prediction
        if soil_type == 'Black Soil':
            return render_template('black.html')
        elif soil_type == 'Sandy Soil':
            return render_template('sandy.html')
        elif soil_type == 'Loamy Soil':
            return render_template('loamy.html')
        elif soil_type == 'Yellow Soil':
            return render_template('yellow.html')
        else:  # Cinder Soil
            return render_template('cinder.html')

    # Handle soil video upload
    if soil_video:
        return render_template("page_error.html")

    # If no file is uploaded
    return render_template('index.html', error="No file uploaded. Please try again.")

if __name__ == "__main__":
    app.run(debug = True,port=5000)