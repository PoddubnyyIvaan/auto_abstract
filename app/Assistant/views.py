import os
from django.shortcuts import render, redirect
from django.http import FileResponse, JsonResponse, HttpResponse
from .forms import UserForm, EmailForm, OutForm
from .models import UserModel,OutModel
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from AIHackPrepare.settings import DEFAULT_FROM_EMAIL, BASE_DIR
from django.conf import settings
#from .tasks import order_created
import yadisk
import time

def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    obj = UserModel.objects.get(id=order_id)
    token = 'y0_AgAAAAAzSxLyAArg1wAAAADy4fApYeNMFE5WS0aalIrIJ00O2B_X2KI'
    y = yadisk.YaDisk(token=token)
    y.upload(settings.MEDIA_ROOT+'/'+obj.data_file.name, "app:/input.mp3",overwrite=True)
    while True:
        files = list(map(lambda x: x.name,y.listdir("app:/")))
        if 'out.txt' in files:
            y.download("app:/out.txt", settings.MEDIA_ROOT+"/out.txt")
            y.remove("app:/out.txt", permanently=True)
            obj = OutForm({'file_path':settings.MEDIA_ROOT+"/out.txt"})
            if obj.is_valid():
                obj = obj.save()
                return obj.id
        else:
            time.sleep(10)
def index(request):
    if request.method == "GET":
        form = UserForm()
        return render(request,'index.html',{"form": form})
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            file = form.save()
            Id = order_created(file.id)
            print(Id)
            return redirect(f"upload/{Id}")
        else:
            return JsonResponse(form.errors, status=400)

def upload(request, id):
    if request.method == "GET":
        form = EmailForm()
        return render(request,'upload.html',{"form": form,"id":id})
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = 'Конспект'
            to_email = form.cleaned_data['user_email']
            message = 'Держите готовый конспект, надеюсь он поможет вам в обучении'
            img_obj = OutModel.objects.get(id=id)
            file_path = settings.MEDIA_ROOT+'/'+img_obj.data_file.name
            try:
                email = EmailMessage(subject, message, DEFAULT_FROM_EMAIL, [to_email])
                email.attach_file(file_path)

                # Send the email
                email.send()
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return render(request,'index.html',{"form": UserForm()})
        else:
            return JsonResponse(form.errors, status=400)

def send_file(request,id):
    if request.method=='GET':
        try:
            file = OutModel.objects.get(id=id)
        except OutModel.DoesNotExist:
            return JsonResponse({'success': False, 'err': f'UserModel with id={id} not found'}, status=400)
        return FileResponse(open(file.file_path, "rb"))
    else:
        return JsonResponse({'success': False, 'err': f'This view need GET request'}, status=400)