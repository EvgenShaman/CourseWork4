from django.urls import path, include, re_path
from django.views.generic import TemplateView
from accounts.views import *
from rest_framework import routers
from accounts.models import *
from django.core import serializers


router = routers.DefaultRouter()
print(conversation.objects.all())
print(serializers.serialize("json", conversation.objects.all()))

urlpatterns = [
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.jwt')),
    path('api/users', user_view),
    path('api/msg', msg_view),
    path('api/conv', conv_view),
    path('api/connection', connection_view),
    #path('api/conv/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]