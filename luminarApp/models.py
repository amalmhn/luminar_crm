from datetime import date

from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50,unique=True)
    course_duration = models.CharField(max_length=50)
    def __str__(self):
        return self.course_name

class Batch(models.Model):
    batch_code = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    batch_date = models.DateField(default=date.today())
    course_fees = models.CharField(max_length=50)
    action={
        ('1','Yet to Begin'),
        ('2', 'Ongoing'),
        ('3', 'Completed'),
    }
    batch_status = models.CharField(max_length=30,choices=action)
    def __str__(self):
        return self.batch_code

class Enquiry(models.Model):
    enquiryId = models.CharField(primary_key=True, editable=False , max_length=150)
    student_name = models.CharField(max_length=100)
    address = models.TextField()
    qualification = models.CharField(max_length=50)
    collegename = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    contact = models.IntegerField()
    email = models.EmailField(unique=True)
    enquirydate = models.DateField(default=date.today())
    followup_date = models.DateField()
    action = {
        ('1', 'Call back'),
        ('2', 'Admitted'),
        ('3', 'Cancel'),
    }
    status = models.CharField(max_length=20,choices=action)
    def __str__(self):
        return str(self.enquiryId)

class Admission(models.Model):
    admission_no = models.CharField(max_length=50,unique=True)
    enquiryid = models.CharField(max_length=50)
    coursefees = models.IntegerField()
    batchcode = models.ForeignKey(Batch, on_delete=models.CASCADE)
    date = models.DateField(default=date.today())
    def __str__(self):
        return self.admission_no

class Payment(models.Model):
    admission_no = models.CharField(max_length=50)
    amount = models.IntegerField()
    payment_date = models.DateField(default=date.today())
    enquiryid = models.CharField(max_length=50)
    def __str__(self):
        return self.amount

class EnquiryThree(models.Model):
    enquiryId = models.CharField(max_length=50)
    student_name = models.CharField(max_length=100)
    address = models.TextField()
    qualification = models.CharField(max_length=50)
    collegename = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    contact = models.IntegerField()
    email = models.EmailField(unique=True)
    enquirydate = models.DateField(default=date.today())
    followup_date = models.DateField()
     
    def __str__(self):
        return str(self.enquiryId)