from django.shortcuts import render, get_object_or_404, redirect
from .models import Meme

def home(request):
    memes = Meme.objects.all()
    return render(request, 'memes/home.html', {'memes': memes})

def add_meme(request):
    if request.method == 'POST':
        image = request.FILES['image']
        caption = request.POST['caption']
        Meme.objects.create(image=image, caption=caption)
    return render(request, 'memes/add_meme.html')

def delete_meme(request, meme_id):
    meme = get_object_or_404(Meme, id=meme_id)
    meme.delete()
    return redirect('home')  # Redirects to the 'home' view
