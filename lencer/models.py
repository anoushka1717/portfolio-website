from django.db import models

# Create your models here.
class datas(models.Model):
    FileID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    File = models.FileField(upload_to= 'files/')
    Image = models.ImageField(upload_to='photos/',blank=True,null=True)
    def _str_(self):
        return self.Name
    
