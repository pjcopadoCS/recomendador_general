from flask import Blueprint, redirect, render_template, session, url_for, request
import pandas as pd
import constants

from utils import categories, filtratge, filtratge_categories

pragmatic_bp = Blueprint('pragmatic', __name__)

df, df2, df3, df4, df5 = [None]*5
RECOMANACIO = 'pragmatic.recomanacio'

@pragmatic_bp.route('/pragmatic_pregunta1', methods = ['GET', 'POST'])
def pregunta_1():
    global df, df2
    error = False
    if request.method == 'GET':
        df = pd.read_excel('wines_dataset.xlsx')
        session['data'] = df.to_dict(orient='records')
    elif request.method == 'POST':
        if request.form.get("Skip"):
            df2 = df
            return redirect(url_for('pragmatic.pregunta_2'))
        if 'Tipus' not in request.form:
            error = True
        else:     
            selected_items = request.form.getlist('Tipus')
            df2 = filtratge(df, 'Type', selected_items)

            if request.form.get("Next"):
                return redirect(url_for('pragmatic.pregunta_2'))
            elif request.form.get('Recomana'):
                session['last'] = '1'
                session['data'] = df2.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))  
           
    return render_template('/pragmatic/pregunta1.html', error = error)


@pragmatic_bp.route('/pragmatic_pregunta2', methods = ['GET', 'POST'])
def pregunta_2():
    global df2, df3
    error = False
    categories_preu = categories(df2, 'Price')
    dict_preu = [(categoria, constants.preu_dict.get(categoria)) for categoria in categories_preu]
    
    if request.method == 'GET':
        
        if len(dict_preu) == 1:
            df3 = filtratge_categories(df2, 'Price', dict_preu[0])
            return redirect(url_for('pragmatic.pregunta_3'))

    if request.method == 'POST':
        if request.form.get("Skip"):
            df3 = df2
            return redirect(url_for('pragmatic.pregunta_3'))
        if 'Preu' not in request.form:
            error = True
        else: 
            selected_items = request.form.getlist('Preu')
            df3 = filtratge_categories(df2, 'Price', selected_items)
            if request.form.get('Next'):
                return redirect(url_for('pragmatic.pregunta_3'))
            elif request.form.get('Recomana'):
                session['last'] = '2'
                session['data'] = df3.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))
            
    return render_template('/pragmatic/pregunta2.html', preu = dict_preu, error = error)


@pragmatic_bp.route('/pragmatic_pregunta3', methods = ['GET', 'POST'])
def pregunta_3():
    global df3, df4
    error = False
    gustos = df3['Taste'].unique().tolist()
    dict_gustos = [(gust, constants.gustos_dict.get(gust, gust)) for gust in gustos]

    if request.method == 'GET':
        if len(dict_gustos) == 1:
            df4 = filtratge(df3, 'Taste', dict_gustos[0])
            return redirect(url_for('pragmatic.pregunta_4'))

    if request.method == 'POST':
        if request.form.get("Skip"):
            df4 = df3
            return redirect(url_for('pragmatic.pregunta_4'))
        if 'Gust' not in request.form:
            error = True
        else:        
            selected_items = request.form.getlist('Gust')
            df4 = filtratge(df3, 'Taste', selected_items)
            
            if request.form.get('Next'):
                return redirect(url_for('pragmatic.pregunta_4'))
            if request.form.get('Recomana'):
                session['last'] = '3'
                session['data'] = df4.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))
            
    return render_template('/pragmatic/pregunta3.html', gustos = dict_gustos, error = error)


@pragmatic_bp.route('/pragmatic_pregunta4', methods = ['GET', 'POST'])
def pregunta_4():
    global df4, df5
    tots_els_menjars = df4['FoodParing'].str.split(',').explode()
    tots_els_menjars = tots_els_menjars.str.strip()
    menjars = tots_els_menjars.unique().tolist()+['Others']
    error = False
    
    if request.method == 'GET':
        if len(menjars) == 1:
            if 'Altres' in menjars:
                regex_pattern = '|'.join(menjars)
                df5 = df4[df4['FoodParing'].str.contains(regex_pattern, case=False, na=False)]
                session['data'] = df5.to_dict(orient='records')
            else:
                df5 = df4
                session['data'] = df5.to_dict(orient='records')
            return redirect(url_for(RECOMANACIO))
    
    if request.method == 'POST':
        session['last'] = '4'
        if 'Menjar' not in request.form:
            df5 = df4
            #return redirect(url_for(RECOMANACIO))
        else:        
            selected_items = request.form.getlist('Menjar')
            if 'Altres' in selected_items:
                selected_items.remove('Altres')
                if len(selected_items) == 0:
                    selected_items = menjars
            regex_pattern = '|'.join(selected_items)
            df5 = df4[df4['FoodParing'].str.contains(regex_pattern, case=False, na=False)]
            
        session['data'] = df5.to_dict(orient='records')
        return redirect(url_for(RECOMANACIO))
    
    return render_template('/pragmatic/pregunta4.html', menjars = menjars, error = error)
        

@pragmatic_bp.route('/pragmatic_recomancio')
def recomanacio():
    data = session.get('data', [])
    last = session.get('last')
    print(data)
    return render_template('/pragmatic/recomanacio.html', data = data, last = last)