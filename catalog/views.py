from django.shortcuts import render

from catalog.utils.add_data import add_to_json_file


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(name, phone, message)
        add_to_json_file(name, phone, message)

    return render(request, 'contacts.html')
