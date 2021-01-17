from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class Category(models.Model):
    sort = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.sort)

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    image = models.ImageField(upload_to='photos')
    price = models.IntegerField()
    price_text = models.TextField(default="")
    fabric = models.TextField(default="")
    size = models.TextField(default="")
    color = models.TextField(default="")
    quantity = models.IntegerField(default=99)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)
    hit = models.IntegerField(default=0)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return '{}'.format(self.name)

class Point(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_point')
    all_point = models.IntegerField()
    able_point = models.IntegerField()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wish_product', blank=True)
    
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '{} // {}'.format(self.user, self.products.name)

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_order')
    name = models.CharField(max_length=100, verbose_name='주문자_이름')
    amount = models.PositiveIntegerField(verbose_name='결제금액', default="")
    home = models.CharField(max_length=100, verbose_name='배송지', default="")
    phone = models.CharField(max_length=100, verbose_name='연락처', default=00000000000)
    quantity = models.IntegerField(default=1)
    products = models.TextField(max_length=100, verbose_name='주문상품', default="")
    order_requset = models.TextField(default="")
    order_date = models.DateTimeField(auto_now_add=True)

    #모델 인스턴스를 아이디 값 내림차순 정렬
    class Meta:
        ordering = ('-order_date',)

    def __str__(self):
        return '{}의 주문 [{}]'.format(self.user, self.order_date)

class Image(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image', blank=True)
    image = models.ImageField(upload_to='photos')
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-products',)

    def  __str__(self):
        return '{}의 이미지 [{}]'.format(self.products, self.order_date)
