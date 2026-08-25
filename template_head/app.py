from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright




def create_head_image(data)-> str:
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('./template_head/template.html')

    template_renderizado = template.render(data)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(template_renderizado)
        
        page.screenshot(path='./template_head/head_image.png',full_page=True)
        
   
        browser.close()
    return './template_head/head_image.png'