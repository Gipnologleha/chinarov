from collections import namedtuple # импорт кортежей

import numpy as np
import pandas as pd
from flask import Flask,render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy # РАССШИРЕННОЕ
from flask_migrate import Migrate

from config import Config # импортируем конфиг  


app = Flask(__name__)           # __name__   -   имя текущего файла
app.config.from_object(Config)  # вносим конфиг из файла config.py
db = SQLAlchemy(app)            # инициализируем базу данных
migrate = Migrate(app, db)      # инициализируем миграции

from models import CowsBreeds1
from models import CowsBreeds2


Chcount1 = namedtuple('ustoychivost', 'chraschet')
chcounts1 = []

Chcount2 = namedtuple('ustoychivost', 'chraschet')
chcounts2 = []

total_nadoi1 = list()

@app.route('/chinarov',  methods=['GET', 'POST'])
def chinarov():
    return render_template('chinarov.html')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', chcounts1=chcounts1, chcounts2=chcounts2, total_nadoi1=total_nadoi1)

@app.route('/chinarovcount1', methods=['POST'])
def chinarovcount1 ():

    longtitude1 = float(request.form['chlongtitude1'])
    latitude1 = float(request.form['chlatitude1'])
    breed1 = request.form['chbreed1']
    type1 = request.form['chtype1']
    udoy1 = float(request.form['chudoy1'])
    jir1 = float(request.form['chjir1'])
    belok1 = float(request.form['chbelok1'])
    massa1 = float(request.form['chmassa1'])
    perviy_otel_dney1 = float(request.form['chperviy_otel_dney1'])
    v_otelah1 = float(request.form['chv_otelah1'])
    vibitiya_v_otelah1 = float(request.form['chvibitiya_v_otelah1'])
    servis_period1 = float(request.form['chservis_period1'])
    suhostoyniy_period1 = float(request.form['chsuhostoyniy_period1'])
    vihod_telyat_na100_golov1 = float(request.form['chvihod_telyat_na100_golov1'])
    total_otely1 = v_otelah1+30

    cowbreed1 = CowsBreeds1(
        longtitude1 = longtitude1,
        latitude1 = latitude1,
        breed1 = breed1,
        type1 = type1,
        udoy1 = udoy1,
        jir1 = jir1,
        belok1 = belok1,
        massa1 = massa1,
        perviy_otel_dney1 = perviy_otel_dney1,
        v_otelah1 = v_otelah1,
        vibitiya_v_otelah1 = vibitiya_v_otelah1,
        servis_period1 = servis_period1,
        suhostoyniy_period1 = suhostoyniy_period1,
        vihod_telyat_na100_golov1 = vihod_telyat_na100_golov1
    
        )

    db.session.add(cowbreed1)
    db.session.commit()


    def pokazateli_myasnosti1 (type1):
        perviy_pokazatel_myasnosti1 = 0

        if type1 == 'молочная':
            perviy_pokazatel_myasnosti1=238.556
        elif type1 == 'комбинированная':
            perviy_pokazatel_myasnosti1=280.038
        elif type1 == 'интенсивная':
            perviy_pokazatel_myasnosti1=258.886
        return (perviy_pokazatel_myasnosti1)

    def pokazateli_myasnosti12 (type1):
        vtoroy_pokazatel_myasnosti1 = 0

        if type1 == 'молочная':
            vtoroy_pokazatel_myasnosti1=0.509
        elif type1 == 'комбинированная':
            vtoroy_pokazatel_myasnosti1=0.539
        elif type1 == 'интенсивная':
            vtoroy_pokazatel_myasnosti1=0.503
        return (vtoroy_pokazatel_myasnosti1)


    srednesutochniy_udoy1 = udoy1/305
    mejotelniy_period1 = 285+servis_period1
    prodoljitelnost_laktacii1 = mejotelniy_period1-suhostoyniy_period1
    dlitelnost_productivnogo_ispolzovaniya1 = mejotelniy_period1*(vibitiya_v_otelah1-1)
    vibrakovka1 = 365.25/dlitelnost_productivnogo_ispolzovaniya1
    total_nadoi1 = np.round(((vibitiya_v_otelah1-1)*srednesutochniy_udoy1*prodoljitelnost_laktacii1),2) #надой расчитан верно
    total_jir_belok1 = np.round(((belok1+jir1)*total_nadoi1/100),2) # верно
    total_vihod_neteley1 = np.round((vibitiya_v_otelah1/2*0.9),2) # верно
    total_myaso1 = np.round((pokazateli_myasnosti1(type1)*(total_vihod_neteley1+1)/pokazateli_myasnosti12(type1)),2) # расчет верный. Вопрос как подать на сервер значения из выпадающего списка
    total_sohrannost1 = np.round((1 - vibrakovka1),2) # верно

    

    chcounts1.append(Chcount1([ #скобка открывающая кортеж
        #summ # возврат значения, указанного в функции, summ и есть это значение
        total_nadoi1, total_jir_belok1, total_vihod_neteley1, total_myaso1, total_sohrannost1
        ]), ) #скобка закрывающая кортеж и его результат


    return redirect(url_for('index'))
    

@app.route('/chinarovcount2', methods=['POST'])
def chinarovcount2 ():

    longtitude2 = float(request.form['chlongtitude2'])
    latitude2 = float(request.form['chlatitude2'])
    breed2 = request.form['chbreed2']
    type2 = request.form['chtype2']
    udoy2 = float(request.form['chudoy2'])
    jir2 = float(request.form['chjir2'])
    belok2 = float(request.form['chbelok2'])
    massa2 = float(request.form['chmassa2'])
    perviy_otel_dney2 = float(request.form['chperviy_otel_dney2'])
    v_otelah2 = float(request.form['chv_otelah2'])
    vibitiya_v_otelah2 = float(request.form['chvibitiya_v_otelah2'])
    servis_period2 = float(request.form['chservis_period2'])
    suhostoyniy_period2 = float(request.form['chsuhostoyniy_period2'])
    vihod_telyat_na100_golov2 = float(request.form['chvihod_telyat_na100_golov2'])

    cowbreed2 = CowsBreeds2(
        longtitude2 = longtitude2,
        latitude2 = latitude2,
        breed2 = breed2,
        type2 = type2,
        udoy2 = udoy2,
        jir2 = jir2,
        belok2 = belok2,
        massa2 = massa2,
        perviy_otel_dney2 = perviy_otel_dney2,
        v_otelah2 = v_otelah2,
        vibitiya_v_otelah2 = vibitiya_v_otelah2,
        servis_period2 = servis_period2,
        suhostoyniy_period2 = suhostoyniy_period2,
        vihod_telyat_na100_golov2 = vihod_telyat_na100_golov2
    
        )

    db.session.add(cowbreed2)
    db.session.commit()


    def pokazateli_myasnosti2 (type2):
        perviy_pokazatel_myasnosti1 = 0

        if type2 == 'молочная':
            perviy_pokazatel_myasnosti2=238.556
        elif type2 == 'комбинированная':
            perviy_pokazatel_myasnosti2=280.038
        elif type2 == 'интенсивная':
            perviy_pokazatel_myasnosti2=258.886
        return (perviy_pokazatel_myasnosti2)

    def pokazateli_myasnosti22 (type2):
        vtoroy_pokazatel_myasnosti22 = 0

        if type2 == 'молочная':
            vtoroy_pokazatel_myasnosti22=0.509
        elif type2 == 'комбинированная':
            vtoroy_pokazatel_myasnosti22=0.539
        elif type2 == 'интенсивная':
            vtoroy_pokazatel_myasnosti22=0.503
        return (vtoroy_pokazatel_myasnosti22)


    srednesutochniy_udoy2 = udoy2/305
    mejotelniy_period2 = 285+servis_period2
    prodoljitelnost_laktacii2 = mejotelniy_period2-suhostoyniy_period2
    dlitelnost_productivnogo_ispolzovaniya2 = mejotelniy_period2*(vibitiya_v_otelah2-1)
    vibrakovka2 = 365.25/dlitelnost_productivnogo_ispolzovaniya2
    total_nadoi2 = np.round(((vibitiya_v_otelah2-1)*srednesutochniy_udoy2*prodoljitelnost_laktacii2),2) #надой расчитан верно
    total_jir_belok2 = np.round(((belok2+jir2)*total_nadoi2/100),2) # верно
    total_vihod_neteley2 = np.round((vibitiya_v_otelah2/2*0.9),2) # верно
    total_myaso2 = np.round((pokazateli_myasnosti2(type2)*(total_vihod_neteley2+1)/pokazateli_myasnosti22(type2)),2) # расчет верный. Вопрос как подать на сервер значения из выпадающего списка
    total_sohrannost2 = np.round((1 - vibrakovka2),2) # верно

    chcounts2.append(Chcount2([ #скобка открывающая кортеж
        #summ # возврат значения, указанного в функции, summ и есть это значение
        total_nadoi2, total_jir_belok2, total_vihod_neteley2, total_myaso2, total_sohrannost2
        ]), ) #скобка закрывающая кортеж и его результат


    return redirect(url_for('index'))





if __name__ == '__main__':  #файл запускается напрямую
    app.run(debug=True)