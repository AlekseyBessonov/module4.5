from django.shortcuts import render

from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from .models import BasicSignupForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from .forms import UserForm


class BaseRegisterView(CreateView):
    model = User
    form_class = BasicSignupForm
    success_url = '/accounts/user'


class UserUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'sign/edit_user.html'
    form_class = UserForm
    success_url = '/'

    # метод get_object мы используем вместо queryset, чтобы получить информацию
    # об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return User.objects.get(pk=id)



@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')