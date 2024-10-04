# ex00/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Tip
from .forms import TipForm

def tips_list(request):
    tips = Tip.objects.all()  # Récupère tous les Tip
    return render(request, 'ex00/tips.html', {'tips': tips})

def tips(request):
    all_tips = Tip.objects.all()  # Récupérer toutes les astuces
    return render(request, 'ex00/tips.html', {'tips': all_tips})

def home(request):
    tips = Tip.objects.all().order_by('-created_at')  # Récupère tous les tips par date
    form = None
    if request.user.is_authenticated:
        form = TipForm()  # Crée le formulaire si l'utilisateur est connecté

    return render(request, 'ex00/home.html', {'tips': tips, 'form': form})

def create_tip(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = TipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user  # Associe l'utilisateur connecté comme auteur
            tip.save()
            messages.success(request, 'Tip créé avec succès !')
            return redirect('home')  # Redirige vers la page d'accueil

    messages.error(request, 'Vous devez être connecté pour créer un tip.')
    return redirect('home')  # Redirige vers la page d'accueil en cas d'erreur

# Inscription d'un nouvel utilisateur
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur est déjà utilisé.')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('home')

    return render(request, 'ex00/signup.html')

# Connexion d'un utilisateur
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')

    return render(request, 'ex00/login.html')

# Déconnexion de l'utilisateur
def logout_view(request):
    logout(request)
    return redirect('home')

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tip

@login_required
def upvote_tip(request, tip_id):
    
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user in tip.downvotes.all():
        tip.downvotes.remove(request.user)
    if request.user not in tip.upvotes.all():
        tip.upvotes.add(request.user)
    tip.author.update_reputation()  # Mettez à jour la réputation de l'auteur
    return redirect('home')

@login_required
def downvote_tip(request, tip_id):
    if not request.user.can_downvote:
        return redirect('home')  # Rediriger si l'utilisateur n'a pas la permission
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user in tip.upvotes.all():
        tip.upvotes.remove(request.user)
    if request.user not in tip.downvotes.all():
        tip.downvotes.add(request.user)
    return redirect('home')

@login_required
@permission_required('app_name.delete_tip', raise_exception=True)  # Remplacez app_name par le nom de votre app
def delete_tip(request, tip_id):
    if request.user.reputation < 30:
        return redirect('home')
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user == tip.author or request.user.has_perm('app_name.delete_tip'):
        tip.delete()
        return redirect('tips_list')
    return redirect('home')
