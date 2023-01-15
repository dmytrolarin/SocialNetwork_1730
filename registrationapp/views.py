from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login

def show_registration_form(request):
    context = {}
    # Якщо тип запиту дорівнює POST (ТОБТО КОРИСТУВАЧ ВІДПРАВИВ ФОРМУ)
    if request.method == "POST": 
        # зберігаємо данні з форми у змінні
        login = request.POST.get("login")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        context["login"] = login
        context["password"] = password
        context["password_confirm"] = password_confirm
        # Якщо паролі співпадають
        if password == password_confirm:
            # Пробуємо виконати код
            try:
                # Зберігаємо користувача в базі данних
                User.objects.create_user(username = login, password = password)
                # Перекидаємо користувача на сторінку "Успішна реєстрація"
                return redirect('success_reg')
            # Якщо помилка, пов'зана з тим, що користувач вже існує
            except IntegrityError:
                # Видаємо відповідну помилку
                context['error'] = 'Користувач вже існує' 
        else:
            # Передаємо помилку у контекст
            context["error"] = "Паролі не спiвпадають"
            
    return render(request, 'registration_form.html', context)
# Якщо користувач зареєструвався
def show_successfull_reg(request):
    return render(request, 'success_reg.html' )
# Показує сторінку з логіном
def show_login_form(request):
    context = {}
    # Якщо тип запиту дорівнює POST (ТОБТО КОРИСТУВАЧ ВІДПРАВИВ ФОРМУ)
    if request.method == 'POST':
        # перекидуємо данні у змінні 
        login_user = request.POST.get("login")
        password = request.POST.get("password")
        # перевіряємо чи існує такий користувач
        user = authenticate(request, username = login_user, password = password)
        # Якщо user існує
        if user != None:
            # логинить нашого користувача
            login(request, user)
            # перекидує на сторінку "welcome"
            return redirect('welcome')
        else:
            # Якщо сталася помилка
            context['error'] = 'Логін або пароль невірні'
            
    return render(request, 'login_form.html', context)
# відповідае за показ сторінки welcome
def show_welcome(request):
    # якщо користува увійшов в систему (True/Flase)
    if request.user.is_authenticated:
        # повертае наш шаблон сторинки welcome.html
        return render(request, 'welcome.html')
    else:
        # якщо користувача не увійшов в систему перекидує на сторінку login 
        return redirect('login')