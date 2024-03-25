import re
from validate_docbr import CPF



  
def nome_valido (nome):
    return nome.isalpha()   
    
def cpf_valido (numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

def rg_valido (numero_do_rg):
    return len(numero_do_rg) == 9
    
def celular_valido(numero_celular):
    """Numero de celular deve seguir o padrao 98 9 1234-1234"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall (modelo, numero_celular)
    return resposta
