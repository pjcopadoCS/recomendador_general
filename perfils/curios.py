from flask import Blueprint, redirect, render_template, session, url_for, request
import pandas as pd
import constants

from utils import categories, filtratge, filtratge_categories

curios_bp = Blueprint('curios', __name__)

df, df2, df3, df4, df5, df6, df7 = [None]*7
RECOMANACIO = 'curios.recomanacio'

@curios_bp.route('/curios_pregunta1', methods = ['GET', 'POST'])
def pregunta_1():

    global df, df2
    error = False

    if request.method == 'GET':
        df = pd.read_excel('wines_dataset.xlsx')
        session['data'] = df.to_dict(orient='records')

    elif request.method == 'POST':

        if request.form.get("Skip"):
            df2 = df
            return redirect(url_for('curios.pregunta_2'))

        if 'Tipus' not in request.form:
            error = True
        else:

            selected_items = request.form.getlist('Tipus')
            df2 = filtratge(df, 'Type', selected_items)

            if request.form.get("Next"):

                return redirect(url_for('curios.pregunta_2'))

            elif request.form.get('Recomana'):

                session['last'] = '1'
                session['data'] = df2.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))  
           
    return render_template('/curios/pregunta1.html', error = error)


@curios_bp.route('/curios_pregunta2', methods = ['GET', 'POST'])
def pregunta_2():

    global df2, df3

    error = False
    categories_alchol = categories(df2, 'Alcohol')
    dict_alcohol = [(categoria, constants.alcohol_dict.get(categoria)) for categoria in categories_alchol]

    if request.method == 'GET':

        if len(dict_alcohol) == 1:
            df3 = filtratge_categories(df2, 'Alcohol', dict_alcohol[0])
            return redirect(url_for('curios.pregunta_3'))

    if request.method == 'POST':
        if request.form.get("Skip"):
            df3 = df2
            return redirect(url_for('curios.pregunta_3'))
        if 'Alcohol' not in request.form:
            error = True
        else: 
            selected_items = request.form.getlist('Alcohol')
            df3 = filtratge_categories(df2, 'Alcohol', selected_items)

            if request.form.get('Next'):
                return redirect(url_for('curios.pregunta_3'))
            elif request.form.get('Recomana'):
                session['last'] = '2'
                session['data'] = df3.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))
            
    return render_template('/curios/pregunta2.html', alcohol = dict_alcohol, error = error)


@curios_bp.route('/curios_pregunta3', methods = ['GET', 'POST'])
def pregunta_3():
    global df3, df4
    error = False
    paisos = df3['Country'].unique().tolist()
    dict_paisos = [(pais, constants.paisos_dict.get(pais, pais)) for pais in paisos]
    emergents = constants.paisos_emergents
    
    
    if request.method == 'GET':
        if len(dict_paisos) == 1:
            df3 = filtratge_categories(df2, 'Country', dict_paisos[0])
            return redirect(url_for('curios.pregunta_3'))

    if request.method == 'POST':
        if request.form.get("Skip"):
            df4 = df3
            return redirect(url_for('curios.pregunta_4'))
        if 'Pais' not in request.form:
            error = True
        else:        
            selected_items = request.form.getlist('Pais')
            df4 = filtratge(df3, 'Country', selected_items)
            
            if request.form.get('Next'):
                return redirect(url_for('curios.pregunta_4'))
            if request.form.get('Recomana'):
                session['last'] = '3'
                session['data'] = df4.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))
            
    return render_template('/curios/pregunta3.html', paisos = dict_paisos, emergents = emergents, error = error)


@curios_bp.route('/curios_pregunta4', methods = ['GET', 'POST'])
def pregunta_4():
    global df4, df5
    error = False
    regions = df4['Region'].unique().tolist()
    
    
    if request.method == 'GET':

        if len(regions) == 1:
            df5 = filtratge(df4, 'Region', regions)
            return redirect(url_for('curios.pregunta_5'))

    if request.method == 'POST':
        if request.form.get("Skip"):
            df5 = df4
            return redirect(url_for('curios.pregunta_5'))
        if 'Regio' not in request.form:
            error = True
        else:        
            selected_items = request.form.getlist('Regio')
            df5 = filtratge(df4, 'Region', selected_items)

            if request.form.get('Next'):
                return redirect(url_for('curios.pregunta_5'))
            if request.form.get('Recomana'):
                session['last'] = '4'
                session['data'] = df5.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))
            
    return render_template(
        '/curios/pregunta4.html', 
        regions = regions, 
        error = error,
    )
        

@curios_bp.route('/curios_pregunta5', methods = ['GET', 'POST'])
def pregunta_5():
    global df5, df6
    error = False
    tots_els_raims = df5['GrapeVariety'].str.split(',').explode()
    tots_els_raims = tots_els_raims.str.strip()
    raims = tots_els_raims.unique().tolist()
    exotiques = constants.varietats_exotiques
    
    if request.method == 'GET':

        if len(raims) == 1:
            df6 = filtratge(df5, 'GrapeVariety', raims)
            return redirect(url_for('curios.pregunta_6'))

    if request.method == 'POST':
        if request.form.get("Skip"):
            df6 = df5
            return redirect(url_for('curios.pregunta_6'))
        if 'Raim' not in request.form:
            error = True
        else:        
            selected_items = request.form.getlist('Raim')
            regex_pattern = '|'.join(selected_items)
            df6 = df5[df5['GrapeVariety'].str.contains(regex_pattern, case=False, na=False)]
            
            if request.form.get('Next'):
                return redirect(url_for('curios.pregunta_6'))
            if request.form.get('Recomana'):
                session['last'] = '5'
                session['data'] = df6.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))
    
    return render_template(
        '/curios/pregunta5.html', 
        raims = raims, 
        exotiques = exotiques, 
        error = error,
    )


@curios_bp.route('/curios_pregunta6', methods = ['GET', 'POST'])
def pregunta_6():
    global df6, df7
    tots_els_menjars = df6['FoodParing'].str.split(',').explode()
    tots_els_menjars = tots_els_menjars.str.strip()
    menjars = tots_els_menjars.unique().tolist()+['Altres']
    
    if request.method == 'GET':
        if len(menjars) == 1:
            if 'Altres' not in menjars:
                regex_pattern = '|'.join(menjars)
                df7 = df6[df6['FoodParing'].str.contains(regex_pattern, case=False, na=False)]
                session['data'] = df7.to_dict(orient='records')
            else:
                df7 = df6
                session['data'] = df7.to_dict(orient='records')
            return redirect(url_for(RECOMANACIO))
    
    if request.method == 'POST':
        session['last'] = '6'
        if 'Menjar' not in request.form:
            return redirect(url_for(RECOMANACIO))
        else:        
            selected_items = request.form.getlist('Menjar')
            if 'Altres' in selected_items:
                selected_items.remove('Altres')
                if len(selected_items) == 0:
                    selected_items = menjars
            regex_pattern = '|'.join(selected_items)
            df7 = df6[df6['FoodParing'].str.contains(regex_pattern, case=False, na=False)]
            
            session['data'] = df7.to_dict(orient='records')
            return redirect(url_for(RECOMANACIO))
    
    return render_template('/curios/pregunta6.html', menjars = menjars)
    

@curios_bp.route('/curios_recomancio')
def recomanacio():
    data = session.get('data', [])
    last = session.get('last')
    return render_template('/curios/recomanacio.html', data = data, last = last)