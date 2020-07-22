from django.shortcuts import render, redirect
from .models import Post, Author, Category
from .forms import CategoryAddForm, AuthorAddForm, PostAddForm


def category_post(request, category_name):
    category = Category.objects.get(name=category_name)
    posts = Post.objects.filter(category=category)
    category_list = Category.objects.all()

    return render(request, 'blog/category_details_new.html', {'posts': posts, 'category_list': category_list, 'name': category_name})

def category_add(request):
    category_list = Category.objects.all()
    forms = CategoryAddForm(request.POST or None)

    if request.method == 'POST':
        if forms.is_valid():
            c_name = forms.cleaned_data["name"]
            Category.objects.create(
                    name=c_name,
                )
            return redirect('category-add')

    context = {
        'forms': forms,
        'category_list': category_list
    }
    return render(request, 'blog/category_add_new.html',context)

def author_list(request):
    authors = Author.objects.all()
    category = Category.objects.all()
    context = {
        'authors': authors,
        'category_list': category
    }

    return render(request, 'blog/author_list_new.html',context)

def authors_post (request, author_name):
    author = Author.objects.get(name=author_name)
    posts = Post.objects.filter(author=author)
    category = Category.objects.all()

    return render(request, 'blog/author_details_new.html', {'posts': posts, 'category_list': category, 'name': author_name})

def author_add(request):
    category_list = Category.objects.all()
    forms = AuthorAddForm(request.POST or None)

    if request.method == 'POST':
        if forms.is_valid():
            c_name = forms.cleaned_data["name"]
            Author.objects.create(
                    name=c_name,
                )
            return redirect('authors')

    context = {
        'forms': forms,
        'category_list': category_list
    }
    return render(request, 'blog/author_add_new.html',context)


def post_list(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    context = {
        'post_list': posts,
        'category_list': category
    }

    return render(request,'blog/post_list_new.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    category = Category.objects.all()
    context = {
        'post': post,
        'category_list': category
    }
    return render(request, 'blog/post_details_new.html', context)

def post_add(request):
    category_list = Category.objects.all()
    forms = PostAddForm()

    if request.method == 'POST':
        forms = PostAddForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save();
            return redirect('post-list')

    context = {
        'forms': forms,
        'category_list': category_list
    }
    return render(request, 'blog/post_add_new.html',context)