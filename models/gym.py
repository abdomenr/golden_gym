from odoo import models, fields

class Gym(models.Model):
    _name = 'gym.gym'
    _description = 'Gym'

    name = fields.Char(string='Name', required=True)
    address = fields.Text(string='Address')
    members = fields.One2many('gym.member', 'gym_id', string='Members')

class Member(models.Model):
    _name = 'gym.member'
    _description = 'Member'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    dob = fields.Date(string='Date of Birth')
    gym_id = fields.Many2one('gym.gym', string='Gym')

class Membership(models.Model):
    _name = 'gym.membership'
    _description = 'Membership'

    member_id = fields.Many2one('gym.member', string='Member', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date')
    amount = fields.Float(string='Amount')
