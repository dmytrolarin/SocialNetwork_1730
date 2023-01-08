from django.shortcuts import render, redirect
from django.contrib.auth.models import User



def show_registration_form(request):
    context = {}
    # Якщо тип запиту дорівнює POST (ТОБТО КОРИСТУВАЧ ВІДПРАВИВИ ФОРМУ)
    if request.method == "POST": 
        # зберігаємо данні з форми у змінні
        login = request.POST.get("login")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        # Якщо паролі співпадають
        if password == password_confirm:
            # Зберігаємо користувача в базі данних
            User.objects.create_user(username = login, password = password)
            # Перекидаємо користувача на сторінку "Успішна реєстрація"
            return redirect('success_reg')
        else:
            # Передаємо помилку у контекст
            context["error"] = "Паролі не спiвпадають"
            
    return render(request, 'registration_form.html', context)

def show_successfull_reg(request):
    return render(request, 'success_reg.html' )