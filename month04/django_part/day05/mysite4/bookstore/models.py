from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField('书名', max_length=20, unique=True)
    price = models.DecimalField('定价', max_digits=5, decimal_places=2)
    market_price = models.DecimalField('零售价', max_digits=5, decimal_places=2)
    press = models.CharField('出版社', max_length=30)

    def __str__(self):
        return "\ntitle:%s\nprice:%s\nmarket_price:%s\npress:%s\n" % \
               (self.title, self.price, self.market_price, self.press)

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = '图书'
