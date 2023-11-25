from celery import shared_task
from django.core.mail import send_mail
from .models import UserModel
import requests
import time
# def fun1():
#     time.sleep(5)
#     return 1
# @shared_task
# def order_created(order_id):
#     """
#     Задача для отправки уведомления по электронной почте при успешном создании заказа.
#     """
    
    
#     return fun1()