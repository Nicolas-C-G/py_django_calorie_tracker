from django.shortcuts import render
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