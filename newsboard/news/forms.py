from django.forms import ModelForm
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


# Создаём модельную форму
class NewsForm(ModelForm):
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['title', 'text', 'categoryType', 'author']

class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email']