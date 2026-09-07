from django import forms

class RelatorioFotografico(forms.Form):
    
    authors_name = forms.CharField(max_length=50, required=True,)
    
    machine = forms.CharField(max_length=100,required=True)
    
    machine_id = forms.CharField(max_length=40, required=True)
    machine_id_photo = forms.ImageField(required=True)
    
    
    machine_metric = forms.CharField(max_length=40,required=True)
    machine_metric_photo = forms.ImageField(required=True)    
    
    
    