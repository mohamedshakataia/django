from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


# Create your models here.

TYPE_POST=(
    ('DRAFT','DRAFT'),
    ('PUBLISTED','PUBLISTED')

)

class Post(models.Model):
    title=models.CharField(max_length=30)
    contant=models.TextField(max_length=3000 ,null=True ,blank=True)
    active=models.BooleanField(default=True)
    Email=models.EmailField()
    create_at=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='posts')
    type=models.CharField(max_length=20,choices=TYPE_POST ,default='DRAFT')
    
    class Meta:
        ordering = ('title',)
        verbose_name = ('Post')
        verbose_name_plural = ('Allposts')

      
    
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("blog:detail",kwargs={"post_id":self.id})

    def editposts(self):
        return reverse("blog:edit",kwargs={"post_id":self.id})

    def deletesposts(self):
        return reverse("blog:deletepost",kwargs={"post_id":self.id})



        
