from . import db


class DataUser(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    namaPenyewa = db.Column(db.String(100))
    namaMotor = db.Column(db.String(100))
    dkMotor = db.Column(db.String(100))
    tanggalSewa = db.Column(db.String(100))
    abisSewa = db.Column(db.String(100))
    sudahSelesai = db.Column(db.Boolean)

    def __init__(self, namaPenyewa, namaMotor, dkMotor, tanggalSewa, abisSewa, sudahSelesai):
        self.namaPenyewa = namaPenyewa
        self.namaMotor = namaMotor
        self.dkMotor = dkMotor
        self.tanggalSewa = tanggalSewa
        self.abisSewa = abisSewa
        self.sudahSelesai = sudahSelesai


