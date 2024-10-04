from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, UserFavouriteArticle
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CommentForm

def home(request):
    return redirect('article_list')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

@login_required
def user_articles(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, 'blog/user_articles.html', {'articles': articles})

@login_required
def article_detail(request, pk):  # Changer 'article_id' en 'pk'
    article = get_object_or_404(Article, id=pk)  # Utiliser 'pk' ici

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            # Rediriger vers la page de détail de l'article après l'envoi du commentaire
            return redirect('article_detail', pk=article.id)
    else:
        form = CommentForm()

    return render(request, 'blog/article_detail.html', {'article': article, 'form': form})

@login_required
def favourites(request):
    favourites = UserFavouriteArticle.objects.filter(user=request.user)
    return render(request, 'blog/favourites.html', {'favourites': favourites})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('article_list')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('article_list')
