from django.shortcuts import render, redirect
from .forms import RelatorioFotografico
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):

    return(render(
        request,
        'global/index.html'
    ))

def criar_formulario(request):
    form : RelatorioFotografico
    
    if request.method == 'POST':
        
        form = RelatorioFotografico(request.POST,request.FILES)
        
        if form.is_valid():
                
            print(form.cleaned_data)
            return render(request, 'exibir_rel.html', {'dados': form.cleaned_data})

        print(form.errors)
    else: 
        
        form = RelatorioFotografico()
        
            
                
    return render(
            request,
            'relatorio-fotografico.html',
            {'form' : form}
    )
        
        
def visualizar_relatorio(request):
        
    return render(
        request,
        'exibir_rel.html',
        {'form':request.session['dados_formulario']}
    )