from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright




def create_head_image(data)-> str:
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('./template_head/template.html')

    template_renderizado = template.render(data)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={"width": 1200, "height": 800},  # ajuste ao tamanho real do seu template
            device_scale_factor=3,  # 2 ou 3 = qualidade "retina"
        )
        page = context.new_page()
        page.set_content(template_renderizado)
        
        page.screenshot(path='./template_head/head_image.png',full_page=True)
        
   
        browser.close()
    return './template_head/head_image.png'