from django.db import models

# Create your models here.
# class student_data(models.Model):
    
#     std_no = models.CharField(max_length=100,primary_key=True)
#     std_name = models.CharField(max_length=100,unique=True)
#     sex = models.CharField(max_length=100)
#     age = models.IntegerField()
#     dept = models.CharField(max_length=100)
    

#     class Meta:
#         db_table = '學生基本資料'

# class student_score(models.Model):
#     score = models.IntegerField()
#     score_std = models.ForeignKey('student_data',on_delete=models.CASCADE,db_column='std_no',related_name='scores')
#     score_sub = models.ForeignKey('student_subject',on_delete=models.CASCADE,db_column='sub_no')
#     class Meta:
#         db_table = '學生成績資料'

# class student_subject(models.Model):
#     subject = models.CharField(max_length=100,unique=True)
#     sub_no = models.CharField(max_length=100,primary_key=True)

#     class Meta:
#         db_table = '學科資料'

# class class_name(models.Model):
#     class_name = models.CharField(max_length=100,db_column='class')
#     class_th = models.ForeignKey('teacher_name',on_delete=models.CASCADE,db_column='th_no',null=True)
#     class_sub = models.ForeignKey('student_subject',on_delete=models.CASCADE,db_column='sub_no',null=True)

#     class Meta:
#         db_table = '教室資料'

# class teacher_name(models.Model):
#     th_no = models.CharField(max_length=100,primary_key=True)
#     th_name = models.CharField(max_length=100,unique=True)
#     age = models.CharField(max_length=100)
#     salary = models.DecimalField(decimal_places=2,max_digits=10)
    
#     class Meta:
#         db_table = '教師資料'


class Captcha(models.Model):

    email = models.EmailField(unique=True)
    captcha = models.CharField(max_length=10)
    creat_time = models.DateTimeField(auto_now=True)
    


class Userdata(models.Model):

    name = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_time = models.DateTimeField(auto_now_add=True)
    
    

class Blog(models.Model):

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100,unique=True)
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    