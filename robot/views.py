from django.shortcuts import render
from django.http import HttpResponse
from .forms import infoForm
import os, openai
# Create your views here.
# Your API KEY
openai.api_key = 'Your API KEY'
# GPT3.5模型
model_id = 'gpt-3.5-turbo'

def robot_view(request):
    if request.method == 'POST':
        form = infoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            descriptions = form.cleaned_data['descriptions']
            response = ChatGPT_conversation(descriptions)
            return render(request, 'result.html', 
                          {'name': name, 'descriptions': descriptions, 'response': response})
    else:
        form = infoForm()
    return render(request, 'index.html', {'form': form})

def ChatGPT_conversation(descriptions):
    conversation = []
    conversation.append({'role': 'system', 'content': 'prompt'}) # 請輸入您的prompt以讓GPT3.5模型更理解您的問題
    conversation.append({'role': 'user', 'content': descriptions})
    
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = conversation
    )    
    conversation.append({'role': 'assistant', 'content': response.choices[0].message.content})
    return response.choices[0].message.content