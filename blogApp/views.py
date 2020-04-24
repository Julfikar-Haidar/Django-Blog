from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Author, Category, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import createForm, registration, creteAuthor, commentForm, categoryForm
from django.contrib import messages


# create my views

def index(request):
    post = Article.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    paginator = Paginator(post, 4)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "post": page_obj
    }
    return render(request, "index.html", context)


def getauthor(request, name):
    post_author = get_object_or_404(User, username=name)
    auth = get_object_or_404(Author, name=post_author.id)
    post = Article.objects.filter(article_author=auth.id)
    context = {
        "auth": auth,
        "post": post,
    }
    return render(request, "profile.html", context)


def getsingle(request, id):
    post = get_object_or_404(Article, pk=id)
    first = Article.objects.first()
    last = Article.objects.last()
    getComment = Comment.objects.filter(post=id)
    related_post = Article.objects.filter(category=post.category).exclude(id=id)[:4]
    form = commentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.post = post
        instance.save()
    context = {
        "post": post,
        "first": first,
        "last": last,
        "related_post": related_post,
        "form": form,
        "comment": getComment
    }
    return render(request, "single.html", context)


def getTopic(request, name):
    cat = get_object_or_404(Category, name=name)
    post = Article.objects.filter(category=cat.id)
    return render(request, "category.html", {"post": post, "cat": cat})


def getLogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)

            if auth is not None:
                login(request, auth)
                return redirect("index")
            else:
                messages.add_message(request, messages.ERROR, 'Username and password not match.')

    return render(request, "login.html")


def getLogout(request):
    logout(request)
    return redirect('index')


def getCreate(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Author, name=request.user.id)
        form = createForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author = user
            instance.save()
            return redirect("index")
        return render(request, "create.html", {"form": form})
    else:
        return redirect('login')


# login base profile
def getProfile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        author_profile = Author.objects.filter(name=user.id)
        if author_profile:
            authorUser = get_object_or_404(Author, name=request.user.id)
            post = Article.objects.filter(article_author=authorUser.id)
            return render(request, "login-profile.html", {"post": post, "get_user": authorUser})
        else:
            form = creteAuthor(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.name = user
                instance.save()
                return redirect("profile")
            return render(request, "createAuthor.html", {"form": form})
    else:
        return redirect("login")


# update article post
def getUpdate(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(Author, name=request.user.id)
        post = get_object_or_404(Article, id=pid)
        form = createForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author = user
            instance.save()
            messages.success(request, 'Your Article updated successfully.')
            return redirect("profile")
        return render(request, "create.html", {"form": form})
    else:
        return redirect('login')


def getDelete(request, pid):
    if request.user.is_authenticated:
        post = get_object_or_404(Article, id=pid)
        post.delete()
        messages.warning(request, 'Article deleted successfully')
        return redirect('profile')
    else:
        return redirect('login')


def getRegister(request):
    user_register = registration(request.POST or None)
    if user_register.is_valid():
        instance = user_register.save(commit=False)
        instance.save()
        messages.success(request, 'User successfully Register')
        return redirect('login')
    return render(request, "register.html", {"user_register": user_register})


# get all category show in this page
def getCategory(request):
    category = Category.objects.all()
    return render(request, "categoryTopics.html", {"category": category})


# category add function
def categoryAdd(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            form = categoryForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'Category added successfully')
                return redirect('category')
            return render(request, "createCategory.html", {"form": form})
        else:
            raise Http404('You are not authorised to access this page')
    else:
        return redirect('login')


def categoryUpdate(request, id):
    category = get_object_or_404(Category, id=id)
    form = categoryForm(request.POST or None, instance=category)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Category added successfully')
        return redirect('category')
    return render(request, "createCategory.html", {"form": form})


def categoryDelete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.warning(request, 'Category deleted successfully')
    return redirect('category')

# Create your views here.
