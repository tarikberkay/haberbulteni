from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    description = models.TextField(blank=True)


    def __str__(self):
        return f"{self.name}____ {self.surname}"

class Article(models.Model):
    author = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    text = models.TextField()
    city = models.CharField(max_length=120)
    published_date = models.DateField()
    active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)  # süre değişmez 
    updated_date = models.DateTimeField(auto_now=True)  #süre değişir
    
    
    def __str__(self):
        return f"{self.author}   {self.title}"
