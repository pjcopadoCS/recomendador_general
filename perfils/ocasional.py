from flask import Blueprint, redirect, render_template, session, url_for, request
import pandas as pd
import constants

from utils import categories, filtratge, filtratge_categories

ocasional_bp = Blueprint('ocasional', __name__)

df, df2, df3, df4 = [None]*4
RECOMANACIO = 'ocasional.recomanacio'

@ocasional_bp.route('/ocasional_pregunta1', methods = ['GET', 'POST'])
def pregunta_1():
    
    global df, df2
    error = False
    
    if request.method == 'GET':
        
        df = pd.read_excel('wines_dataset.xlsx')
        session['data'] = df.to_dict(orient='records')
        
    elif request.method == 'POST':
        
        if request.form.get("Skip"):
            
            df2 = df
            return redirect(url_for('ocasional.pregunta_2'))
        
        if 'Tipus' not in request.form:
        
            error = True
        
        else:
                 
            selected_items = request.form.getlist('Tipus')
            df2 = filtratge(df, 'Type', selected_items)

            if request.form.get("Next"):
                
                return redirect(url_for('ocasional.pregunta_2'))
            
            elif request.form.get('Recomana'):
                
                session['last'] = '1'
                session['data'] = df2.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))  
           
    return render_template('/ocasional/pregunta1.html', error = error)


@ocasional_bp.route('/ocasional_pregunta2', methods = ['GET', 'POST'])
def pregunta_2():
    
    global df2, df3
    error = False
    categories_alchol = categories(df2, 'Alcohol')
    dict_alcohol = [(categoria, constants.alcohol_dict.get(categoria)) for categoria in categories_alchol]

    if request.method == 'GET':
        if len(dict_alcohol) == 1:
            df3 = filtratge_categories(df2, 'Alcohol', dict_alcohol[0])
            return redirect(url_for('ocasional.pregunta_3'))
    
    if request.method == 'POST':
        if request.form.get("Skip"):
            df3 = df2
            return redirect(url_for('ocasional.pregunta_3'))
        
        if 'Alcohol' not in request.form:
            
            error = True
            
        else:
             
            selected_items = request.form.getlist('Alcohol')
            df3 = filtratge_categories(df2, 'Alcohol', selected_items)

            if request.form.get('Next'):
                
                return redirect(url_for('ocasional.pregunta_3'))
            
            elif request.form.get('Recomana'):
                
                session['last'] = '2'
                session['data'] = df3.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))
            
    return render_template('/ocasional/pregunta2.html', alcohol = dict_alcohol, error = error)


@ocasional_bp.route('/ocasional_pregunta_3', methods = ['GET', 'POST'])
def pregunta_3():
    
    global df3, df4
    gustos = df3['Taste'].unique().tolist()
    #dict_gustos = [(gust, constants.gustos_dict.get(gust, gust)) for gust in gustos]
    dict_gustos = [(gust, gust) for gust in gustos]
    gustos_ocasional = constants.gustos_ocasional

    if request.method == 'GET':
        if len(dict_gustos) == 1:
            df4 = filtratge(df3, 'Taste', dict_gustos[0])
            session['data'] = df4.to_dict(orient='records')
            return redirect(url_for(RECOMANACIO))
    
    if request.method == 'POST':
        
        session['last'] = '3'
        if 'Gust' not in request.form:
            
            return redirect(url_for(RECOMANACIO))
        
        else:   
                 
            selected_items = request.form.getlist('Gust')
            df4 = filtratge(df3, 'Taste', selected_items)
            
            session['data'] = df4.to_dict(orient='records')
            return redirect(url_for(RECOMANACIO))
            
    return render_template('/ocasional/pregunta3.html', gustos = dict_gustos, gustos_ocasional = gustos_ocasional)
    

@ocasional_bp.route('/ocasional_recomancio')
def recomanacio():
    data = session.get('data', [])
    last = session.get('last')
    return render_template('/ocasional/recomanacio.html', data = data, last = last)