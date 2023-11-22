from app import db, login 
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String,DateTime
from datetime  import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Admin(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True)
    password_hash = Column(String(168))
    def _repr_(self):
        return f'<Admin {self.username}'
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Surat(db.Model):
    id = Column(Integer, primary_key=True)
    nomor_surat = Column(String(20))
    tgl_surat = Column(DateTime, default=datetime.now())
    keterangan = Column(String(55))
    url_docx = Column(String(200))


class SuratMasuk(db.Model):
    id = Column(Integer, primary_key=True)
    nomor_surat = Column(String(20))
    tgl_surat = Column(DateTime, default=datetime.now())
    keterangan = Column(String(55))
    url_docx = Column(String(200))


@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))