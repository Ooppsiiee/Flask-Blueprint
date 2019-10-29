from flask import Blueprint, render_template, request, jsonify, url_for, redirect
from .models import DataUser
from . import db
main = Blueprint('main', __name__)




@main.route('/')
def index():
    return render_template('index.html')

@main.route('/', methods=['POST'])
def addRental():
    namaPenyewa = request.form.get('namaPenyewa')
    namaMotor = request.form.get('namaMotor')
    dkMotor = request.form.get('dkMotor')
    tanggalSewa = request.form.get('tanggalSewa')
    abisSewa = request.form.get('abisSewa')

    Data_we_Send = DataUser(namaPenyewa, namaMotor, dkMotor, tanggalSewa, abisSewa, False)
    db.session.add(Data_we_Send)
    db.session.commit()
    data = {
        'namaPenyewa': namaPenyewa,
        'namaMotor': namaMotor,
        'dkMotor': dkMotor,
        'tanggalSewa': tanggalSewa,
        'abisSewa': abisSewa
    }

    return redirect(url_for('main.index'))

@main.route('/list')
def list_avalaible():
    Lists = DataUser.query.filter_by(sudahSelesai=False).all()
    return render_template('list.html', lists=Lists)

@main.route('/list_done')
def list_done():
    Lists = DataUser.query.filter_by(sudahSelesai=True).all()
    return render_template('list_complete.html', lists=Lists)

@main.route('/complete/<id>')
def complete(id):
    userData = DataUser.query.filter_by(id=int(id)).first()
    userData.sudahSelesai = True
    db.session.commit()

    return redirect(url_for('main.list_done '))

