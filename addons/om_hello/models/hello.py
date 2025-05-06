from odoo import models, fields

class Hello(models.Model):
    _name = 'om.hello'
    _description = 'Hello World Module'

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address")
