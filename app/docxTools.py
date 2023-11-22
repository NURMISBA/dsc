from docxtpl import DocxTemplate
from app import db
from app.models import Surat
import os


def formToDict(form):
    data = {}
    for isi in form:
        if isi.name == "submit":
            break
        data[isi.name] = isi.data
    print(len(data))
    return data       


def BuatDocxFromTemplateIzin(data, user):
    data = formToDict(data)
    curpath = os.path.join(os.getcwd(), "app/")
    namauser = user.replace(" ","_")
    fn = data['nosurat'].replace("/","_")
    path_hasil = f"{curpath}static/docxhasil/{fn}.docx"
    nama_file = 'static/tplDocx/surat_izin.docx'
    # if not os.path.exists(f"{curpath}static/docxhasil"):
    #     os.mkdir(f"{curpath}static/docxhasil")
    docxFile = DocxTemplate(os.path.join(curpath,nama_file))
    docxFile.render(data)
    docxFile.save(os.path.join(curpath, path_hasil))
    surat = Surat(nomor_surat=data['nosurat'], keterangan=data['fakultas'], url_docx=f"{fn}.docx")
    db.session.add(surat)
    db.session.commit()


def BuatDocxFromTemplateEdaran(data, user):
    data = formToDict(data)
    curpath = os.path.join(os.getcwd(), "app/")
    namauser = user.replace(" ","_")
    fn = data['nosurat'].replace("/","_")
    path_hasil = f"{curpath}static/docxhasil/{fn}.docx"
    nama_file = 'static/tplDocx/surat_edaran.docx'
    # if not os.path.exists(f"{curpath}static/docxhasil"):
    #     os.mkdir(f"{curpath}static/docxhasil/{namauser}")
    docxFile = DocxTemplate(os.path.join(curpath,nama_file))
    docxFile.render(data)
    docxFile.save(os.path.join(curpath, path_hasil))
    surat = Surat(nomor_surat=data['nosurat'], keterangan=data['fakultas'], url_docx=f"{fn}.docx")
    db.session.add(surat)
    db.session.commit()
