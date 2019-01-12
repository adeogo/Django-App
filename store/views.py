from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Store
from.forms import StoreForm

def index(request):
	context = {}
	return render(request, 'store/index.html', context)


def list(request):
	lists = Store.objects.order_by('-id')[:5]
	context = {'lists' : lists}
	return render(request, 'store/list.html', context)


def add(request):

	form = StoreForm()

	context = {'form': form}
	return render(request, 'store/add.html', context)


@require_POST
def store(request):
	store = StoreForm(request.POST)

	if store.is_valid():
		new_store = Store(name = request.POST['name'], email = request.POST['email'])
		new_store.save()

	return redirect('list')
