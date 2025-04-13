from odoo import models, fields, api

class ReadingDay(models.Model):
    _name = 'book.reading.day'
    _description = 'Reading Checkpoint'

    date = fields.Date(string='Reading Date', required=True, default=fields.Date.today)
