from django.db import models

# Create your models here.
class UserModel(models.Model):
    user_name = models.CharField(max_length=10,verbose_name='用户名')
    password = models.CharField(max_length=21,verbose_name='密码')
    tel = models.CharField(max_length=11,verbose_name='手机号')
    birthday = models.DateField(verbose_name='出生日期')   # 日期
    class Meta:
        db_table = 'users_table'
        verbose_name_plural = '用户表'
    def __str__(self):
        return self.user_name

class TeacherModel(models.Model):
    tea_name = models.CharField(max_length=30,verbose_name='老师姓名')
    tea_age = models.IntegerField(verbose_name='老师年龄')
    tea_project = models.CharField(max_length=40,verbose_name='老师专业')
    class Meta:
        db_table = 'tea_table'
        verbose_name_plural = '老师表'
class StudentModel(models.Model):
    stu_name = models.CharField(max_length=30,verbose_name='学生姓名')
    stu_age = models.IntegerField(verbose_name='学生年龄')
    teacher = models.ForeignKey(to=TeacherModel,on_delete=models.SET_NULL,verbose_name='老师',blank=True,null=True)