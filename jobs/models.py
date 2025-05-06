from django.db import models

class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    start_date = models.DateField()
    experience = models.TextField()

    def __str__(self):
        return self.name
