from django.db import models


class University(models.Model):
    """
    University table
    """

    name = models.CharField(max_length=50, default="")
    cnpj = models.CharField(max_length=20, default="", unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Major(models.Model):
    """
    Major table - undergraduation course
    e.g., Computer Engeneering, Economics, Law, etc
    """

    name = models.CharField(max_length=50, default="", unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.name is not None:
            self.name = self.name.lower()
        super().save(*args, **kwargs)
