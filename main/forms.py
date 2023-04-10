from django.forms import ModelForm, TextInput
from .models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'style': 'color:black',
            })
        }
