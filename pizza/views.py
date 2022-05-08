from django.shortcuts import render, redirect
from .models import Pizza, Topping
#from Pizzeria.forms import CommentForm
from .forms import CommentForm

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


def Comment(request):
    if request.method != "POST":
        form = CommentForm
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save()

            return redirect('Pizzeria:comment')

    context = {'form':form}
    return render(request, 'Pizzeria/pizza.html', context)

