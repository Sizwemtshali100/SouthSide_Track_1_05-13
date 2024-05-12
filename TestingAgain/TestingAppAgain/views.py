from django.shortcuts import render, redirect
from .models import Form
from django.contrib.auth.decorators import login_required

@login_required
def Home(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Form.objects.create(user=request.user, title=title, content=content)
        return redirect('Home')
    else:
        forms = Form.objects.filter(user=request.user)
        forms = Form.objects.all()
        return render(request, 'Home.html', {'forms': forms})
