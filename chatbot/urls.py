from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_home, name='chatbot_home'),
    path('api/analyze/', views.analyze_input, name='analyze_input'), 
    path('chat/', views.chat_view, name='chat'),
]
