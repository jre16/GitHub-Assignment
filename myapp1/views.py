from django.shortcuts import render, get_object_or_404, redirect
from .forms import VideoForm
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'myapp1/video_list.html', {'videos': videos})

def video_detail(request, movie_id):
    video = get_object_or_404(Video, movie_id=movie_id)
    return render(request, 'myapp1/video_detail.html', {'video': video})

def video_create(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'myapp1/video_form.html', {'form': form})

def video_update(request, movie_id):
    video = get_object_or_404(Video, movie_id=movie_id)
    if request.method == "POST":
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('video_detail', movie_id=video.movie_id)
    else:
        form = VideoForm(instance=video)
    return render(request, 'myapp1/video_form.html', {'form': form})

def video_delete(request, movie_id):
    video = get_object_or_404(Video, movie_id=movie_id)
    if request.method == "POST":
        video.delete()
        return redirect('video_list')
    return render(request, 'myapp1/video_confirm_delete.html', {'video': video})