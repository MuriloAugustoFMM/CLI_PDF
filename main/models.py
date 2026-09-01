from django.db import models
from django.utils import timezone

class Checklist(models.Model):
    STATUS_OPTIONS =[
        ('EM ANDAMENTO','Em andamento'),
        ('CONCLUIDO','Concluido'),
        ('CANCELADO','Cancelado')
    ]
    TYPE_OPTIONS =[
        ('RELATORIO_FOTOGRAFICO','Relatorio fotografico'),
        ('RECEPCAO','Recepcao'),
        ('EXPEDICAO','Expedicao')
    ]
    title = models.CharField(max_length=40,editable=False,blank=True,unique=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=40, choices=STATUS_OPTIONS)
    type = models.CharField(max_length=50,choices=TYPE_OPTIONS)
    
    
    def save(self,*args, **kwargs):
        if not self.title:
            data_str = timezone.now().strftime("%d-%m-%Y--%H:%M:%S")
            
            self.title = f'{self.type}-SEMID-{data_str}'
            
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title
    

class Item(models.Model):
    question = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.question

class ItemChecklist(models.Model):
    item = models.ForeignKey(to=Item,on_delete=models.CASCADE)
    checklist = models.ForeignKey(to=Checklist,on_delete=models.CASCADE)
    optional_image = models.BooleanField(default=False)
    
    

class ImagensChecklist(models.Model):
    checklist = models.ForeignKey(to=Checklist,on_delete=models.CASCADE,blank=True, null=True)
    item = models.ForeignKey(to=Item,on_delete=models.CASCADE, blank=True,null=True)
    image = models.ImageField()


