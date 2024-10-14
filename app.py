from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

imgs_path = r".\static\data\seg"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['file']
        image = []
        for scene in os.listdir(imgs_path):
            # print(scene)
            scene_imgs = os.path.join(imgs_path,scene)
            for img in os.listdir(scene_imgs):
                img_path = os.path.join(scene_imgs,img)
                image.append(img_path)
                break
            # image.append()
        return render_template('index.html',result=image)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=9000)