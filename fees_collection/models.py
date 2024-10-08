from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Student(models.Model):
    COURSE_CHOICES = [
        ('Mahade Ashraf', 'Mahade Ashraf'),
        ('معہد علیم', 'معہد علیم'),
        ('معہد ابرار', 'معہد ابرار'),
        ('معہد قاسم', 'معہد قاسم'),
        ('حفظ', 'حفظ'),
        ('ناظرہ', 'ناظرہ'),
    ]

    BRANCH_CHOICES = [
        ('Khaja Bagh', 'Khaja Bagh'),
        ('Akber Bagh', 'Akber Bagh'),
        ('Ghatkesar', 'Ghatkesar'),
        ('Bandlaguda', 'Bandlaguda'),
    ]

    STUDENT_TYPE_CHOICES = [
        ('Day Scholar', 'Day Scholar'),
        ('Boarder', 'Boarder'),
    ]

    SECTION_CHOICES = [
        ('INTER - I', 'INTER - I'),
        ('INTER - II', 'INTER - II'),
        ('B.COM - I', 'B.COM - I'),
        ('B.COM - II', 'B.COM - II'),
        ('B.COM - III', 'B.COM - III'),
        ('Awwal (Alif)', 'اول (الف)'),
        ('Awwal (Baa)', 'اول (ب)'),
        ('Awwal (Jeem)', 'اول (ج)'),
        ('Duwwam (Alif)', 'دوم (الف)'),
        ('Duwwam (Baa)', 'دوم (ب)'),
        ('Suwwam (Alif)', 'سوم (الف)'),
        ('Suwwam (Baa)', 'سوم (ب)'),
        ('Suwwam (Jeem)', 'سوم (ج)'),
        ('Chahrum (Alif)', 'چهارم (الف)'),
        ('Chahrum (Baa)', 'چهارم (ب)'),
        ('Panjum', 'پنجم'),
        ('Mouqoof Alai', 'موقوف علیہ'),
        ('Daur-e-Hadees', 'دورہ حدیث'),
        ('Edadiya School (Alif)', 'ادادیہ اسکول (الف)'),
        ('Edadiya School (Baa)', 'ادادیہ اسکول (ب)'),
        ('Awwal School (Alif)', 'اول اسکول (الف)'),
        ('Awwal School (Baa)', 'اول اسکول (ب)'),
        ('Duwwam School (Alif)', 'دوم اسکول (الف)'),
        ('Duwwam School (Baa)', 'دوم اسکول (ب)'),
        ('Suwwam', 'سوم'),
        ('Chahrum', 'چهارم'),
        ('Hifz-Alif', 'Hifz-Alif'),
        ('Hifz-Baa', 'Hifz-Baa'),
        ('Hifz-Jeem', 'Hifz-Jeem'),
        ('Hifz-Daal', 'Hifz-Daal'),
        ('Hifz-Zaa', 'Hifz-Zaa'),
        ('Hifz-Haa', 'Hifz-Haa'),
        ('Hifz-Haah', 'Hifz-Haah'),
        ('Hifz-Waav', 'Hifz-Waav'),
        ('Nazira-Alif', 'Nazira-Alif'),
        ('Nazira-Baa', 'Nazira-Baa'),
        ('Nazira-Jeem', 'Nazira-Jeem'),
        ('Nazira-Daal', 'Nazira-Daal'),
    ]

    admission_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    branch = models.CharField(max_length=100, choices=BRANCH_CHOICES)
    section = models.CharField(max_length=100, choices=SECTION_CHOICES, null=True, blank=True)
    monthly_fees = models.DecimalField(max_digits=10, decimal_places=2)
    student_type = models.CharField(max_length=20, choices=STUDENT_TYPE_CHOICES, default='Boarder')

    @property
    def total_fees(self):
        return self.monthly_fees * 12

    def __str__(self):
        return f'{self.name} ({self.admission_number})'


class Payment(models.Model):
    RECEIPT_TYPE_CHOICES = [
        ('fee', 'Fee'),
        ('donation', 'Donation'),
        ('other', 'Other'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('online', 'Online'),
    ]

    receipt_no = models.CharField(max_length=20, null=False, blank=False, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipt_type = models.CharField(max_length=15, choices=RECEIPT_TYPE_CHOICES, default='fee')
    name = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES, default='cash')
    organization = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=9, null=True, blank=True)

    class Meta:
        unique_together = ('receipt_no',)

    def __str__(self):
        return f'Receipt No: {self.receipt_no}'


 
