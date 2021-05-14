from django.db import models
from profiles.models import Mentor, Student


class Market(models.Model):
    """
    Market table - used to connect mentors to projects related to their markets
    """

    name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    mentors = models.ManyToManyField(Mentor, related_name="markets", blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name is not None:
            self.name = self.name.lower()

        super().save(*args, **kwargs)


class Project(models.Model):
    """
    Project table
    """

    project_categories_choices = [
        ("startup", "startup"),
        ("junior_enterprise", "junior enterprise"),
        ("academic", "academic project"),
        ("hobby", "hobby"),
    ]

    category = models.CharField(max_length=50, choices=project_categories_choices)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    students = models.ManyToManyField(Student, related_name="projects", blank=True)
    mentors = models.ManyToManyField(Mentor, related_name="projects", blank=True)
    markets = models.ManyToManyField(Market, related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def students_profile(self):
        return [student.profile for student in self.students.all()]

    @property
    def mentors_profile(self):
        return [mentor.profile for mentor in self.mentors.all()]
