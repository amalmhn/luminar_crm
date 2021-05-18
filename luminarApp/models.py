from datetime import date

from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50,unique=True)
    course_duration = models.CharField(max_length=50)
    def __str__(self):
        return self.course_name

class BatchStatus(models.Model):
    choice = models.CharField(max_length=120)
    def __str__(self):
        return self.choice

class BatchModelNew(models.Model):
    batch_code = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch_date = models.DateField(default=date.today())
    course_fees = models.CharField(max_length=50)
    batch_status = models.ForeignKey(BatchStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.batch_code

class Batch(models.Model):
    batch_code = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    batch_date = models.DateField(default=date.today())
    course_fees = models.CharField(max_length=50)
    batch_status = models.ForeignKey(BatchStatus,on_delete=models.CASCADE)
    def __str__(self):
        return self.batch_code

class Enquiry(models.Model):
    enquiryId = models.CharField(primary_key=True, editable=False , max_length=150)
    student_name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
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





class ChoiceModel(models.Model):
    action = models.CharField(max_length=150)
    def __str__(self):
        return str(self.action)

class EnquiryThree(models.Model):
    enquiryId = models.CharField(max_length=50)
    student_name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    qualification = models.CharField(max_length=50)
    collegename = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    contact = models.IntegerField()
    email = models.EmailField(unique=True)
    enquirydate = models.DateField(default=date.today())
    followup_date = models.DateField()
    choice = models.ForeignKey(ChoiceModel,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.enquiryId)

class Admissions(models.Model):
    admission_no = models.CharField(max_length=50,unique=True)
    enquiryid = models.ForeignKey(EnquiryThree, on_delete=models.CASCADE)
    coursefees = models.IntegerField()
    batchcode = models.ForeignKey(Batch, on_delete=models.CASCADE)
    date = models.DateField(default=date.today())
    def __str__(self):
        return self.admission_no

class AdmissionNewModel(models.Model):
    admission_no = models.CharField(max_length=50,unique=True)
    enquiryid = models.ForeignKey(EnquiryThree, on_delete=models.CASCADE)
    coursefees = models.IntegerField()
    batchcode = models.ForeignKey(Batch, on_delete=models.CASCADE)
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.admission_no

class PaymentNewModel(models.Model):
    admission_no = models.ForeignKey(AdmissionNewModel, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_date = models.DateField(default=date.today())
    enquiryid = models.ForeignKey(EnquiryThree,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount)

class Payment(models.Model):
    admission_no = models.ForeignKey(AdmissionNewModel,on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_date = models.DateField(default=date.today())
    enquiryid = models.CharField(max_length=50)
    def __str__(self):
        return self.amount

class EmployeeModel(models.Model):
    employee_id = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    salary = models.CharField(max_length=100)

    def __str__(self):
        return str(self.employee_id)

class StudentModel(models.Model):
    student_id = models.CharField(max_length=50)
    student_name = models.CharField(max_length=150)
    course = models.CharField(max_length=150)
    total_fees = models.CharField(max_length=100)

    def __str__(self):
        return str(self.student_id)