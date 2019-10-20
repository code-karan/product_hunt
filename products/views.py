from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

def home(request):
    return render(request, 'home.html')



@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon'] and request.POST['summary']:
            product = Product()
            product.title = request.POST['title']
            product.summary = request.POST['summary']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            product.date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('home')

        else:
            return render(request, 'create.html', {'error': 'Fields must not be empty!'})

    else:
        return render(request, 'create.html')


