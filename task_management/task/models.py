from django.db import models
from category.models import TaskCategory

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(TaskCategory, related_name='tasks')

    def __str__(self):
        return self.taskTitle
