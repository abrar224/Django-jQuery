from django.shortcuts import render
from .forms import Registration
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    form = Registration()
    std = User.objects.all()
    return render(request,'home.html', {'form':form, 'std':std})

@csrf_exempt
def data_save(request):
    if request.method =="POST":
        form = Registration(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            batch = request.POST['batch']
            dept = request.POST['dept']
            user = User(name = name, email = email, batch = batch, dept = dept)
            user.save()
            std = User.objects.values()
            s_data = list(std)
            return JsonResponse({'status':'Save', 's_data':s_data})
        else:
            return JsonResponse({'status':0})

@csrf_exempt
def data_delete(request):
    if request.method =="POST":
        id = request.POST.get('id')
        id = str(id)
        sid = ''
        for i in id:
            if i.isdigit():
                sid = sid + i
        sid = int(sid)
        d = User.objects.get(pk=sid)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})



            
