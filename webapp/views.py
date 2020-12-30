from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from . import models
from django.shortcuts import redirect

def get_state():
    State = models.State
    return State.objects.first().state



# Create your views here.
def index(request):
    return render(request, 'index.html', {"state":get_state()})


def login(request, methods=["POST"]):
    return render(request, "login.html")

def login_post(request):

    user = authenticate(username=request.POST["username"], password=request.POST["password"])

    request.session["auth"] = True

    if user is not None:
        return render(request, "switch.html")
    else:
        return render(request, "index.html", {"state":get_state, "message_type":"bad", "message": "Login failed"})

def switch(request):
    State = models.State
    state = State.objects.first()

    #print("user: ", request.user.username)
    #print("auth: ", request.session["auth"])

    if not request.session["auth"]:
        return render(request, "index.html", {"state":get_state, "message_type":"bad", "message": "User not authenticated"})


    new_state = request.POST["state"]
   # print("state: ", state.state)
    #print("new state: ", new_state)

    state.state = new_state
    state.save()

    return redirect("index")