from django.contrib import admin
from .models import Person, Position, Student, Class, Task, Mark, Curriculum, Discipline


class PositionAdmin(admin.ModelAdmin):
    list_display = ('positionID', 'positionName',)
    list_display_links = ('positionID',)
    search_fields = ('positionName',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('personID', 'surname', 'name', 'patronymic', 'positionID',)
    list_display_links = ('personID',)
    search_fields = ('surname', 'name', 'surname', 'patronymic',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentID', 'personID', 'classID',)
    list_display_links = ('studentID',)
    search_fields = ('personID', 'classID',)


class ClassAdmin(admin.ModelAdmin):
    list_display = ('classID', 'className',)
    list_display_links = ('classID',)
    search_fields = ('className',)


class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('disciplineID', 'nameDiscipline',)
    list_display_links = ('disciplineID',)
    search_fields = ('nameDiscipline',)


class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('curriculumID', 'personID', 'classID', 'disciplineID')
    list_display_links = ('curriculumID',)
    search_fields = ('classID', 'disciplineID')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('taskID', 'taskName', 'comments', 'startDateTime', 'endDateTime')
    list_display_links = ('taskID',)
    search_fields = ('taskName', 'startDateTime')


class MarkAdmin(admin.ModelAdmin):
    list_display = ('markID', 'score', 'studentID', 'taskID',)
    list_display_links = ('markID',)
    search_fields = ('studentID',)


admin.site.register(Position, PositionAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Mark, MarkAdmin)


admin.site.site_header = 'Электронный дневник'
admin.site.site_title = 'Электронный дневник'
