from flask import Flask, render_template

# Sujet 7
# Leo Krakovinsky
# https://cours-info.iut-bm.univ-fcomte.fr/upload/perso/77/rs_S1_DIW/diw/diw_tp3_1_projet_sujets_v25.html#sujet-7

app = Flask(__name__)


# id, libelleType, logo
typesReparations=[
    {'id':1,'libelleType':'entretien','logo':'logo_entretien.png'},
    {'id':2,'libelleType':'carrosserie','logo':'logo_carrosserie.png'},
    {'id':3,'libelleType':'mecanique','logo':'mecanique.png'},
    {'id':4,'libelleType':'autre','logo':'autre.png'}
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


if __name__ == '__main__':
    app.run()
