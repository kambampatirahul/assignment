from django.db import models


# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=50)
    st_id = models.CharField(max_length=10, primary_key=True)
    email = models.EmailField(unique=True, blank=True)
    catageory = models.CharField(max_length=10)

    # password = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.st_id, self.catageory)


class assignment(models.Model):
    te_id = models.CharField(max_length=10)
    stu = models.ForeignKey(student, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    questions = models.TextField()
    deadline = models.DateField()
    solution = models.TextField(default='NULL')
    marks = models.IntegerField(default=0, max_length=3)
    remarks = models.CharField(max_length=25, default='NULL')

    def save(self):
        super(assignment, self).save()

    def __str__(self):
        return self.title


