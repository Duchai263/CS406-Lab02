# CS406-Lab02
# Installation  
Create a virtual environment using  
`python -m venv venv`  
activate `venv` by  
`venv/scripts/activate`

Clone repo and install python and install requirements with  
`$ pip install -r requirements.txt`  
# Usage  
Run the app with  
`python app.py`  
and go to `http://127.0.0.1:5000/`  

Upload an image  
Things this repo do:  
Find 10 similar images by rgb histogram with euclidian distance 
#### Note:  
dataset: `https://drive.google.com/file/d/1F6sPtl0H-Sh7XPrAojDKcz_rBoUl_fgu/view?usp=sharing`  
Take a while to start app  
using FAISS for faster search with over 14k images  