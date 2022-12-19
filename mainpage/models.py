from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_description = models.TextField()
    def __str__(self):
        return self.dept_name
class Doctor(models.Model):
    doc_name=models.CharField(max_length=255)
    dept_name = models.ForeignKey(Department,on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctors')
    def __str__(self):
        return self.doc_name
class Appointments(models.Model):
    patient_name = models.CharField(max_length=200)
    dept_name = models.ForeignKey(Department,on_delete=models.CASCADE)
    a_date = models.DateField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.patient_name
    class Meta:
        ordering =("-date",)


