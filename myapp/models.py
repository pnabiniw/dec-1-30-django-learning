from django.db import models


class ClassRoom(models.Model):
    name = models.CharField(max_length=10)


class Student(models.Model):  # class name later becomes the table name in the database. appname_classname
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="classroom_students",
                                  null=True, blank=True)


class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14)
    roll_no = models.IntegerField()
    bio = models.TextField(max_length=500)
    profile_picture = models.FileField(null=True, blank=True, upload_to="profile_pictures")


# Student.objects.create(name="Jon", age=30, email="kdns@nds.com", address="KTM")
# # INSERT INTO Student (NAME, EMAIL) VALUES ("fnd", )
#
#
# Student.objects.all()
# # Select * from student
