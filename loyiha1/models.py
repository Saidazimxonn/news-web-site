from django.db import models

# Create your models here.

class Blog(models.Model):
    user = models.CharField('Muallif nomi', max_length=100)
    title = models.CharField('Maqola nomi', max_length=255)
    text = models.TextField('Maqola matni')
    date = models.DateTimeField('vaqt',auto_now_add=True)

    def __str__(self):
        return f'{self.user} qalamiga mansub {self.title}'
    

class Position(models.Model):
    UNVON=(
        ('Y','bor'),
        ('NO', 'yoq'),
        ('Z','----')
    )
    title= models.CharField('Darajasi', max_length=100)
    unvoni = models.CharField('Unvoni', choices=UNVON,default='Z',max_length=10 )

    def __str__(self):
        return self.title

class Users(models.Model):
    name =  models.CharField(verbose_name='Isim',max_length=100)
    l_name= models.CharField('Falmilya', max_length=100)
    position= models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.name





