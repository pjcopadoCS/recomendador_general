paisos_dict = {
    'Spain': 'Espanya',
    'France': 'França',
    'Portugal': 'Portugal',
    'Italy': 'Itàlia',
    'Germany': 'Alemanya',
    'USA': 'Estats Units',
    'New Zealand': 'Nova Zelanda',
    'Argentina': 'Argentina',
    'Chile': 'Xile',
    'South Africa': 'Sud-àfrica',
    'Uruguay': 'Uruguai',
    'Morocco': 'Marroc',
    'Brazil': 'Brasil',
    'Japan': 'Japó',
}

paisos_reconeguts = [
    'França',
    'Itàlia',
    'Espanya',
    'Estats Units',
    'Argentina',
    'Xile',
    'Austràlia',
    'Sud-àfrica',
    'Alemanya',
    'Nova Zelanda',
]

paisos_emergents = [
    'Uruguay',
    'Brasil',
    'Mèxic',
    'Xina',
    'Índia',
    'Anglaterra',
    'Grècia',
    'Geòrgia',
    'Líban',
    'Sud-àfrica',
]

varietats_nobles = [
    'Cabernet Sauvignon',
    'Merlot',
    'Pinot Noir',
    'Syrah',
    'Chardonnay',
    'Sauvignon Blanc',
    'Riesling',
    'Tempranillo',
    'Nebbiolo',
    'Sangiovese',
]

varietats_exotiques = [
    'Assyrtiko',
    'Xinomavro',
    'Torrontés',
    'Saperavi',
    'Aglianico',
    'Grüner Veltliner',
    'Carmenère',
    'Verdicchio',
    'Picpoul',
    'Blaufränkisch',
    'Furmint',
    'Mencia',
    'Touriga Nacional',
    'Schiava',
    'Bobal',
]

gustos_dict = {
    'Dry': 'Sec',
    'Semi Dry': 'Semi Sec',
    'Brut': 'Brut',
    'Extra Brut': 'Extra Brut',
    'Fortified Wine': 'Vi Fortificat',
    'Sweet': 'Dolç',
    'Semi Sweet': 'Semi Dolç',
}

gustos_ocasional = [
    'Dolç',
    'Semi Dolç',
    'Semi Sec',
]

rang_alcohol = [8, 12, 14.5]

alcohol_dict = {
    'low': f'Menys de {rang_alcohol[0]}%',
    'medium': f'Entre {rang_alcohol[0]}% i {rang_alcohol[1]}%',
    'high': f'Entre {rang_alcohol[1]}% i {rang_alcohol[2]}%',
    'very_high': f'Més de {rang_alcohol[2]}%',
}

rang_preu = [20, 50, 100]

preu_dict = {
    'low': f'Menys de {rang_preu[0]}€',
    'medium': f'Entre {rang_preu[0]}€ i {rang_preu[1]}€',
    'high': f'Entre {rang_preu[1]}€ i {rang_preu[2]}€',
    'very_high': f'Més de {rang_preu[2]}€',
}