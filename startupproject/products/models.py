from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    founder = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e &Y")


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    timestamp = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return '{}-{}'.format(self.product, str(self.user.username))


# class Product(models.Model):
#     title = models.CharField(max_length=255)
#     pub_date = models.DateTimeField()
#     body = models.TextField()
#     url = models.TextField()
#     image = models.ImageField(upload_to='images/')
#     icon = models.ImageField(upload_to='images/')
#     votes_total = models.IntegerField(default=1)
#     hunter = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

#     def summary(self):
#         return self.body[:100]

#     def pub_date_pretty(self):
#         return self.pub_date.strftime('%b %e %Y')