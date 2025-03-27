# Recomanador general de vins

## Descripció
El Recomanador general de vins és una aplicació que ajuda els usuaris a trobar vins segons el seu perfil preguntant la mínima informació possible. Utilitzant tècniques de filtratge basat en contingut, coneixement expert i una base de dades de vins, l'aplicació pot suggerir vins que s'ajustin als gustos i criteris específics dels usuaris amb el menor nombre de preguntes.

Podeu accedir al recomanador utilitzant aquest enllaç: https://recomendador-general.onrender.com/

## Instal·lació local

### Requisits
- Python 3.8+

### Passos
#### 1. Clona el repositori:
```bash
git clone https://github.com/pjcopadoCS/recomendador_general
cd api_recomanador
```

#### 2. Crea un entorn virtual:
```bash
python -m venv venv
.\venv\Scripts\activate 
```

#### 3. Instal·la les dependències:
```bash
pip install -r requirements.txt
```

## Execució local
### 1. Executa l'aplicació:
```bash
py ./app.py
```

### 2. Obre el navegador i ves a http://localhost:5000.


## Autors
- Angela Nebot (angela@cs.upc.edu)
- Pedro Jesús Copado (pedro.jesus.copado@upc.edu, pcopado@cs.upc.edu)

## Informació addicional
#### Actualitzar les llibreries ja instalades
```bash
pip install --upgrade -r requirements.txt
```

#### Actualizar el fitxer de depèndencies amb les llibreries instalades
```bash
pip freeze > requirements.txt
```