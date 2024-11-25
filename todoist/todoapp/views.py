from django.shortcuts import render, redirect
from .models import Todo, status_choices



def main(request):
    if request.method == 'GET':
        t = Todo.objects.all()
        return render(request, 'main.html', {'todos':t, 'statuses': status_choices})
    elif request.method == 'POST':
        desc = request.POST.get('desc')
        status = request.POST.get('status')
        date = request.POST.get('date')
        temp  = Todo(
            desc = desc,
            status = status,
            date = date
        )
        temp.save()
        return redirect('/')
    
def del_view(request, pk):
    t = Todo.objects.get(pk=pk)
    t.delete()
    return redirect('/')