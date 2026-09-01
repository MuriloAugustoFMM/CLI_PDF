from django.db import models

class Checklist(models.Model):
    STATUS_OPTIONS =[
        ''
    ]
    title = models.CharField(max_length=40)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_lenght=40)
    

class Item(models.Model):
    question = models.CharField(max_length=150)
    description = models.TextField(blank=True)

class ItemChecklist(models.Model):
    item_id = models.ForeignKey(to=Item,on_delete=models.CASCADE)
    checklist_id = models.ForeignKey(to=Checklist,on_delete=models.CASCADE)
    optional_image = models.BooleanField(default=False)

class ImagensChecklist(models.Model):
    fk_checklist = models.ForeignKey(to=Checklist,on_delete=models.CASCADE,blank=True)
    fk_item = models.ForeignKey(to=Item,on_delete=models.CASCADE)


