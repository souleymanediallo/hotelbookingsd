from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

type = (
    ('S', "sale"),
    ('R', "rent")
)

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(choices=type, max_length=50)
    price = models.PositiveIntegerField()
    area = models.DecimalField(max_digits=8, decimal_places=2)
    bedroom = models.PositiveIntegerField()
    bathroom = models.PositiveIntegerField()
    garage = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    photo_main = models.ImageField(upload_to="photos")
    photo_1 = models.ImageField(upload_to="photos", blank=True, null=True)
    photo_2 = models.ImageField(upload_to="photos", blank=True, null=True)
    photo_3 = models.ImageField(upload_to="photos", blank=True, null=True)
    photo_4 = models.ImageField(upload_to="photos", blank=True, null=True)
    photo_5 = models.ImageField(upload_to="photos", blank=True, null=True)
    photo_6 = models.ImageField(upload_to="photos", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Reserve(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
