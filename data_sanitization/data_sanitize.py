import pandas as pd

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

    json = df.to_dict(orient='records')

    return json

def sanitize_credito(filename):

    df = pd.read_csv(filename, encoding='utf-8')
    #Converte nomes do csv p/ o formatdo da API
    df = df.rename(columns={'amount': 'value', 'title': 'description'})

    #filtra apenas os valores positivos
    df = df[df['value'] > 0].copy()

    json = df.to_dict(orient='records')

    return json
