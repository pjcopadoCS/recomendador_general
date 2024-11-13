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
    'France',
    'Italy',
    'Spain',
    'USA',
    'Argentina',
    'Chile',
    'Australia',
    'South Africa',
    'Germany',
    'New Zealand',
]

paisos_emergents = [
    'Uruguay',
    'Brazil',
    'Mexico',
    'China',
    'India',
    'England',
    'Greece',
    'Georgia',
    'Lebanon',
    'South Africa',
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
    'Sweet',
    'Semi Sweet',
    'Semi Dry',
]

rang_alcohol = [8, 12, 14.5]

alcohol_dict = {
    'low': f'Less than {rang_alcohol[0]}%',
    'medium': f'Between {rang_alcohol[0]}% and {rang_alcohol[1]}%',
    'high': f'Between {rang_alcohol[1]}% and {rang_alcohol[2]}%',
    'very_high': f'More than {rang_alcohol[2]}%',
}

rang_preu = [20, 50, 100]

preu_dict = {
    'low': f'Less than {rang_preu[0]}€',
    'medium': f'Between {rang_preu[0]}€ and {rang_preu[1]}€',
    'high': f'Between {rang_preu[1]}€ and {rang_preu[2]}€',
    'very_high': f'More than {rang_preu[2]}€',
}