from app import app 
from flask import render_template, url_for, redirect, flash, send_file
from app.forms import loginform, suratizinform, suratedaranform
from app.models import Admin, Surat
from app.docxTools import BuatDocxFromTemplateIzin, BuatDocxFromTemplateEdaran
from flask_login import login_required, login_user, logout_user, current_user



@app.route("/")
@app.route("/index")
def index ():
    return render_template("index1.html")


@app.route("/login", methods = ['GET','POST'])
def login ():
    form = loginform()
    if (current_user.is_authenticated):
        return redirect(url_for('home'))
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin is None or not admin.check_password(form.password.data):
                flash("Username atau Password Salah!!")
                return redirect(url_for('home'))
        flash("Berhasil Login")
        login_user(admin)
        return redirect(url_for('login'))
    return render_template("login.html", form = form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/daftar")
def daftar ():
    return render_template("daftar.html")


@app.route("/home")
@login_required
def home ():
    return render_template("home.html")


@app.route("/cetak-surat")
@login_required
def cetaksurat ():
    return render_template("cetaksurat.html")


@app.route("/input-surat-masuk")
@login_required
def inputsuratmasuk ():
    return render_template("inputsuratmasuk.html")


@app.route("/pilih-jenis")
@login_required
def opsisurat():
    return render_template("input3.html")


@app.route("/input-surat-keluar/<opsi>", methods=['GET','POST'])
@login_required
def inputsuratkeluar (opsi):
    if opsi == "edaran":
        form = suratedaranform()
        if form.validate_on_submit():
            BuatDocxFromTemplateEdaran(form, current_user.username)
    else:
        form = suratizinform()
        if form.validate_on_submit():
            BuatDocxFromTemplateIzin(form, current_user.username)
    return render_template("input2.html",opsi=opsi, form=form)


@app.route("/arsip-surat-masuk")
@login_required
def suratmasukarsip ():
    return render_template("suratmasukarsip.html")


@app.route("/arsip-surat-keluar")
@login_required
def suratkeluararsip ():
    daftar_surat = Surat.query.all()
    return render_template("suratkeluararsip.html", daftar_surat=daftar_surat)

@app.route("/download/<filename>")
def download(filename):
    return send_file(filename, as_attachment=True, download_name="surat.docx")
