from django.db import models
import datetime

# Create your models here.
class Host(models.Model):
    # id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, default="null")
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    org = models.CharField(max_length=200)
    type_org = models.CharField(max_length=100, default="School")
    designation = models.CharField(max_length=150)
    phone = models.PositiveIntegerField()
    purpose = models.TextField()
    detail = models.TextField()
    theme = models.CharField(max_length=250)
    guidelines = models.TextField()
    elig_cri = models.TextField()
    last_sub = models.DateField(
        auto_now=False, auto_now_add=False, default=datetime.date.today
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.org

    class Meta:
        ordering = ["-date"]


class Participant(models.Model):
    # id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, default="null", blank=True)
    School_Name = models.CharField(max_length=50)
    School_Phone_no = models.CharField(max_length=150)
    School_Email_address = models.EmailField(max_length=100)
    School_Address = models.CharField(max_length=200)
    State = models.CharField(max_length=100)
    Student_Name = models.CharField(max_length=50)
    Contact_no = models.CharField(max_length=150)
    Email_address = models.EmailField(max_length=100)
    House_Address = models.CharField(max_length=200)
    Gender = models.CharField(max_length=100)
    Title_of_your_project = models.CharField(max_length=200)
    Question_or_Problem = models.CharField(max_length=100)
    Hypothesis_or_possible_solution = models.CharField(max_length=50)
    Materials_needed = models.CharField(max_length=150)
    Results = models.CharField(max_length=100)
    Image_of_Project = models.URLField()
    Link_of_your_project = models.URLField(max_length=200)
    host_id = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Student_Name

    class Meta:
        ordering = ["-date"]


class Contact(models.Model):
    # id = models.AutoField(primary_key=True)
    Full_Name = models.CharField(max_length=150)
    Email_Address = models.EmailField(max_length=100)
    Message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Full_Name

    class Meta:
        ordering = ["-date"]
