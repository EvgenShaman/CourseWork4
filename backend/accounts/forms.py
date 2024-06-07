from .models import message, conversation, User_conv
from django.forms import ModelForm


class messageForm(ModelForm):

    class Meta:
        model = message
        fields = ('text', 'sender', 'conv')

class conversationForm(ModelForm):

    class Meta:
        model = conversation
        fields = ('name', )

class connectionForm(ModelForm):

    class Meta:
        model = User_conv
        fields = ('sender', 'conv')