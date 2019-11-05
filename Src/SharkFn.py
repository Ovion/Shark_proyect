import pandas as pd
import numpy as np
import re


def clean_last_ws (serie):
    # Esta función limpia el último espacio de una cadena de str.
    return serie.replace("\s$", "")

def clean_first_ws (serie):
    # Esta función limpia el primer espacio de una cadena de str.
    return serie.replace("^\s", "")

def clean_mult_ws (serie):
    # Esta función en caso de haber dos espacios seguidos limpia uno de ellos.
    return serie.replace("\s+", " ")

def clean_weird_ch (serie):
    # Esta función limpia de caracteres raros que puedan impedir una RegEx para muchos datos
    return serie.replace("[\[\]\,\"\'\\\.\-\?\<\>\*\&\;\+\(\)]", "")

def clean_num (serie):
    # Esta función elimina dígitos almacenados donde no deberían estar.
    return serie.replace("[\d]", "")

def clean_1to2_ch (serie):
    #Esta función elimina palabras de 2 o menos caracteres.
    aux = serie.replace("\s\w{1,2}\s", " ")
    aux1 = aux.replace("\s\w{1,2}\s", " ")
    aux2 = aux1.replace("\s\w{1,2}\s", " ")
    return aux2.replace("\s\w{1,2}\s", " ")
    
'''
# Code 1
sharkUSA = sharky.loc[(shark['Country'] == 'USA')]
sharkAUS = sharky.loc[(shark['Country'] == 'AUSTRALIA')]
sharkSA = sharky.loc[(shark['Country'] == 'SOUTH AFRICA')]
sharkPNG = sharky.loc[(shark['Country'] == 'PAPUA NEW GUINEA')]
sharkBRZ = sharky.loc[(shark['Country'] == 'BRAZIL')]
​
# Code 2 - Refactor
def generaFiltros(paises):
  filtosPaises = dict()
  for pais in paises:
    filtrosPaises[pais] = sharky.loc[(shark['Country'] == pais)]
  return filtrosPaises
​
paises = ['USA','AUSTRALIA','SOUTH AFRICA','PAPUA NEW GUINEA']
df = generaFiltros(paises)['USA']
'''