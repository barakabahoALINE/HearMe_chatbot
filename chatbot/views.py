from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserInput
from chatbot.sentiment_analysis import analyze_sentiment
from chatbot.video_reccomendation import recommend_videos
from django.shortcuts import render
from .forms import ChatForm  # Import your form class


def chatbot_home(request):
    return render(request, 'chatbot/index.html')
# Ensure correct template path
# Make sure the template file exists at hearme/templates/chatbot/index.html


def chatbot_view(request):
    form = ChatForm()  # Instantiate the form
    return render(
        request, 'index.html', {'form': form}
    )  # Pass the form to the template


def chat_view(request):
    response = None
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            # Process the user input (e.g., generate a chatbot response)
            response = (
                f"You said: {user_input}"  # Replace with actual chatbot logic
            )
    else:
        form = ChatForm()

    return render(request, 'chat.html', {'form': form, 'response': response})


@api_view(['POST'])
def analyze_input(request):
    text = request.data['text']
    emotion = analyze_sentiment(text)
    videos = recommend_videos(emotion)

    UserInput.objects.create(text=text, emotion=emotion)

    return Response({"emotion": emotion, "videos": videos})


@api_view(['GET'])
def get_user_inputs(request):
    user_inputs = UserInput.objects.all().values('text', 'emotion')
    return Response({"user_inputs": list(user_inputs)})
