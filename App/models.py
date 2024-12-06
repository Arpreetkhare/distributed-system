from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places= 2)

    def __str__(self):
        return self.name 


class Order(models.Model):

    order_id =  models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order {self.order_id}  of {self.product.name } by {self.user.name}"
