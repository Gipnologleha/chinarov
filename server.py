from collections import namedtuple
import numpy as np
import pandas as pd
from flask import Flask,render_template 
from flask import redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
app = Flask(__name__)          
app.config.from_object(Config) 
db = SQLAlchemy(app)            
migrate = Migrate(app, db)      
from models import CowsBreeds1
from models import CowsBreeds2


Chcount1 = namedtuple('ustoychivost', 'chraschet')
chcounts1 = []

Chcount2 = namedtuple('ustoychivost', 'chraschet')
chcounts2 = []

Chcount1r = namedtuple('ustoychivost', 'chraschet')
chcounts1r = []

Chcount2r = namedtuple('ustoychivost', 'chraschet')
chcounts2r = []


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/eng',  methods=['GET'])
def eng():   #значения из обработчика падают сюда - в функцию.
    return render_template('eng.html', chcounts1=chcounts1, chcounts2=chcounts2)

@app.route('/rus',  methods=['GET'])
def rus():   #значения из обработчика падают сюда - в функцию.
    return render_template('rus.html', chcounts1r=chcounts1r, chcounts2r=chcounts2r)

@app.route('/eng1', methods=['POST'])
def chinarovcount1 ():
    try:
        longtitude1 = float(request.form['chlongtitude1'])
        latitude1 = float(request.form['chlatitude1'])
        breed1 = request.form['chbreed1']
        type1 = request.form['chtype1']
        yeild1 = float(request.form['chudoy1'])
        fat1 = float(request.form['chjir1'])
        protein1 = float(request.form['chbelok1'])
        weight1 = float(request.form['chmassa1'])
        first_calving_days1 = float(request.form['chperviy_otel_dney1'])
        age_in_calving1 = float(request.form['chv_otelah1'])
        leaving_in_calving1 = float(request.form['chvibitiya_v_otelah1'])
        service_period1 = float(request.form['chservis_period1'])
        dry_period1 = float(request.form['chsuhostoyniy_period1'])
        calving_per100_heads1 = float(request.form['chvihod_telyat_na100_golov1'])




        cowbreed1 = CowsBreeds1(
            longtitude1 = longtitude1,
            latitude1 = latitude1,
            breed1 = breed1,
            type1 = type1,
            yeild1 = yeild1,
            fat1 = fat1,
            protein1 = protein1,
            weight1 = weight1,
            first_calving_days1 = first_calving_days1,
            age_in_calving1 = age_in_calving1,
            leaving_in_calving1 = leaving_in_calving1,
            service_period1 = service_period1,
            dry_period1 = dry_period1,
            calving_per100_heads1 = calving_per100_heads1
            )
        db.session.add(cowbreed1)
        db.session.commit()


        def first_meat_indicator1 (type1):
            first_meat_indicator = 0
            if type1 == 'dairy':
                first_meat_indicator=238.556
            elif type1 == 'combined':
                first_meat_indicator=280.038
            elif type1 == 'intensive':
                first_meat_indicator=258.886
            return (first_meat_indicator)

        def second_meat_indicator1 (type1):
            second_meat_indicator = 0
            if type1 == 'dairy':
                second_meat_indicator=0.509
            elif type1 == 'combined':
                second_meat_indicator=0.539
            elif type1 == 'intensive':
                second_meat_indicator=0.503
            return (second_meat_indicator)


        daily_average_yeild1 = yeild1/305
        interbody_period1 = 285+service_period1
        lactation_duration1 = interbody_period1-dry_period1
        productive_use_duration1 = interbody_period1*(leaving_in_calving1-1)
        rejection1 = 365.25/productive_use_duration1
        total_yeild1 = np.round(((leaving_in_calving1-1)*daily_average_yeild1*lactation_duration1),2)
        total_fat_protein1 = np.round(((protein1+fat1)*total_yeild1/100),2)
        total_heifers1 = np.round((leaving_in_calving1/2*0.9),2) 
        total_meat1 = np.round((first_meat_indicator1(type1)*(total_heifers1+1)/second_meat_indicator1(type1)),2)
        total_safety1 = np.round((1 - rejection1),2)

        chcounts1.append(Chcount1([
            total_yeild1, total_fat_protein1, total_heifers1, total_meat1, total_safety1
            ]), )


        return redirect(url_for('eng')) #передает данные в именно в функцию eng
    except ZeroDivisionError:
        return "age in calving could not be equal 1, please enter another value"
    except ValueError:
        return """You entered text instead of numbers.
        Or missed the field.
        Please check the data you entered.
        Separate decimal places with a dot ( . )"""
    
@app.route('/eng2', methods=['POST'])
def chinarovcount2 ():
    try:
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
            perviy_pokazatel_myasnosti2 = 0

            if type2 == 'dairy':
                perviy_pokazatel_myasnosti2=238.556
            elif type2 == 'combined':
                perviy_pokazatel_myasnosti2=280.038
            elif type2 == 'intensive':
                perviy_pokazatel_myasnosti2=258.886
            return (perviy_pokazatel_myasnosti2)

        def pokazateli_myasnosti22 (type2):
            vtoroy_pokazatel_myasnosti22 = 0

            if type2 == 'dairy':
                vtoroy_pokazatel_myasnosti22=0.509
            elif type2 == 'combined':
                vtoroy_pokazatel_myasnosti22=0.539
            elif type2 == 'intensive':
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


        return redirect(url_for('eng'))
    except ZeroDivisionError:
        return "age in calving could not be equal 1, please enter another value"
    except ValueError:
        return """You entered text instead of numbers.
        Or missed the field.
        Please check the data you entered.
        Separate decimal places with a dot ( . )"""


@app.route('/rus1', methods=['POST'])
def rus1 ():
    try:
        longtitude1 = float(request.form['chlongtitude1'])
        latitude1 = float(request.form['chlatitude1'])
        breed1 = request.form['chbreed1']
        type1 = request.form['chtype1']
        yeild1 = float(request.form['chudoy1'])
        fat1 = float(request.form['chjir1'])
        protein1 = float(request.form['chbelok1'])
        weight1 = float(request.form['chmassa1'])
        first_calving_days1 = float(request.form['chperviy_otel_dney1'])
        age_in_calving1 = float(request.form['chv_otelah1'])
        leaving_in_calving1 = float(request.form['chvibitiya_v_otelah1'])
        service_period1 = float(request.form['chservis_period1'])
        dry_period1 = float(request.form['chsuhostoyniy_period1'])
        calving_per100_heads1 = float(request.form['chvihod_telyat_na100_golov1'])




        cowbreed1 = CowsBreeds1(
            longtitude1 = longtitude1,
            latitude1 = latitude1,
            breed1 = breed1,
            type1 = type1,
            yeild1 = yeild1,
            fat1 = fat1,
            protein1 = protein1,
            weight1 = weight1,
            first_calving_days1 = first_calving_days1,
            age_in_calving1 = age_in_calving1,
            leaving_in_calving1 = leaving_in_calving1,
            service_period1 = service_period1,
            dry_period1 = dry_period1,
            calving_per100_heads1 = calving_per100_heads1
            )
        db.session.add(cowbreed1)
        db.session.commit()


        def first_meat_indicator1 (type1):
            first_meat_indicator = 0
            if type1 == 'молочная':
                first_meat_indicator=238.556
            elif type1 == 'комбинированная':
                first_meat_indicator=280.038
            elif type1 == 'интенсивная':
                first_meat_indicator=258.886
            return (first_meat_indicator)

        def second_meat_indicator1 (type1):
            second_meat_indicator = 0
            if type1 == 'молочная':
                second_meat_indicator=0.509
            elif type1 == 'комбинированная':
                second_meat_indicator=0.539
            elif type1 == 'интенсивная':
                second_meat_indicator=0.503
            return (second_meat_indicator)


        daily_average_yeild1 = yeild1/305
        interbody_period1 = 285+service_period1
        lactation_duration1 = interbody_period1-dry_period1
        productive_use_duration1 = interbody_period1*(leaving_in_calving1-1)
        rejection1 = 365.25/productive_use_duration1
        total_yeild1 = np.round(((leaving_in_calving1-1)*daily_average_yeild1*lactation_duration1),2)
        total_fat_protein1 = np.round(((protein1+fat1)*total_yeild1/100),2)
        total_heifers1 = np.round((leaving_in_calving1/2*0.9),2) 
        total_meat1 = np.round((first_meat_indicator1(type1)*(total_heifers1+1)/second_meat_indicator1(type1)),2)
        total_safety1 = np.round((1 - rejection1),2)

        chcounts1r.append(Chcount1r([
            total_yeild1, total_fat_protein1, total_heifers1, total_meat1, total_safety1
            ]), )


        return redirect(url_for('rus')) #передает данные в именно в функцию eng
    except ZeroDivisionError:
        return "age in calving could not be equal 1, please enter another value"
    except ValueError:
        return """You entered text instead of numbers.
        Or missed the field.
        Please check the data you entered.
        Separate decimal places with a dot ( . )"""
    

@app.route('/rus2', methods=['POST'])
def rus2 ():
    try:
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
            perviy_pokazatel_myasnosti2 = 0

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

        chcounts2r.append(Chcount2r([ #скобка открывающая кортеж
            #summ # возврат значения, указанного в функции, summ и есть это значение
            total_nadoi2, total_jir_belok2, total_vihod_neteley2, total_myaso2, total_sohrannost2
            ]), ) #скобка закрывающая кортеж и его результат


        return redirect(url_for('rus'))
    except ZeroDivisionError:
        return "Возраст выбытия в отелах не может быть равен 1, пожалуйста, введите другое значение"
    except ValueError:
        return """Выввели текст вместо цифр.
        Или пропустили поле.
        Пожалуйста, проверте введенные вами данные.
        Отделяйте десятичные знаки точкой ( . )"""




if __name__ == '__main__':  #файл запускается напрямую
    app.run(debug=True)