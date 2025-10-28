from flask import Flask, render_template, flash, request, redirect

# Sujet 7
# Leo Krakovinsky
# https://cours-info.iut-bm.univ-fcomte.fr/upload/perso/77/rs_S1_DIW/diw/diw_tp3_1_projet_sujets_v25.html#sujet-7

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'une cle(token) : grain de sel(any random string)'


# id, libelleType, logo
typesReparations=[
    {'id':1,'libelleType':'entretien','logo':'logo_entretien.png'},
    {'id':2,'libelleType':'carrosserie','logo':'logo_carrosserie.png'},
    {'id':3,'libelleType':'mecanique','logo':'logo_mecanique.png'},
    {'id':4,'libelleType':'autre','logo':'logo_autre.png'}
]

# id, libelleReparation, immatVoiture, prixReparation, dateReparation, typeReparation_id, photo
reparations=[
    {'id':1,'libelleReparation':'Vidange' , 'immatVoiture':'RP-456-ZF' , 'prixReparation':'50' , 'dateReparation':'2014-10-15' , 'typeReparation_id':1, 'photo':'intervention_1.png'},
    {'id':2,'libelleReparation':'Vidange' , 'immatVoiture':'HK-856-SN' , 'prixReparation':'89' , 'dateReparation':'2005-05-06' , 'typeReparation_id':1, 'photo':'intervention_1.png'},
    {'id':3,'libelleReparation':'Vidange' , 'immatVoiture':'SD-479-EG' , 'prixReparation':'57' , 'dateReparation':'2007-08-08' , 'typeReparation_id':1, 'photo':'intervention_1.png'},
    {'id':4,'libelleReparation':'Vidange' , 'immatVoiture':'KU-458-VX' , 'prixReparation':'68' , 'dateReparation':'2007-04-13' , 'typeReparation_id':1, 'photo':'intervention_1.png'},
    {'id':5,'libelleReparation':'Remplac. pare brise' , 'immatVoiture':'LY-228-EY' , 'prixReparation':'250.00' , 'dateReparation':'2003-12-30' , 'typeReparation_id':2, 'photo':'intervention_2.png'},
    {'id':6,'libelleReparation':'Remplac. pare brise' , 'immatVoiture':'DS-865-KT' , 'prixReparation':'175.65' , 'dateReparation':'2011-05-06' , 'typeReparation_id':2, 'photo':'intervention_2.png'},
    {'id':7,'libelleReparation':'révision' , 'immatVoiture':'XG-554-DD' , 'prixReparation':'100' , 'dateReparation':'2010-03-01' , 'typeReparation_id':1, 'photo':'intervention_3.png'},
    {'id':8,'libelleReparation':'révision' , 'immatVoiture':'JK-103-DG' , 'prixReparation':'90' , 'dateReparation':'2001-05-06' , 'typeReparation_id':1, 'photo':'intervention_3.png'},
    {'id':9,'libelleReparation':'Changement pneus' , 'immatVoiture':'KU-458-VX' , 'prixReparation':'30.54' , 'dateReparation':'2007-04-13' , 'typeReparation_id':1, 'photo':'intervention_4.png'},
    {'id':10,'libelleReparation':'Changement pneus' , 'immatVoiture':'LY-228-EY' , 'prixReparation':'224.21' , 'dateReparation':'2009-12-30' , 'typeReparation_id':1, 'photo':'intervention_4.png'},
    {'id':11,'libelleReparation':'Changement pneus' , 'immatVoiture':'DS-865-KT' , 'prixReparation':'227.00' , 'dateReparation':'2011-05-06' , 'typeReparation_id':1, 'photo':'intervention_4.png'},
    {'id':12,'libelleReparation':'Remplacement plaq. de frein' , 'immatVoiture':'XG-554-DD' , 'prixReparation':'150' , 'dateReparation':'2010-03-01' , 'typeReparation_id':1, 'photo':'intervention_5.png'},
    {'id':13,'libelleReparation':'Tambour freins arr.' , 'immatVoiture':'CD-665-GZ' , 'prixReparation':'180' , 'dateReparation':'2012-05-06' ,  'typeReparation_id':3, 'photo':'intervention_6.png'},
    {'id':14,'libelleReparation':'Remplacement plaq. de frein' , 'immatVoiture':'KU-458-VX' , 'prixReparation':'100' , 'dateReparation':'2007-04-13' , 'typeReparation_id':1, 'photo':'intervention_5.png'},
    {'id':15,'libelleReparation':'Changement des cardans' , 'immatVoiture':'LY-228-EY' , 'prixReparation':'1300' , 'dateReparation':'2009-12-30' ,  'typeReparation_id':3, 'photo':'intervention_7.png'},
    {'id':16,'libelleReparation':'Changement boite de vitesse' , 'immatVoiture':'DS-865-KT' , 'prixReparation':'1400' , 'dateReparation':'2011-05-06', 'typeReparation_id':3, 'photo':'intervention_8.png'} ,
    {'id':17,'libelleReparation':'Remplac. courroie distribution' , 'immatVoiture':'XG-554-DD' , 'prixReparation':'440', 'dateReparation':'2010-03-01' ,  'typeReparation_id':3, 'photo':'intervention_9.png'} ,
    {'id':18,'libelleReparation':'Remplac. courroie distribution' , 'immatVoiture':'JK-103-DG' , 'prixReparation':'460' , 'dateReparation':'2001-05-06' ,  'typeReparation_id':3, 'photo':'intervention_9.png'}
]

@app.route('/')
def home_page():
    return render_template('layout.html')

@app.route('/type-reparation/show', methods=['GET'])
def show_type_reparation():
    return render_template('type_reparation/show_type_reparation.html',types=typesReparations)


# Add
@app.route('/type-reparation/add', methods=['GET'])
def add_type_reparation():
    return render_template('type_reparation/add_type_reparation.html',types=typesReparations)

@app.route('/type-reparation/add', methods=['POST'])
def valid_add_type_reparation():
    # id_type = request.form['id_type']
    nom = request.form['nom']
    logo = request.form['logo']
    flash(f'Type reparation ajoute: {nom}, {logo}', 'alert-success')
    print(request.form)
    return render_template('type_reparation/show_type_reparation.html',types=typesReparations)


# Delete
@app.route('/type-reparation/delete', methods=['GET'])
def delete_type_reparation():
    id = request.args.get('id')
    flash(f'Type reparation id={id} supprime', 'alert-warning')
    return render_template('type_reparation/show_type_reparation.html',types=typesReparations)
# Edit
@app.route('/type-reparation/edit', methods=['GET'])
def edit_type_reparation():
    id = request.args.get('id', '')
    id=int(id)
    type_reparation = typesReparations[id-1]
    return render_template('type_reparation/edit_type_reparation.html',reparation=type_reparation)

@app.route('/type-reparation/edit', methods=['POST'])
def valid_edit_type_reparation():
    id_type = request.form['id_type']
    nom = request.form['nom']
    logo = request.form['logo']
    print(request.form)
    flash(f'Type reparation edite {id_type} {nom} {logo}', 'alert-success')
    return render_template('type_reparation/show_type_reparation.html',types=typesReparations)






############# REPARATIONS ##########

@app.route('/reparation/show', methods=['GET'])
def show_reparation():
    return render_template('reparation/show_reparation.html', reparations=reparations)


# Add
@app.route('/reparation/add', methods=['GET'])
def add_reparation():
    return render_template('reparation/add_reparation.html', types=typesReparations)

@app.route('/reparation/add', methods=['POST'])
def valid_add_reparation():
    # Args: id_reparation nom immatriculation prix date type image
    # id_reparation = request.form['id_reparation']
    nom_reparation = request.form['nom']
    immatriculation = request.form['immatriculation']
    prix = request.form['prix']
    date = request.form['date']
    type_reparation = request.form['type']
    logo_reparation = request.form['image']

    flash(f'Ajoute {nom_reparation} {immatriculation} {prix} {date} {type_reparation} {logo_reparation}', 'alert-success')
    return render_template('reparation/show_reparation.html', reparations=reparations)


# Delete
@app.route('/reparation/delete', methods=['GET'])
def delete_reparation():
    id = request.args.get('id')
    flash(f'reparation supprime {id}', 'alert-warning')
    return render_template('reparation/show_reparation.html', reparations=reparations)

# Edit
@app.route('/reparation/edit', methods=['GET'])
def edit_reparation():
    repar_id = request.args.get('id')
    print(repar_id)
    rep = reparations[int(repar_id)-1]
    return render_template('reparation/edit_reparation.html', types=typesReparations, reparation=rep)

@app.route('/reparation/edit', methods=['POST'])
def valid_edit_reparation():
    libelle = request.form['nom']
    immatVoiture = request.form['immatriculation']
    prixReparation = request.form['prix']
    dateReparation = request.form['date']
    typeReparation = request.form['type']
    flash(f'reparation edite: {libelle}, {immatVoiture}, {prixReparation}, {dateReparation}, {typeReparation}', 'alert-success')
    return render_template('reparation/show_reparation.html', reparations=reparations)

@app.route('/reparation/filtre', methods=['GET'])
def filtre_reparation():
    return render_template('reparation/front_reparation_filtre_show.html', reparations=reparations, types=typesReparations)

@app.route('/reparation/filtre', methods=['POST'])
def valid_filtre_reparation():
    filter_word = request.form.get('filter_word', None)
    filter_value_min = request.form.get('filter_value_min', None)
    filter_value_max = request.form.get('filter_value_max', None)

    # getlist au lieu de get ? get donnait un string pour une raison qui m'echappe
    # https://stackoverflow.com/questions/31859903/get-the-value-of-a-checkbox-in-flask
    filter_items = request.form.getlist('filter_items', None)
    if filter_word and filter_word != "":
        message = u'filtre sur le mot : '  + filter_word
        flash(message, 'alert-success')

    if filter_value_min or filter_value_max:
        min=str(filter_value_min).replace(' ', '').replace(',', ',')
        max=str(filter_value_max).replace(' ', '').replace(',', ',')
        if min.replace('.', '', 1).isdigit() \
            and max.replace('.', '', 1).isdigit():
            if float(min) < float(max):
                message = u'filtre sur la colone avec un numeriquqe entre ' + str(min) + ', ' + str(max) + ', '
                flash(message, 'alert-success')
            else:
                message = u'min > max'
                flash(message, 'alert-warning')
        else:
            message = u'min ' + min + ' et max ' + max + ' doivent etre des numeriques positifs'
            flash(message, 'alert-warning')

    if filter_items and filter_items != []:
        message = u'case a cocher selectionnee: '
        for case in filter_items:
            message += ' id: ' + case + ' '

        flash(message, 'alert-success')

    return redirect('/reparation/filtre')
if __name__ == '__main__':
    app.run()
