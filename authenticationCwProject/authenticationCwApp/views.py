from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import FoodFitnessForm
from django.contrib.auth.models import User


# function to test with
def index(request):
    return HttpResponse("You made it.")


# function to create new user
def createUser(request):
  form = FoodFitnessForm(request.POST or None)
  context = {
      "form": form
  }
  if request.method == "POST":
      print(request.POST)
      User.objects.create_user(request.POST["username"], request.POST["calories"], request.POST["date"])
      return render(request, "authenticationCwApp/confirmUser.html")

  return render(request, 'authenticationCwApp/createUser.html', context)



# function to confirm new user
def confirmUser(request):
    form = FoodFitnessForm(request.GET or None)
    context = {
        "form": form
    }

    if request.method == 'GET':
        User.objects.create_user(request.GET["username"], "", request.GET["calories"], request.GET["date"])
        form.save()
        return HttpResponse("New Food Calorie Tracker Created!!!!!")

    return render(request, "authenticationCwApp/confirmUser.html", context)
