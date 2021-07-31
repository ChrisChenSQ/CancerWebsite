from django.urls import path
from . import views

urlpatterns = [
    path('', views.initpage, name="initpage"),
    path('result', views.result, name="result"),
    path('chatbot1',views.chatbot_null, name = "chatbot_null"),
    path('chatbot2', views.chatbot_colon_aca, name = "chatbot_colon_aca"),
    path('chatbot3', views.chatbot_lung_scc, name = "chatbot_lung_scc"),
    path('chatbot4', views.chatbot_lung_aca, name = "chatbot_lung_aca"),
]