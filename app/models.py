from django.db import models

class About(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

class Guarantee(models.Model):
    guarantee = models.CharField(max_length=60)


class Service(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    icon = models.CharField(max_length=50)

class Feature(models.Model):
    icon = models.CharField(max_length=50)
    title1 = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)

class Doctor(models.Model):
    name = models.CharField(max_length=70)
    job = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/doctors')
    fc = models.URLField
    twitter = models.URLField
    inst = models.URLField

class Testimonial(models.Model):
    image = models.ImageField(upload_to='images/patients')
    text = models.TextField()
    name = models.CharField(max_length=70)
    proffesion = models.CharField(max_length=40)

