from django.db import models

class members(models.Model):

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=500)
    link=models.CharField(max_length=100,null=True)
    link01=models.CharField(max_length=100,null=True)
    link02=models.CharField(max_length=100,null=True)
    link04=models.CharField(max_length=100,null=True)
    image = models.ImageField(default=False,upload_to='Board_member_image')

    def __str__(self):
        return self.position

class board_dicription(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=10000)


class about_us(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=10000)


class contact(models.Model):
    name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    subjects = models.CharField(max_length=100)
    message = models.CharField(max_length=10000)

    def __str__(self):
        return self.subjects + '--Email:--' + self.Email

