from django.shortcuts import render
from django.http import JsonResponse, Http404

# Create your views here.
import chat.Chatbot.chatbot as Chatbot

chatter = Chatbot.Chatbot(build_console=False)

#print("Hello, I am Mianbot.")

#while True:
#    raw = input()
#    reply,confidence = chatter.testQuestionAnswering(raw)
#    print("%s ,%d" % (reply,confidence))

def chat(request):
    reply,confidence = chatter.testQuestionAnswering(request.GET['sentence'])
    return JsonResponse({'reply':reply, 'confidence':confidence})
    #print("%s ,%d" % (reply,confidence))
