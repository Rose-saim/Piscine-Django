from django.shortcuts import render
from .forms import MyForm
from django.conf import settings
import os
from datetime import datetime

def display_form(request):
    history = []
    
    # Chargement de l'historique depuis le fichier de logs
    log_file_path = settings.LOG_FILE_PATH  # Assurez-vous que cette variable est définie dans settings.py
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            history = [line.strip().split(' - ') for line in log_file.readlines()]

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data['text_field']
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Écriture dans le fichier de log
            with open(log_file_path, 'a') as log_file:
                log_file.write(f"{entry} - {timestamp}\n")

            # Ajout à l'historique
            history.append([entry, timestamp])
    else:
        form = MyForm()

    context = {
        'form': form,
        'history': history,
    }
    return render(request, 'ex02/index.html', context)
