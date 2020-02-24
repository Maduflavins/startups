from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    body = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='image/')
    votes_total = models.ImageField(default=1)
    founder = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e &Y")
