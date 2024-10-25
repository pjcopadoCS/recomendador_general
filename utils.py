import pandas as pd
import constants

def filtratge(df, atribut, valors):
    df_filrat = df[df[atribut].isin(valors)]
    return df_filrat


def categories(df, atribut):
    rang = []
    if atribut == 'Alcohol':
        rang = constants.rang_alcohol
    elif atribut == 'Price':
        rang = constants.rang_preu

    categories = []

    if (df[atribut] < rang[0]).any():
        categories.append('low')
        
    if ((df[atribut] >= rang[0]) & (df[atribut] <= rang[1])).any():
        categories.append('medium')

    if ((df[atribut] > rang[1]) & (df[atribut] < rang[2])).any():
        categories.append('high')

    if (df[atribut] >= rang[2]).any():
        categories.append('very_high')

    return categories


def filtratge_categories(df, atribut, valors):
    rang = []
    if atribut == 'Alcohol':
        rang = constants.rang_alcohol
    elif atribut == 'Price':
        rang = constants.rang_preu
    filtrats = []

    for valor in valors:
        if valor == "low":
            filtrats.append(df[df[atribut] < rang[0]])
        elif valor == "medium":
            filtrats.append(df[(df[atribut] >= rang[0]) & (df[atribut] <= rang[1])])
        elif valor == "high":
            filtrats.append(df[(df[atribut] > rang[1]) & (df[atribut] < rang[2])])
        elif valor == "very_high":
            filtrats.append(df[df[atribut] >= rang[2]])
    df_filtrat = pd.concat(filtrats).drop_duplicates().reset_index(drop=True)
    return df_filtrat