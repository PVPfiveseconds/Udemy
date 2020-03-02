from django.shortcuts import render
from .models import Transaction
import datetime


def home(request):
    date = {'now': datetime.datetime.now(), 'today': ['t1', 't2', 't3']}

    return render(request, 'contas/home.html', date)


def listing(request):
    data = {'transactions': Transaction.objects.all()}
    return render(request, 'contas/listing.html', data)
