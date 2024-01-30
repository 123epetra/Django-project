from faker import Faker
fake = Faker()
import random
from .models import *
from django.db.models import Q,  Sum

def marks_gen(n) -> None:
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subject_obj = Subject.objects.all()
            for subject in subject_obj:
                marks.objects.create(
                    student = student,
                    subject = subject,
                    marks = random.randint(0, 100)

                )
                
                
    except Exception as e:
        print(e)
    




def seed_db(n=10) -> None:
    try:
    
        
        for _ in range(n):
            obj_depart = Department.objects.all()
            index = random.randint(0, len(obj_depart)-1)
            abc= obj_depart[index]
            student_id = f'STU-0{random.randint(100,900)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 40)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id = student_id)

            student_obj = Student.objects.create(
                abc=abc,
                student_id = student_id_obj ,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age ,
                student_address = student_address 
            )
    except Exception as e:
        print(e)

def rank_generator():
    ranks= Student.objects.annotate(stud_marks = Sum('student_marks__marks')).order_by('-stud_marks','student_age')
    
    i=1
    for rank in ranks:
        hay_rank.objects.create(
            student = rank,
            rank = i
        )
        i=i+1

