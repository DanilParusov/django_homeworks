from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        email = request.POST.get('email')
        # а также передается информация, которую заполнил пользователь
        print(f"{name} - {email}")
    return render(request, 'catalog/contacts.html')
