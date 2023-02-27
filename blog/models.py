from django.db import models

class TecMembers(models.Model):
    Co_Name = models.CharField(max_length=100)
    Clas1 = models.CharField(max_length=30)
    Sub_Clas1 = models.CharField(max_length=30)
    Sub_Clas2 = models.CharField(max_length=30)
    Sub_Clas3 = models.CharField(max_length=30)
    Sub_Clas4 = models.CharField(max_length=30)
    No_tec = models.CharField(max_length=2)
    Office = models.CharField(max_length=10)
    Specific = models.TextField()
    Web_Page = models.CharField(max_length=100)
    Cel_Number = models.CharField(max_length=30)
