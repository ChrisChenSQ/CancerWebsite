import numpy as np
from tensorflow import keras
from keras.preprocessing import image

def get_result():
    model_file = 'djangoProject\model.h5'
    model = keras.models.load_model(model_file)

    file_path = "djangoProject\lung_colon_image_set\lung_image_sets\lung_aca\lungaca91.jpeg"
    img = image.load_img(file_path, target_size=(128, 128))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    y = model.predict(x)
    a = list(y[0])
    result = ["lung_n", "colon_aca", "lung_aca", "colon_n", "lung_scc"]
    return result[a.index(max(a))]
