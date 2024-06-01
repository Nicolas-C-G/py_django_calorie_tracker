from django.shortcuts import render, redirect
from .models import Food, Consume

# Create your views here.
def index(request):

    user = request.user
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consumed = Food.objects.get(name=food_consumed)
        consumed = Consume(user=user, food_consumed=consumed)
        consumed.save()
        foods = Food.objects.all()
        consumed_food = Consume.objects.filter(user=user)
    else:
        foods = Food.objects.all()
        consumed_food = ""
        if Consume.objects.filter(user=user) != "":
            consumed_food = Consume.objects.filter(user=user)

    return render(request, 'calorieTracker/index.html',{'foods':foods, 'consumed_food':consumed_food})

def delete_consume(request,id):

    consumed_food = Consume.objects.get(id=id)
    if request.method == "POST":
        consumed_food.delete()
        return redirect('/')
    
    return render(request, 'calorieTracker/delete.html')