from django.db import models

class UserModel(models.Model):
    data_file = models.FileField(verbose_name='Файл', upload_to="video/")
    status = models.PositiveSmallIntegerField(verbose_name='Статус', choices=((0, 'Загружен'), (1, 'В работе'), (2, 'Ошибка'), (3, 'Готово')), default=0)

class EmailModel(models.Model):
    user_email =  models.EmailField(verbose_name='Почта')
    
class OutModel(models.Model):
    file_path = models.TextField()
