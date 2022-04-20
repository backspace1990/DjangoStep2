from importlib.resources import contents
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.http import Http404

# Create your views here.
# Icinde python fonksiyonlari yazacagimiz
# yerdir.
# Kullanicinin istekte bulunmasi ve web 
# sitesinin bu isteklere cevap vermesi 
# burada katmanda yazilan fonksiyonlarla
# saglanir.
# tr karsiligi goruntu demektir view

# Migrations : Uygulamanin veritabanini tutan yerdir. 
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def post_index(request):
    posts_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        posts_list = posts_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)).distinct()

    paginator = Paginator(posts_list, 3)

    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post/index.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'post':post,
        'form':form,
    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    #form = PostForm(request.POST)
    #context = {
    #    'form': form,
    #}
    #if request.method == "POST":
        #print(request.POST)
    #if request.method == "POST": #1.YONTEMMMMMMM
    #    title = request.POST.get('title')
    #    content = request.POST.get('content')
    #    Post.objects.create(title=title, content=content)

    #---------Iyi yontem 1 ---------
    #if request.method == "POST":
    #    #formdan gelen bilgileri kaydet
    #    form = PostForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #else:
    #    #formu kullaniciya goster
    #    form = PostForm()
    #
    #context = {
    #    'form': form,
    #}
    #---------------------Iyi yontem 1 sonu
    #---------Iyi yontem2  ---------
    #if not request.user.is_authenticated():
    #    return Http404() #yetkisiz veya tam uyelik olusturmamis kullanicilar siteye erisemeyecekler

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Basarili bir post olusturdunuz')
        return HttpResponseRedirect(post.get_absolute_url())
    
    context = {
        'form': form,
    }
    #---------------------Iyi yontem 2 sonu
    return render(request, 'post/form.html', context)


def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Postu basariyla guncellediniz')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post/update.html', context)


def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')


