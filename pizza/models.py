from django.db import models

#from pizza.views import Comment

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    def __str__(self): 
        return self.pizza_name 

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=200)


'''
class Entry(models.Model):
    topic = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name_plural = 'entries'


    def __str__(self): 
        return f"{self.text[:50]}..."

'''


"""
Add a page to the project that shows the names of available pizzas. Then link each pizza name to a page displaying the pizza and its pizza’s toppings. Add a picture for each pizza.
Create a form that allows users to post comments on any particular pizza page
"""