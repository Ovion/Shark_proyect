import pandas as pd
import numpy as np
import re

def clean_last_ws (serie):
    return serie.replace("\s$", "")

def clean_first_ws (serie):
    return serie.replace("^\s", "")

def clean_mult_ws (serie):
    return serie.replace("\s+", " ")

def clean_weird_ch (serie):
    return serie.replace("[\[\]\,\"\'\\\.\-\?\<\>\*\&\;\+\(\)]", "")

def clean_num (serie):
    return serie.replace("[\d]", "")

def clean_1to2_ch (serie):
    aux = serie.replace("\s\w{1,2}\s", " ")
    aux1 = aux.replace("\s\w{1,2}\s", " ")
    aux2 = aux1.replace("\s\w{1,2}\s", " ")
    return aux2.replace("\s\w{1,2}\s", " ")
    
def shark_sp (serie):
    return serie.replace(r'(?!\w+\sshark)\b([\S\s]+?)(\b|$)', lambda x: (x.end() - x.start())*'') 

'''
df_sp = df_raw
df_sp.loc[(df_sp.Species == ''), 'Species'] = np.nan

df_sp.Species.fillna('shark', inplace = True)
df_sp.Species = df_sp.Species.str.lower()

df_sp1 = df_sp
df_sp1.Species = df_sp1.Species.str.findall("\w+\sshark")

lst_cc_sp = []
for e in df_sp1.Species:
    if e == []:
        lst_cc_sp.append("undef. shark")
    else:
        lst_cc_sp.append(e[0])

df_sp1["Shark_sp"] = lst_cc_sp
df_sp1.Shark_sp.value_counts()

df_sp1.loc[(df_sp1.Shark_sp == 'to shark')|
           (df_sp1.Shark_sp == 'small shark')|
           (df_sp1.Shark_sp == 'm shark')|
           (df_sp1.Shark_sp == 'involve shark')|
           (df_sp1.Shark_sp == 'kg shark')|
           (df_sp1.Shark_sp =='lb shark'), 'Shark_sp'] = "undef. shark"

df_sp1.Shark_sp.value_counts()
'''

    