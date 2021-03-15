from django.db import models

class product(models.Model):
    title=models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    image=models.ImageField(default=False,upload_to='product_image')
    image01=models.ImageField(default=False,upload_to='product_image')
    image02=models.ImageField(default=False,upload_to='product_image')

    def __str__(self):
        return self.title

