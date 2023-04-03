from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import os
from . forms import AddPost, CommentForm
from . models import BlogPost, Category, Comment


def home(request):
    post = BlogPost.objects.all()[:5]
    total_post = BlogPost.objects.count()
    context = {'post': post, 'total_post': total_post}
    return render(request, 'blog/home.html', context)


def detail(request, id):

    post_detail = BlogPost.objects.get(id=id)
    comments = Comment.objects.filter(commentpost=post_detail).order_by('created_on')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            if not request.user.is_authenticated:
                return redirect('login')
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.commentpost = post_detail
            new_comment.save()
            return redirect('/post/' + str(id))
    else:
        
        form = CommentForm()
        print(form.errors)
    return render(request, 'blog/post_article.html', {'post_detail': post_detail, 'form': form, 'comments': comments})
@login_required
def comment_replies(request, post_id, parent_id):
    post_detail = BlogPost.objects.get(id=post_id)
    parent_comment  = Comment.objects.get(id=parent_id)
    print(parent_comment)
    form = CommentForm()
    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():
            comment_reply = form.save(commit=False)
            comment_reply.commentpost = post_detail
            comment_reply.parent = parent_comment
            comment_reply.author = request.user

            comment_reply.save()
        return redirect('detail', post_id)

def load_more(request):
    # get total items currently being displayed
    total_item = int(request.GET.get('total_item'))
    # amount of additional posts to be displayed when i click on load more
    limit = total_item + 3
    posts = list(BlogPost.objects.all()[total_item: limit])
    print(posts)
    data = {
        'posts': posts,
    }

    return JsonResponse(data=data)


@login_required
def Addpost(request):
    form = AddPost()
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.author = request.user
            submission.save()
        else:
            form = AddPost()

    return render(request, 'blog/new_post.html', {'form': form})


def search(request):

    search_input = request.GET.get('search-area') or ''

    data = BlogPost.objects.filter(title__icontains=search_input)

    # data['search_input'] = search_input

    return render(request, 'blog/search_result.html', {'data': data})
# configure tinymce to allow file upload


@csrf_exempt
def upload_image(request):
    if request.method != "POST":
        return JsonResponse({'detail': "Wrong request"})
    file_obj = request.FILES['file']
    file_name_suffix = file_obj.name.split(".")[-1]
    if file_name_suffix not in ["jpg", "png", "gif", "jpeg", ]:
        return JsonResponse({"message": "Wrong file format"})

    path = os.path.join(
        settings.MEDIA_ROOT,
        'tinymce',
    )
    # If there is no such path, create
    if not os.path.exists(path):
        os.makedirs(path)

    file_path = os.path.join(path, file_obj.name)

    file_url = f'{settings.MEDIA_URL}tinymce/{file_obj.name}'

    if os.path.exists(file_path):
        return JsonResponse({
            "message": "file already exist",
            'location': file_url
        })

    with open(file_path, 'wb+') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    return JsonResponse({
        'message': 'Image uploaded successfully',
        'location': file_url})