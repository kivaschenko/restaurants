from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=160, null=True)
    department = models.CharField(max_length=160, null=True)
    phone = models.CharField(max_length=20, null=True)
    
    class Meta:
        ordering = ['department', 'position']
    
    def __str__(self) -> str:
        return f'{self.position} {self.user.get_full_name()}'

    def __repr__(self) -> str:
        return f'<Employee(id={self.id} user={self.user}...)>'