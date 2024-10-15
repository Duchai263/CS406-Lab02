from flask import Flask, render_template, request, send_file
import os
import sys
import shutil
import cv2
import histogram
import numpy as np

app = Flask(__name__)

dataset_path = r".\static\data\seg"
histogram_path = r".\static\data\histograms"

if (not os.path.exists(dataset_path)):
    sys.exit("NO IMAGES DATASET")

def calcHists():
    for scene in os.listdir(dataset_path):
        scene_imgs = os.path.join(dataset_path,scene)
        for image_name in os.listdir(scene_imgs):
            img_path = os.path.join(scene_imgs,image_name)
            
            hist = histogram.calcHist(img_path)
            # print(os.path.splitext(image_name))
            np.save(os.path.join(histogram_path,os.path.splitext(image_name)[0]),hist)
            # exit()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['file']
        return render_template('index.html',result=image)
    return render_template('index.html')

if __name__ == '__main__':
    if (not os.path.exists(histogram_path)):
        os.makedirs(histogram_path)
        calcHists()
        
    app.run(port=9000)