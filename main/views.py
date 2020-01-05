import datetime
import re

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from main.forms import StringForm
from main.models import StrHistory


def menu():
    data = [
        {'url': '/', 'text': 'Главная страница'},
        {'url': '/login', 'text': 'Вход'},
        {'url': '/str2words', 'text': 'Строка->слова'},
        {'url': '/str_history', 'text': 'История запросов'},
        {'url': '/logout', 'text': 'Выйти'}]
    context = {'data': data}
    return context


def index(request):
    context = menu()
    now = datetime.datetime.now()
    context['today'] = now.strftime("%d/%m/%Y")
    context['time'] = now.strftime("%H:%M:%S")
    return render(request, 'index.html', context)


def word_counter(s):
    a = []
    for i in s.split():
        if not i.isdigit():
            a.append(i)
    return len(a)


def number_counter(s):
    return len(re.findall('\d+', s))


def words(s):
    a = []
    for i in s.split():
        if not i.isdigit():
            a.append(i)
    return a


def numbers(s):
    return list(map(int, re.findall('\d+', s)))


@login_required
def str2words(request):
    context = menu()
    number_data = []
    word_data = []
    user = User.objects.filter(username='vasya').first()
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            input_string = form.data['input_string']
            context['word_counter'] = word_counter(input_string)
            context['number_counter'] = number_counter(input_string)
            now = datetime.datetime.now()
            item = StrHistory(
                date=now.strftime("%d/%m/%Y"),
                time=now.strftime("%H:%M:%S"),
                string=input_string,
                word_count=word_counter(input_string),
                number_count=number_counter(input_string),
                author=user)
            item.save()

            for i in words(input_string):
                word_data.append({'item': i})
            context['word_data'] = word_data

            for i in numbers(input_string):
                number_data.append({'item': i})
            context['number_data'] = number_data
        else:
            context['form'] = form
            context['errors'] = 'Найдены ошибки в данных формы'
    else:
        context['nothing_entered'] = True
        context['form'] = StringForm()
    return render(request, 'str2words.html', context)


@login_required
def str_history(request):
    context = menu()
    datahistory = StrHistory.objects.all()
    context['datahistory'] = datahistory
    return render(request, 'str_history.html', context)
