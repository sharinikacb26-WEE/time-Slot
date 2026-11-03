from django.db import models

class TimeSlot(models.Model):
    day = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject_name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    classroom = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name
