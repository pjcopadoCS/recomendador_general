from flask import Blueprint, redirect, render_template, session, url_for, request
import pandas as pd
import constants

from utils import filtratge

expert_bp = Blueprint('expert', __name__)

df, df2, df3, df4, df5, df6, df7, df8 = [None]*8
RECOMANACIO = 'expert.recomanacio'

@expert_bp.route('/expert_pregunta1', methods = ['GET', 'POST'])
def pregunta_1():
    global df, df2
    error = False
    if request.method == 'GET':
        df = pd.read_excel('wines_dataset.xlsx', dtype={'Year': str})
        session['data'] = df.to_dict(orient='records')
    elif request.method == 'POST':
        if request.form.get("Skip"):
            df2 = df
            return redirect(url_for('expert.pregunta_2'))
        if 'Tipus' not in request.form:
            error = True
        else:
            selected_items = request.form.getlist('Tipus')
            df2 = filtratge(df, 'Type', selected_items)
            if request.form.get("Next"):
                return redirect(url_for('expert.pregunta_2'))
            elif request.form.get('Recomana'):
                session['last'] = '1'
                session['data'] = df2.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))    
             
    return render_template('/expert/pregunta1.html', error = error)

@expert_bp.route('/expert_pregunta2', methods = ['GET', 'POST'])
def pregunta_2():
    global df2, df3
    error = False
    paisos = df2['Country'].unique().tolist()
    dict_paisos = [(pais, constants.paisos_dict.get(pais, pais)) for pais in paisos]
    reconeguts = constants.paisos_reconeguts
    
    if request.method == 'GET':
        if len(dict_paisos)==1:
            df3 = filtratge(df2, 'Country',dict_paisos[0])
            return redirect(url_for('expert.pregunta_3'))
    
    if request.method == 'POST':
        if request.form.get("Skip"):
            df3 = df2
            return redirect(url_for('expert.pregunta_3'))
        
        if 'Pais' not in request.form:
            error = True
        else:
            selected_items = [item.rstrip('/') for item in request.form.getlist('Pais')]
            df3 = filtratge(df2, 'Country', selected_items)

            if request.form.get('Next'):
                return redirect(url_for('expert.pregunta_3'))
            elif request.form.get('Recomana'):
                session['last'] = '2'
                session['data'] = df3.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))
            
    return render_template(
        '/expert/pregunta2.html', 
        paisos = dict_paisos,
        reconeguts = reconeguts,
        error = error,
    )

@expert_bp.route('/expert_pregunta3', methods = ['GET', 'POST'])
def pregunta_3():
    global df3, df4
    error = False
    regions = df3['Region'].unique().tolist()
    
    if request.method == 'GET':
        if len(regions)==1:
            df4 = filtratge(df3, 'Region',regions)
            return redirect(url_for('expert.pregunta_3'))

    if request.method == 'POST':
        if request.form.get("Skip"):
            df4 = df3
            return redirect(url_for('expert.pregunta_4'))
        if 'Regio' not in request.form:
            error = True
        else:        
            selected_items = request.form.getlist('Regio')
            df4 = filtratge(df3, 'Region', selected_items)

            if request.form.get('Next'):
                return redirect(url_for('expert.pregunta_4'))
            if request.form.get('Recomana'):
                session['last'] = '3'
                session['data'] = df4.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))
            
    return render_template('/expert/pregunta3.html', regions = regions, error = error)

@expert_bp.route('/expert_pregunta4', methods = ['GET', 'POST'])
def pregunta_4():
    global df4, df5
    error = False
    tots_els_raims = df4['GrapeVariety'].str.split(',').explode()
    tots_els_raims = tots_els_raims.str.strip()
    raims = tots_els_raims.unique().tolist()
    nobles = constants.varietats_nobles
    
    if request.method == 'GET':
        if len(raims) == 1:    
            regex_pattern = '|'.join(raims)
            df5 = df4[df4['GrapeVariety'].str.contains(regex_pattern, case=False, na=False)]
            return redirect(url_for('expert.pregunta_5'))   

    if request.method == 'POST':
        if request.form.get("Skip"):
            df5 = df4
            return redirect(url_for('expert.pregunta_5'))
        if 'Raim' not in request.form:
            error = True
        else:        
            selected_items = request.form.getlist('Raim')
            regex_pattern = '|'.join(selected_items)
            df5 = df4[df4['GrapeVariety'].str.contains(regex_pattern, case=False, na=False)]
    
            if request.form.get('Next'):
                return redirect(url_for('expert.pregunta_5'))
            if request.form.get('Recomana'):
                session['last'] = '4'
                session['data'] = df5.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))
            
    return render_template(
        '/expert/pregunta4.html', 
        raims = raims,
        nobles = nobles,
        error = error,
    )


@expert_bp.route('/expert_pregunta5', methods = ['GET', 'POST'])
def pregunta_5():
    global df5, df6
    error = False
    dens_orig = df5['DO'].unique().tolist()
    
    if request.method == 'GET':
        if len(dens_orig) == 1:
            df6 = filtratge(df5, 'DO', dens_orig)
            return redirect(url_for('expert.pregunta_6'))

    if request.method == 'POST':
        if request.form.get("Skip"):
            df6 = df5
            return redirect(url_for('expert.pregunta_6'))
        if 'DO' not in request.form:
            error = True
        else:        
            selected_items = request.form.getlist('DO')
            df6 = filtratge(df5, 'DO', selected_items)

            if request.form.get('Next'):
                return redirect(url_for('expert.pregunta_6'))
            if request.form.get('Recomana'):
                session['last'] = '5'
                session['data'] = df6.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))
            
    return render_template('/expert/pregunta5.html', dens_orig = dens_orig, error = error)


@expert_bp.route('/expert_pregunta6', methods = ['GET', 'POST'])
def pregunta_6():
    global df6, df7
    error = False
    anys = df6['Year'].unique().tolist()
    
    if request.method == 'GET':
        if len(anys) == 1:
            df7 = filtratge(df6, 'Year', anys)
            return redirect(url_for('expert.pregunta_7'))
    
    
    if request.method == 'POST':
        if request.form.get("Skip"):
            df7 = df6
            return redirect(url_for('expert.pregunta_7'))
        if 'Any' not in request.form:
            error = True
        else:        
            selected_items = request.form.getlist('Any')
            df7 = filtratge(df6, 'Year', selected_items)
            
            if request.form.get('Next'):
                return redirect(url_for('expert.pregunta_7'))
            if request.form.get('Recomana'):
                session['last'] = '6'
                session['data'] = df7.to_dict(orient='records')
                return redirect(url_for(RECOMANACIO))
            
    return render_template('/expert/pregunta6.html', anys = anys, error = error)


@expert_bp.route('/expert_pregunta7', methods = ['GET', 'POST'])
def pregunta_7():
    global df7, df8
    tots_els_menjars = df7['FoodParing'].str.split(',').explode()
    tots_els_menjars = tots_els_menjars.str.strip()
    menjars = tots_els_menjars.unique().tolist()+['Altres']
    
    if request.method == 'GET':
        # Case en que només hi ha un tipus de menjar
        if len(menjars) == 1:
            # En cas que sigui altres, no es filtra
            if 'Altres' not in menjars:
                regex_pattern = '|'.join(menjars)
                df8 = df7[df7['FoodParing'].str.contains(regex_pattern, case=False, na=False)]
                session['data'] = df8.to_dict(orient='records')
            else:
                df8 = df7
                session['data'] = df8.to_dict(orient='records')
            return redirect(url_for(RECOMANACIO))
    
    if request.method == 'POST':
        session['last'] = '7'
        if 'Menjar' not in request.form:
            return redirect(url_for(RECOMANACIO))
        else:        
            selected_items = request.form.getlist('Menjar')
            if 'Altres' in selected_items:
                selected_items.remove('Altres')
                # Problema: si l'usuari selecciona només 'altres' llavors s'ha d'escollir tot, 
                # si esculla alguna altra opció s'ha d'esborrar 'altres'
                if len(selected_items) == 0:
                    selected_items = menjars
            regex_pattern = '|'.join(selected_items)
            df8 = df7[df7['FoodParing'].str.contains(regex_pattern, case=False, na=False)]
            
            session['data'] = df8.to_dict(orient='records')
            return redirect(url_for(RECOMANACIO))
    
    return render_template('/expert/pregunta7.html', menjars = menjars)


@expert_bp.route('/expert_recomancio')
def recomanacio():
    last = session.get('last')
    data = session.get('data', [])
    awarded = [product for product in data if product.get('Award') == True]
    not_awarded = [product for product in data if not product.get('Award')]
    return render_template(
        '/expert/recomanacio.html', 
        awarded = awarded, 
        not_awarded = not_awarded,
        last = last,
    )