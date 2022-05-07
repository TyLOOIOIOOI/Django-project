from django.shortcuts import render
from .models import Pizza, Topping

# Create your views here.
def index(request):
    pizzas = Pizza.objects.all()
    toppings = Topping.objects.all()
    context = {'pizzas': pizzas, 'toppings': toppings}
    return render(request, 'index.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    context = {'pizza':pizza}
    return render(request, 'pizza.html', context)