from server import db


class CowsBreeds1(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    longtitude1 = db.Column(db.Float, nullable = False)
    latitude1 = db.Column(db.Float, nullable = False)
    breed1 = db.Column(db.String, nullable = False)
    type1 = db.Column(db.String, nullable = False)
    yeild1 = db.Column(db.Float, nullable = False)
    fat1 = db.Column(db.Float, nullable = False)
    protein1 = db.Column(db.Float, nullable = False)
    weight1 = db.Column(db.Float, nullable = False)
    first_calving_days1 = db.Column(db.Float, nullable = False)
    age_in_calving1 = db.Column(db.Float, nullable = False)
    leaving_in_calving1 = db.Column(db.Float, nullable = False)
    service_period1 = db.Column(db.Float, nullable = False)
    dry_period1 = db.Column(db.Float, nullable = False)
    calving_per100_heads1 = db.Column(db.Float, nullable = False)

    def __repr__(self):
        return '<CowsBreeds1 {}>'.format(self.breed)


class CowsBreeds2(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    longtitude2 = db.Column(db.Float, nullable = False)
    latitude2 = db.Column(db.Float, nullable = False)
    breed2 = db.Column(db.String, nullable = False)
    type2 = db.Column(db.String, nullable = False)
    udoy2 = db.Column(db.Float, nullable = False)
    jir2 = db.Column(db.Float, nullable = False)
    belok2 = db.Column(db.Float, nullable = False)
    massa2 = db.Column(db.Float, nullable = False)
    perviy_otel_dney2 = db.Column(db.Float, nullable = False)
    v_otelah2 = db.Column(db.Float, nullable = False)
    vibitiya_v_otelah2 = db.Column(db.Float, nullable = False)
    servis_period2 = db.Column(db.Float, nullable = False)
    suhostoyniy_period2 = db.Column(db.Float, nullable = False)
    vihod_telyat_na100_golov2 = db.Column(db.Float, nullable = False)


    def __repr__(self):
        return '<CowsBreeds2 {}>'.format(self.breed)
