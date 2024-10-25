import pandas as pd

df = pd.read_excel('Products_Stock.xlsx')

def print_info():
    # Mostra un resum concís del DataFrame, incloent informació sobre índex, columnes, tipus de dades 
    # i memòria utilitzada.
    print(df.info()) 
    # Comprobar els tipus de dades de cada columna del DataFrame.
    print(df.dtypes) 
    # Mostra les primeres files del DataFrame per proporcionar una vista prèvia dels seus continguts.
    print(df.head())  
    # Proporciona estadístiques descriptives per a les columnes numèriques del DataFrame, com la mitjana, 
    # la desviació estàndard, el valor mínim, els quartils i el valor màxim.
    print(df.describe()) 

def divide_alcohol(value):
    if value > 1:
        return value / 100
    else:
        return value

def remove_spaces(column):
    df[column] = df[column].str.strip()

if __name__ == "__main__":
    print_info()
    df = df.drop_duplicates()
    # Aplicar la funció a la columna 'Alcohol'
    df['Alcohol'] = df['Alcohol'].apply(divide_alcohol) 
    # remove_spaces('Type')
    # df.to_excel("Products_Stock.xlsx", index=False)