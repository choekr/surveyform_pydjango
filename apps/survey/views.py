from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "survey/index.html");

def process(request):
    try:
        request.session['count'] += 1
    except Exception:
        request.session['count'] = 1

    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session["location"] = request.POST["location"]
        request.session["language"] = request.POST["language"]
        request.session["comment"] = request.POST["comment"]
        return redirect("/result")
    else:
        return redirect('/')

def result(request):
    return render(request, "survey/result.html")
