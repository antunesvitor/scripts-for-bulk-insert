import pandas as pd
import json
from data_sanitization.Groups import *

def sanitize_debito(filename):
    df = pd.read_csv(filename, encoding='utf-8')
    #Converte nomes do csv p/ o formatdo da API
    df = df.rename(columns={'Valor': 'value', 'Descrição': 'description', 'Data': 'date'})

    # converte formato da data de dd/MM/yyyy para yyyy-MM-dd
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')

    #drop column
    columns_to_convert = ['value', 'description', 'date']
    df = df[columns_to_convert]

    #reverter os valores negativos em positivos e vice-versa
    df['value'] = -df['value']

    #filtra apenas os valores positivos
    df = df[df['value'] > 0].copy()

    #Add the groupId column here
    df['groupId'] = df['description'].apply(get_group_id).astype('Int64')

    json_data = df.to_dict(orient='records')

    return json_data

def sanitize_credito(filename):

    df = pd.read_csv(filename, encoding='utf-8')
    #Converte nomes do csv p/ o formatdo da API
    df = df.rename(columns={'amount': 'value', 'title': 'description'})

    #filtra apenas os valores positivos
    df = df[df['value'] > 0].copy()

    #Add the groupId column here
    df['groupId'] = df['description'].apply(get_group_id).astype('Int64')

    json_data = df.to_dict(orient='records')
    
    return json_data

def get_group_id(description):
    description_lower = description.lower()
    
    # Check ALIMENTACAO
    for keyword in ALIMENTACAO_MATCHING_TYPE:
        if keyword.lower() in description_lower:
            return GROUP_ID_ALIMENTACAO
    
    # Check TRANSPORTE
    for keyword in TRANSPORTE_MATCHING_TYPE:
        if keyword.lower() in description_lower:
            return GROUP_ID_TRANSPORTE
    
    # Check ASSINATURAS
    for keyword in ASSINATURAS_MATCHING_TYPE:
        if keyword.lower() in description_lower:
            return GROUP_ID_ASSINATURAS
    
    # Default: return 0 or None if no match found
    return None