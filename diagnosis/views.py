from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from diagnosis.models import *
# from diagnosis import get_result
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from diagnosis import nltk_null, nltk_lung_aca, nltk_lung_scc, nltk_colon_aca
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications import *

# Create your views here.
model_file = 'model.h5'
model = keras.models.load_model(model_file)
def initpage(request):
    contex = {}
    if request.method == "POST":
        upload_image = request.FILES['cancer_image']
        fs = FileSystemStorage()
        name = fs.save(upload_image.name, upload_image)
        url = fs.url(name)
        print("image name",upload_image.name)
        print("image size",upload_image.size)
        print(url)
        image = Image()
        image.image_name = name
        image.image_path = url
        image.save()
        return render(request, "diagnosis.html", locals())
    return render(request, "main.html", locals())


def result(request):
    image_name = Image.objects.last().image_name
    url = Image.objects.last().image_path
    print('URL:' , url)
    result = get_result(image_name)
    final_result = "Looks like that you have a great chance of getting {}.".format(result)
    print(final_result)
    if result == "lung_n" or result == "colon_n":
        final_result = "Looks like that you do not have any cancer!!"
        return render(request, "result.html", locals())
    elif result == "Colon adenocarcinoma":
        return render(request, "result_colon_adenocarcinoma.html", locals())
    elif result == "Lung adenocarcinoma":
        return render(request, "result_lung_adenocarcinoma.html", locals())
    elif result == "Lung squamous cell carcinoma":
        return render(request, "result_lung_squamous_cell_carcinoma.html", locals())

def scalar(img):
    return img / 127.5 - 1  # scale pixel between -1 and +1

gen = ImageDataGenerator(preprocessing_function=scalar)

def get_result(file_path):
    a = "media/ "
    a = a.strip()
    file_path = a + file_path
    img = tf.keras.preprocessing.image.load_img(file_path, target_size=(128, 128))
    img = tf.keras.utils.img_to_array(img)
    img = np.expand_dims(img, axis=0)

    predictions = model.predict(img)
    pred_id = np.argmax(predictions)

    print("The result for prediction is {}".format(pred_id))

    cancer_type = ["Colon adenocarcinoma", "colon_n", "Lung adenocarcinoma", "lung_n",
                   "Lung squamous cell carcinoma"]

    return cancer_type[pred_id]


def chatbot_null(request):
    Question = 'what cancer do I have'
    if request.method == "POST":
        question =request.POST.get("user_input","")
        print("question:", question)
        response = nltk_null.get_respoonse(question)
        print(response)
        return render(request, "chatbot.html",locals())
    return render(request, "chatbot.html",locals())


def chatbot_colon_aca(request):
    Question = 'what cancer do I have'
    if request.method == "POST":
        question = request.POST.get("user_input", "")
        print("question:", question)
        response = nltk_colon_aca.get_respoonse(question)
        print(response)
        return render(request, "chatbot.html", locals())
    return render(request, "chatbot.html", locals())


def chatbot_lung_aca(request):
    Question = 'what cancer do I have'
    if request.method == "POST":
        question = request.POST.get("user_input", "")
        print("question:", question)
        response = nltk_lung_aca.get_respoonse(question)
        print(response)
        return render(request, "chatbot.html", locals())
    return render(request, "chatbot.html", locals())


def chatbot_lung_scc(request):
    Question = 'what cancer do I have'
    if request.method == "POST":
        question = request.POST.get("user_input", "")
        print("question:", question)
        response = nltk_lung_scc.get_respoonse(question)
        print(response)
        return render(request, "chatbot.html", locals())
    return render(request, "chatbot.html", locals())




