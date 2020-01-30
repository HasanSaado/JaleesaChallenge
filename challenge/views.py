from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
    babysitters = Babysitter.objects.all()

    form = BabysitterForm()

    if request.method == 'POST':
        form = BabysitterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'babysitters':babysitters, 'form':form}
    return render(request, 'challenge/babysitters.html', context)


def deleteBabysitter(request, pk):
    item = Babysitter.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
    return redirect('/')

    context = {'item':item}
    return render(request, 'challenge/delete.html', context)