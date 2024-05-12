from django.shortcuts import render, redirect
from .models import TheForm
from django.contrib.auth.decorators import login_required

@login_required
def form_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        TheForm.objects.create(user=request.user, title=title, content=content)
        return redirect('form_view')
    else:
        forms = TheForm.objects.filter(user=request.user).count()
        Okay = TheForm.objects.all()
        return render(request, 'Home.html', {'forms': forms,
                                             'Okay':Okay})
