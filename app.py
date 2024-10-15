from flask import Flask, render_template, request, send_file
import os
import sys
import shutil
import cv2
import numpy as np
import histogram
import database

app = Flask(__name__)

dataset_path = r".\static\data\seg"

if (not os.path.exists(dataset_path)):
    sys.exit("NO IMAGES DATASET")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        file_name = "temp" + os.path.splitext(file.filename)[1]
        file_path = os.path.join(r"static",file_name)
        file.save(file_path)

        hist = histogram.calcHist(file_path)

        results = database.search(hist)

        return render_template('index.html', original = file_path,result=results)
    return render_template('index.html')

if __name__ == '__main__':
    database.calcHists()
    app.run(port=5000)