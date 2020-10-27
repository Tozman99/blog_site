from django.shortcuts import render

# Create your views here.


def home_view(request):

    if request.method == "POST":
        pass
        #request.POST[f"query"] = 
    
    return render(request, "home.html", {})