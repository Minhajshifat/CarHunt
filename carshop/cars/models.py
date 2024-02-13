from django.db import models
from carBrand.models import Brand


# Create your models here.
class carModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cars/media/uploads/", blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CommentModel(models.Model):
    car = models.ForeignKey(carModel, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    body = models.TextField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
