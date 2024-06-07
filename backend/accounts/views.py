# Create your views here.
from .forms import messageForm, connectionForm, conversationForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics
from django.core import serializers
from django.http import HttpResponse
import json


from .models import message, conversation, User_conv, UserAccount
from .serializers import MessageSerializer, convSerializer, connectionSerializer

'''@csrf_exempt
def msg_view(request):

    if request.method == 'POST':

        form = messageForm(request.POST)
        # Проверяем правильность введенных данных
        if form.is_valid():
            # сохраняем в базу
            form.save()
            return "Успешно"
    else:
        form =messageForm()
        context = {
            'form': form
        }
        return render(request, 'create.html', context)

@csrf_exempt
def conv_view(request):
    print(request)
    if request.method == 'POST':
        print(form.errors)
        form = conversationForm(request.POST)
        print(form.errors)
        # Проверяем правильность введенных данных
        if form.is_valid():
            # сохраняем в базу
            form.save()
        print(form.errors)
        return redirect('/')
    else:
        form =conversationForm()
        context = {
            'form': form
        }
        return render(request, 'create.html', context)    
@csrf_exempt
def connection_view(request):

    if request.method == 'POST':

        form = connectionForm(request.POST)
        # Проверяем правильность введенных данных
        if form.is_valid():
            # сохраняем в базу
            form.save()
            return "Успешно"
    else:
        form = connectionForm()
        context = {
            'form': form
        }
        return render(request, 'create.html', context)'''


@csrf_exempt
def msg_view(request):
    if request.method == 'GET':
        form = message.objects.all()
        return HttpResponse(serializers.serialize('json', form), content_type='application/json')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        form = messageForm(body_data)
        print("created")
        # Проверяем правильность введенных данных
        if form.is_valid():
            # сохраняем в базу
            form.save()
        print(form.errors)
        return HttpResponse(form)
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        message.objects.filter(id=body_data.get('id')).update(name=body_data.get('name'))
        return HttpResponse("changed")
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        print(message.objects.filter(id=body_data.get('id')))
        message.objects.filter(id=body_data.get('id')).delete()
        return HttpResponse("deleted")

@csrf_exempt
def conv_view(request):
    if request.method == 'GET':
        form = conversation.objects.all()
        return HttpResponse(serializers.serialize('json', form), content_type='application/json')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        form = conversationForm(body_data)
        print("created")
        if form.is_valid():
            form.save()
        print(form.errors)
        return HttpResponse(form)
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        conversation.objects.filter(id=body_data.get('id')).update(name=body_data.get('name'))
        return HttpResponse("changed")
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        print(conversation.objects.filter(id=body_data.get('id')))
        conversation.objects.filter(id=body_data.get('id')).delete()
        return HttpResponse("deleted")

@csrf_exempt
def connection_view(request):
    if request.method == 'GET':
        form = User_conv.objects.all()
        return HttpResponse(serializers.serialize('json', form), content_type='application/json')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        form = connectionForm(body_data)
        print("created")
        # Проверяем правильность введенных данных
        if form.is_valid():
            # сохраняем в базу
            form.save()
        print(form.errors)
        return HttpResponse(form)
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        User_conv.objects.filter(id=body_data.get('id')).update(name=body_data.get('name'))
        return HttpResponse("changed")
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        print(User_conv.objects.filter(id=body_data.get('id')))
        User_conv.objects.filter(id=body_data.get('id')).delete()
        return HttpResponse("deleted")

@csrf_exempt
def user_view(request):
    if request.method == 'GET':
        form = UserAccount.objects.all()
        return HttpResponse(serializers.serialize('json', form), content_type='application/json')
    return HttpResponse("NOT AVAILIBLE")

user_view


'''class MsgApi(viewsets.ModelViewSet):
    queryset = message.objects.all()
    serializer_class = MessageSerializer

class ConvApi(viewsets.ModelViewSet):
    queryset = conversation.objects.all()

    serializer_class = convSerializer

class ConnectionsApi(viewsets.ModelViewSet):
    queryset = User_conv.objects.all()
    serializer_class = connectionSerializer
'''
