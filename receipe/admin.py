from django.contrib import admin
from receipe.models import *
from django.db.models import Sum
admin.site.register(receipe)
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Subject)
class marksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks' ]
admin.site.register(marks, marksAdmin)
class hay_rankAdmin(admin.ModelAdmin):
    list_display = ['student', 'rank', 'date_of_creation','total_marks']
    ordering = ['rank']
    def total_marks(self, obj):
        student_marks = marks.objects.filter(student = obj.student)
        markse = student_marks.aggregate(marks = Sum('marks'))

        return markse['marks']
    
admin.site.register(hay_rank, hay_rankAdmin)




# Register your models here.
