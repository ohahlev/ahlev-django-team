from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class Member(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False)
    photo = models.ImageField(upload_to='member')
    photo_thumbnail = ImageSpecField(source='photo', 
        processors=[ResizeToFit(None, 200)],
        format='PNG',
        options={'quality': 100})
    position = models.CharField(max_length=32, blank=False)
    dribbble = models.CharField(max_length=128, blank=True, help_text='''
        <i class="fab fa-4x fa-dribbble" style='color:red'></i>
    ''')
    facebook = models.CharField(max_length=128, blank=True, help_text='''
        <i class="fab fa-4x fa-facebook" style='color:blue'></i>
    ''')
    github = models.CharField(max_length=128, blank=True, help_text='''
        <i class="fab fa-4x fa-github" style='color:magenta'></i>
    ''')
    linkedin = models.CharField(max_length=128, blank=True, help_text='''
        <i class="fab fa-4x fa-linkedin" style='color:green'></i>
    ''')
    pinterest = models.CharField(max_length=128, blank=True, help_text='''
        <i class="fab fa-4x fa-pinterest" style='color:orange'></i>
    ''')
    twitter = models.CharField(max_length=128, blank=True, help_text='''
        <i class="fab fa-4x fa-twitter" style='color:cyan'></i>
    ''')
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'member'

    def __str__(self):
        return self.name
