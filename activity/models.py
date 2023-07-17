from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
CATEGORY=(
    ('M','M'),
    ('F','F')
)
class worker(models.Model):
    First_Name = models.CharField(max_length= 200)
    Middle_Name = models.CharField(max_length= 200,null=True)
    Gender = models.CharField(max_length= 200,choices=CATEGORY,null=True)
    Id_Number = models.CharField(max_length= 200,null=True,blank=True)
    Phone = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.First_Name} {self.Middle_Name}'
    def pending_payments(self): 
        total_salary = self.attendance_set.filter(presentstatus='Present',paystatus='Pending').aggregate(models.Sum('salary'))['salary__sum'] or 0
        return total_salary

    @staticmethod
    def total_pending_payments(): 
        total_salary = attendance.objects.filter(presentstatus='Present',paystatus='Pending').aggregate(models.Sum('salary'))['salary__sum'] or 0
        return total_salary     

      
STATUS=(
    ('Pending','Pending'),
    ('Paid','Paid'),
    ('Absent','Absent')
)
COMINGSTATUS=(
    ('Absent','Absent'),
    ('Present','Present')
)        

class attendance(models.Model):
    name=models.ForeignKey(worker,on_delete=models.CASCADE)
    date=models.DateField()
    presentstatus=models.CharField(max_length= 200,choices=COMINGSTATUS,default='Absent')
    paystatus=models.CharField(max_length= 200,choices=STATUS,default='Absent')
    salary =models.DecimalField(max_digits=10,decimal_places=2,null=True)

    def __str__(self):
        return f'{self.name}'
    