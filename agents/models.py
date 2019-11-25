from django.db import models

# Create your models here.
type = (
    ('Buying Agent', 'Buying Agent'),
    ('Selling Agent', 'Selling Agent'),
    ('Real Estate Brooker', 'Real Estate Brooker'),
)

class Agents(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=type)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    image = models.ImageField(upload_to="photos")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Agents"

    def __str__(self):
        return self.name
