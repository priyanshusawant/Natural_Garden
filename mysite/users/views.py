from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    form = UserCreationForm()

    if form.is_valid():
        form.save()
        return redirect('plants:index')
    
    else:
        form = UserCreationForm()

        context = {
            'form':form
        }

    return render(request, 'users/register.html', context)