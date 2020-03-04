from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
import datetime

def home(request):
    date = {'now': datetime.datetime.now(), 'today': ['t1', 't2', 't3']}
    return render(request, 'contas/home.html', date)

def listing(request):
    data = {'transactions': Transaction.objects.all()}
    return render(request, 'contas/listing.html', data)

def newTransaction(request):
    form = TransactionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listingURL')

    return render(request, 'contas/forms.html', {'form': form})

def update(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    form = TransactionForm(request.POST or None, instance=transaction)

    if form.is_valid():
        form.save()
        return redirect('listingURL')

    data = {}
    data['form'] = form
    data['transaction'] = transaction

    return render(request, 'contas/forms.html', data)

def delete(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.delete()

    return redirect('listingURL')
