from odoo import models, fields

class Buku(models.Model):
    _name = 'om.buku'
    _description = 'Data Buku'

    name = fields.Char(string="Judul Buku")
    penulis = fields.Char(string="Penulis")
    tahun_terbit = fields.Integer(string="Tahun Terbit")
