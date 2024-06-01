from flask import render_template, request
import os
import cv2




UPLOAD_FOLDER = "static/upload"


def index():
    return render_template('index')

def app():
    return render_template('app')

def genderapp():
    
    if request.method=="POST":
        f = request.files['image_name']
        filename = f.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(path)
        
        
        
        pred_filename = "Prediction_image.jpg"
        
        cv2.imwrite(f"./static/predict/{pred_filename}")
        print("Machine Learning model executed Sucessfully")
        
        
        
        
    return render_template('gender')










