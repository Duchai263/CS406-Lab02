import os
import numpy as np
import faiss
import histogram

dataset_path = r".\static\data\seg"
index2path = {}
dimension = 768
db = faiss.IndexFlatL2(dimension)
def calcHists():
    idx = 0
    for scene in os.listdir(dataset_path):
        scene_imgs = os.path.join(dataset_path,scene)
        for image_name in os.listdir(scene_imgs):
            img_path = os.path.join(scene_imgs,image_name)
            hist = histogram.calcHist(img_path)
            
            index2path[idx] = img_path
            db.add(hist) 
            idx = idx + 1

def search(hist):
    hist = hist.reshape(1,-1)
    distances, indices = db.search(hist, 10)
    indices = indices.tolist()[0]
    print(indices)
    results = [index2path[x] for x in indices]

    return results

# if __name__ == '__main__':


# # Perform a search for the 10 nearest neighbors
# query_vector = np.random.random((1, d)).astype('float32')
# distances, indices = index.search(query_vector, 10)

# print(distances, indices)