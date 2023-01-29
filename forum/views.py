from django.shortcuts import render
from forum.models import Post

# Create your views here.
def show_forum(request):
    # якщо користувач НАДІСЛАВ форму.
    if request.method == 'POST':
        # беремо у змінні данні з форми
        title =  request.POST.get("title")
        content = request.POST.get("content")
        author = request.user.username
        image = request.FILES.get("image")
        # створюємо пост
        Post.objects.create(title = title, content = content, author = author, image = image)
    #отримуємо усі пости, щоб відобразити їх у шаблоні
    posts = Post.objects.all()
    return render(request, "forum.html", context = {'posts': posts})
    