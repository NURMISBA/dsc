from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
# innary tens
class loginform(FlaskForm):
    username = StringField("username")
    password = PasswordField("password")
    submit = SubmitField("login")


class suratizinform(FlaskForm):
    program_studi = StringField("Program Study")
    fakultas = StringField("Fakultas")
    kontak = StringField("Kontak")
    nosurat = StringField("No. Surat")
    lampiran = StringField("Lampiran")
    hal = StringField("Hal")
    kepada = StringField("Kepada")
    tempat = StringField("Tempat")
    isi = StringField("Isi")
    hari = StringField("Hari")
    waktu = StringField("Waktu")
    tempat_1 = StringField("Tempat")
    penutup = StringField("Penutup")
    lokasi = StringField("Lokasi")
    date = StringField("Date")
    ketua_program = StringField("Ketua Program")
    ttd = StringField("TTD")
    nama_ketua = StringField("Nama Pimpinan")
    nidn = StringField("NIDN")
    submit = SubmitField("Buat Surat")


class suratedaranform(FlaskForm):
    program_studi = StringField("Program Study")
    fakultas = StringField("Fakultas")
    kontak = StringField("Kontak")
    nosurat = StringField("No. Surat")
    lampiran = StringField("Lampiran")
    hal = StringField("Hal")
    kepada = StringField("Kepada")
    tempat = StringField("Tempat")
    isi = StringField("Isi")
    penutup = StringField("Penutup")
    lokasi = StringField("Lokasi")
    date = StringField("Date")
    ketua_program = StringField("Ketua Program")
    ttd = StringField("TTD")
    nama_ketua = StringField("Nama Pimpinan")
    nidn = StringField("NIDN")
    submit = SubmitField("Buat Surat")