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
    context['today_date'] = now.day
    context['today_month'] = now.month
    context['today_year'] = now.year
    return render(request, 'index.html', context)


def word_counter(s):
    return len(s.split())


def number_counter(s):
    count = len(re.findall('\d+', s))


def words(s):
    return list(map(str, re.findall('\w+', s)))


def numbers(s):
    return list(map(int, re.findall('\d+', s)))


@login_required
def str2words(request):
    context = menu()
    ndata = []
    wdata = []
    user = User.objects.filter(username='vasya').first()
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            input_string = form.data['input_string']
            wc = wrd_cntr(input_string)
            context['wrd_cntr'] = wc
            nc = nmbr_cntr(input_string)
            context['nmbr_cntr'] = nc

            today = datetime.datetime.now()
            item = StrHistory(
                date=today.strftime("%d/%m/%Y"),
                time=today.strftime("%H:%M:%S"),
                istring=input_string,
                word_cnt=wc,
                nmbr_cnt=nc,
                author=user
            )
            item.save()

            # List of words
            for i in wrd_list(input_string):
                wdata.append({'item': i})
            context['wdata'] = wdata

            # List of numbers
            for i in nmbr_list(input_string):
                ndata.append({'item': i})
            context['ndata'] = ndata
        else:
            pass
    else:
        context['nothing_entered'] = True
        context['form'] = StringForm()
    return render(request, 'str2words.html', context)


@login_required
def str_history(request):
    context = menu()
    data = StrHistory.objects.all()
    context['data'] = data
    return render(request, 'str_history.html', context)
