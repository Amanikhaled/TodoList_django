from django.db import models


# Create your models here.


class Todo(models.Model):
    # gradechoices = [('A+', '100'), ('B+', '85')]
    # grade = models.CharField(
    #     max_length = 2, choices = gradechoices, null = True, blank = True)
    name = models.CharField(max_length=150, null=True, blank=True)
    # description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    is_completed = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name


class TodoItems(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    createAt = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    Description = models.TextField(null=True, blank=True)
    todo = models.ForeignKey(Todo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def getdesc(self):
        return self.Description
