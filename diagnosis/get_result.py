# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

def get_result(file_path):
    model_file = 'D:\djangoProject\model.h5'
    model = keras.models.load_model(model_file)
    a = "D:\djangoProject\media\ "
    a = a.strip()
    file_path = a + file_path
    img = image.load_img(file_path, target_size=(128, 128))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    y = model.predict(x)
    result_y = list(y[0])
    max_index = result_y.index(max(result_y))
    cancer_type = ["lung_n", "colon_aca", "long_aca", "colon_n", "lung_scc"]
    return cancer_type[max_index-1]

