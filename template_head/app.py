from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import datetime

dados_mockados = {
    'equipamento' : 'PERERÃO',
    'patrimonio' : 'EXEMPLO_PATRIMONIO',
    'data' : datetime.date.strftime(datetime.datetime.now(),"%d/%m/%Y, %H:%M:%S"),
    'operador': 'EXEMPLO_OPERADOR',
    'mecanico' : 'mecanico_exemplo'
}

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

template_renderizado = template.render(dados_mockados)

HTML(string=template_renderizado,base_url='.').write_pdf('relatorio_final.pdf')