from django.db import models

select_branch = [('cse', 'Computer Science and Engineering'), ('ece', 'Electronics and Communication Engineering')]
select_subject = [('pfsd', 'Professional Software Development'), ('mswd', 'Mobile Software Development')]


class Student(models.Model):
    objects = None
    sid=models.IntegerField()
    name=models.CharField(max_length=30)
    branch = models.CharField(max_length=3, choices=select_branch)
    subject = models.CharField(max_length=4, choices=select_subject)

    def __str__(self):
        return f"Student ID: {self.sid}, Name:{self.name}, Branch: {self.branch}, Subject: {self.subject}"
