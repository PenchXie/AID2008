from django.db import models

# Create your models here.
class Press(models.Model):
    name = models.CharField('出版社', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = "出版社"

class Book(models.Model):
    title = models.CharField('书名', max_length=50)
    press = models.ForeignKey(Press, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "图书"
        verbose_name_plural = "图书"