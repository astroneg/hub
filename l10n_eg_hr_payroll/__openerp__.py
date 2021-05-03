# -*- encoding: utf-8 -*-

{
    'name': 'Egypt - Payroll',
    'category': 'Localization',
    'author': 'Khaled Hamed',
    'depends': ['hr','hr_payroll','hr_contract','hr_attendance'],
    'version': '1.0',
    'summary': "HR Payroll rules for Egypt country as per latest tax and insurance laws 2015/2016",
    'description': """
Egypt Payroll Rules as per last rules 2015/2016.
======================

    * Employee Details
    * Social insurance based Contract
    * Income taxes based on new Egypt tax rules 08/2015
    * Insurance rules as per 01/2016 amendments.
    * Allowances/Deductions
    * Allow to configure Basic/Gross/Net Salary
    * Employee Payslip
    * Salary, Meal, Transportation, Tax, Allowance, ...

    """,
    'license': 'AGPL-3',
    'auto_install': False,
    'website': 'https://www.grandtk.com',
    'data': [
        'l10n_eg_hr_payroll_view.xml',
        'data/l10n_eg_hr_payroll_data.xml',
    ],
    'installable': True,
    'price': 40,
    'currency': 'EUR',
}
