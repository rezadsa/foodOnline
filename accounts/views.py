from django.shortcuts import render,redirect
from .models import User,UserProfile
from .forms import UserRegisterationForm
from django.contrib import messages

# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        form=UserRegisterationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role=User.CUSTOMER
            user.save()
            messages.success(request,f'{user.username!r} Registered Successfully.')
            return redirect('registerUser')

    else:
        form=UserRegisterationForm()

    context={
        'form': form,
    }

    return render(request, 'accounts/registerUser.html',context)
    
    