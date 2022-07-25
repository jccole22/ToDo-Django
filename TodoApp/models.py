from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


    #This is needed for /admin stuff
    #will print item name and not "List object 1" "List object 2" etc..
    def __str__(self):
        return self.item
