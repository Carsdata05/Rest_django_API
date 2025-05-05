from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_view')
    else:
        form = UserForm()

    users = User.objects.all()
    return render(request, 'users/user_form.html', {'form': form, 'users': users})
