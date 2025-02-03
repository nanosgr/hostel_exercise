from odoo import api, fields, models

class HostelRoom(models.Model):
    _name = 'hostel.room'
    _description = 'Hostel Room'

    currency_id = fields.Many2one('res.currency', string='Currency')
    rent_amount = fields.Monetary('Rent Amount', help="Enter rent amount per month")
