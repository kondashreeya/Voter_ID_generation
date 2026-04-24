from django.db import models

class Voter(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    voter_no = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.name
