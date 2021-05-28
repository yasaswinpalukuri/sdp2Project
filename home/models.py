from django.db import models
from django.contrib.auth.models import User



departments=[('tiny house','Tiny Houses'),
('apartment','Apartments'),
('bungalow','Bungalows'),
('commercial','Commercial Buildings'),
('individual house','Individual Houses'),
('mansion','Mansions'),
('palace','Palaces')
]

class Designer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DesignerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Tiny Houses')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)



class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    measurements = models.CharField(max_length=100,null=False)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.measurements+")"


class Project(models.Model):
    customerId=models.PositiveIntegerField(null=True)
    designerId=models.PositiveIntegerField(null=True)
    customerName=models.CharField(max_length=40,null=True)
    designerName=models.CharField(max_length=40,null=True)
    discussionDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)



class ProjectCompletion(models.Model):
    customerId=models.PositiveIntegerField(null=True)
    customerName=models.CharField(max_length=40)
    assignedDesignerName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    measurements = models.CharField(max_length=100,null=True)

    startDate=models.DateField(null=False)
    endDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    workCharge=models.PositiveIntegerField(null=False)
    equipmentCost=models.PositiveIntegerField(null=False)
    designerFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total = models.PositiveIntegerField(null=False)
