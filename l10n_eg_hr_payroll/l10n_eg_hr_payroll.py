# -*- coding:utf-8 -*-

from openerp import fields, models
import openerp.addons.decimal_precision as dp


class HRContractEg(models.Model):
    _inherit = 'hr.contract'
    
    variable_amount = fields.Float(string='Insurance Variable Salary', digits=dp.get_precision('Payroll'), default=0.0)
    commission_amount = fields.Float(string='Commissions', digits=dp.get_precision('Payroll'), default=0.0)
    mobile_amount = fields.Float(string='Mobile', digits=dp.get_precision('Payroll'), default=0.0)
    meal_amount = fields.Float(string='Meal', digits=dp.get_precision('Payroll'), default=0.0)
    transportation_amount = fields.Float(string='Transportation', digits=dp.get_precision('Payroll'), default=0.0)
    non_taxable_amount = fields.Float(string='Non Taxable Allowance', digits=dp.get_precision('Payroll'), default=0.0)
    other_taxable_amount = fields.Float(string='Taxable Allowance', digits=dp.get_precision('Payroll'), default=0.0)
    social_allowance_amount = fields.Float(string='Social Allowance', digits=dp.get_precision('Payroll'), default=0.0)

# class HREmployeeEg(models.Model):
#     _inherit = 'hr.employee'
