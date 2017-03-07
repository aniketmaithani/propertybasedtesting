from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=10, blank=False, null=True)
    class_enrolled = models.IntegerField()
    preferred_subject = models.CharField(max_length=10, blank=False, null=True)
    marks_obtained = models.IntegerField()

    def __str__(self):
        return self.name
