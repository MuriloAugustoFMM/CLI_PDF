def converter_digito(digito)-> int:

    try:
        digito_convertido = int(digito)
        return digito_convertido
    
    except Exception as e:
        
        print(e.__class__.__name__)
        return -1