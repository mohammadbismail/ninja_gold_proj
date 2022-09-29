from django.shortcuts import render, redirect
import random


def index(request):
    if "gold" not in request.session:
        request.session[
            "gold"
        ] = 0  # if there is not gold obtained yet, set the value for zero

    return render(request, "index.html")


def find_gold_farm(request):
    gold = random.randint(10, 20)
    request.session["gold"] += gold
    message = f"You entered a farm and earned {gold} gold"
    return redirect("/")


def find_gold_cave(request):
    gold = random.randint(10, 20)
    request.session["gold"] += gold
    message = f"You entered a cave and earned {gold} gold"
    return redirect("/")


def find_gold_house(request):
    gold = random.randint(10, 20)
    request.session["gold"] += gold
    message = f"You entered a house and earned {gold} gold"
    return redirect("/")


def find_gold_quest(request):
    gold = random.randint(-50, 50)
    request.session["gold"] += gold
    request.session["message"] = f"You entered a quest and earned {gold} gold"
    return redirect("/")
