from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet
User = get_user_model()


class receipe(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, blank = True)

    receipe_name = models.CharField(max_length = 100)
    receipe_description = models.CharField(max_length = 500)
    receipe_image =  models.ImageField(upload_to= "receipe_image")
    watches_count = models.IntegerField(default = 1)
    def __str__(self) -> str:
        return self.receipe_name
# class testing(models.Model):
#     test_name= 'supreme'
#     relate_receipe = models.ForeignKey(receipe, related_name='depart', on_delete = models.CASCADE)

class Department(models.Model):
    department = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.department
    class Meta:
        ordering = ['department']

class Subject(models.Model):
    subject_name = models.CharField(max_length = 100)
    def __str__(self):
        return self.subject_name


class StudentID(models.Model):
    student_id = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.student_id
    
class studentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete = False)
    
class Student(models.Model):
    abc = models.ForeignKey(Department, related_name='depart', on_delete = models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name= 'studentid', on_delete = models.CASCADE)
    student_name = models.CharField(max_length = 100)
    student_email= models.EmailField(unique= True)
    student_age = models.IntegerField(default = 18)
    student_address = models.TextField()
    objects = studentManager()
    admin_objects = models.Manager()

    is_delete = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.student_name
    class Meta:
        
        verbose_name = 'student' # this is displayed in admin pannel as name of this model (Students) since admin makes first letter capital and adds s for fun
    
class marks(models.Model):
    student = models.ForeignKey(Student, related_name = 'student_marks', on_delete= models.CASCADE)
    subject = models.ForeignKey(Subject, related_name = 'subject_marks', on_delete = models.CASCADE)
    marks = models.IntegerField(default = 0)
    def __str__(self) -> str:
        return f'{self.student.student_name} {self.subject.subject_name}'

    class Meta():
        unique_together = ['student', 'subject']

class hay_rank(models.Model):
    student = models.ForeignKey(Student, related_name = 'student_rank', on_delete = models.CASCADE)
    rank = models.IntegerField(default = 0)
    date_of_creation  = models.DateField(auto_now_add = True)
    def __str__(self) -> str:
        return self.student.student_name

    class Meta():
        unique_together = ['rank', 'date_of_creation']






# class Ranks(models.Model):
#  student = models.ForeignKey(Student, related_name = 'student_det_R', on_delete= models.CASCADE)
#  sudent_rank = models.IntegerField()
#  date_of_creation = models.DateField()
 


 

# Create your models here.
