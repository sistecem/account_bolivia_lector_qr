# -*- coding: utf-8 -*-
from psycopg2 import sql, DatabaseError
from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
import re

# from odoo.exceptions import ValidationError
class account_bolivia_lector_qr(models.Model):
    _name = 'account_bolivia_lector_qr.account_bolivia_lector_qr'
    _description = 'account_bolivia_lector_qr.account_bolivia_lector_qr'

    name = fields.Char(string='QR')
    date = fields.Date(string='Fecha Escaneada', default=datetime.today())
    autorizacion = fields.Char()
    nit = fields.Char(string="Nit")
    invoice_date = fields.Date(string="Fecha Factura")
    ref = fields.Char(string="#Num")
    codigodecontrol = fields.Char(string="CodControl")
    nit_compania = fields.Char(string="NIT")
    total = fields.Float()
    descuentos = fields.Float()


    # _sql_constraints = [
    #     ('name_unique',
    #      'UNIQUE(name)',
    #      'Duplicado! este QR ya fue registrado'),
    # ]

    @api.onchange('name')
    def _split_name(self):
        for r in self:
            if r.name :
                if 'siat.impuestos' in r.name :
                    # re = re.findall('nit=(.)&', r.name)
                    r.nit = "Test"
                else:
                    partes = r.name.split('|')

                    ajuste = 12-len(partes)

                    if ajuste > 1:
                        raise ValidationError('Hacer Manual, Error en QR')

                    # print(partes)
                    # print(partes[0])
                    r.nit = partes[0]
                    if len(partes)>1:
                        r.ref = partes[1-ajuste]
                        r.autorizacion = partes[2-ajuste]
                        try:
                            r.invoice_date = partes[3-ajuste]
                        except:
                            try:
                                r.invoice_date = datetime.strptime(partes[3-ajuste], '%d/%m/%Y')
                            except:
                                try:
                                    r.invoice_date = datetime.strptime(partes[3-ajuste], '%d/%m/%y')
                                except:
                                    try:
                                        r.invoice_date = datetime.strptime(partes[3-ajuste], '%m/%d/%y')
                                    except:
                                        try:
                                            r.invoice_date = datetime.strptime(partes[3-ajuste], '%m/%d/%Y')
                                        except:
                                            r.invoice_date = ""
                                            # raise ValidationError('Error con la Fecha')
                        try:
                            r.total = partes[4-ajuste]
                        except:
                            try:
                                r.total = partes[4 - ajuste] #FALTA probar con coma decimal o punto decimal
                            except:
                                pass

                        try:
                            r.total = partes[5-ajuste]
                        except:
                            try:
                                r.total = partes[5 - ajuste] #FALTA probar con coma decimal o punto decimal
                            except:
                                pass
                            # con descuento? r.total = partes[6]
                        r.codigodecontrol = partes[6 - ajuste]
                        r.nit_compania = partes[7 - ajuste]
                        #siempre 0? r. = partes[8]
                        #siempre 0? r. = partes[9]
                        #siempre 0? r. = partes[10]
                        #siempre 0? r. = partes[11]

                    else:
                        raise ValidationError('Error al Leer el código')

    @api.constrains('name')
    def _check_unique_name(self):
        for r in self:
            qr = self.env['account_bolivia_lector_qr.account_bolivia_lector_qr'].search([('id','!=', r.id),('name', '=', r.name)])
            if qr :
                raise ValidationError('Duplicado! este QR ya fue registrado')


class AccountMove(models.Model):
    # Hereda todo y modifica
    _inherit = 'account.move'

    lector_qr = fields.Char()
    total_qr_referencial = fields.Float()

    selector_qr = fields.Many2one(
        'account_bolivia_lector_qr.account_bolivia_lector_qr', 'Selector QR',
        readonly=False)


    @api.onchange('selector_qr')
    def _change_selector(self):
        for r in self:
            r.lector_qr = r.selector_qr.name


    @api.onchange('lector_qr','selector_qr')
    def _split_qr(self):
        for r in self:
            if r.lector_qr:
                if 'siat.impuestos' in r.lector_qr:
                    # re = re.findall('nit=(.)&', r.lector_qr)
                    r.nit = "Test"
                else:
                    partes = r.lector_qr.split('|')

                    ajuste = 12 - len(partes)

                    if ajuste > 1:
                        raise ValidationError('Hacer Manual, Error en QR')


                    r.nit = partes[0]
                    if len(partes) > 1:
                        r.ref = partes[1 - ajuste]
                        r.autorizacion = partes[2 - ajuste]
                        try:
                            r.invoice_date = r.date = partes[3 - ajuste]
                        except:
                            try:
                                r.invoice_date = r.date = datetime.strptime(partes[3 - ajuste], '%d/%m/%Y')
                            except:
                                try:
                                    r.invoice_date = r.date = datetime.strptime(partes[3 - ajuste], '%d/%m/%y')
                                except:
                                    try:
                                        r.invoice_date = r.date = datetime.strptime(partes[3 - ajuste], '%m/%d/%y')
                                    except:
                                        try:
                                            r.invoice_date = r.date = datetime.strptime(partes[3 - ajuste], '%m/%d/%Y')
                                        except:
                                            r.invoice_date = ""
                                            r.date = ""
                                            # raise ValidationError('Error con la Fecha')
                        try:
                            r.total_qr_referencial = partes[4 - ajuste]
                        except:
                            try:
                                r.total_qr_referencial = partes[4 - ajuste]  # FALTA probar con coma decimal o punto decimal
                            except:
                                pass

                        try:
                            r.total_qr_referencial = partes[5 - ajuste]
                        except:
                            try:
                                r.total_qr_referencial = partes[5 - ajuste]  # FALTA probar con coma decimal o punto decimal
                            except:
                                pass
                            # con descuento? r.total = partes[6]
                        r.codigodecontrol = partes[6 - ajuste]
                        #REVISAR SI NIT CUADRAr.codigodecontrol = partes[7 - ajuste]
                        # siempre 0? r. = partes[8]
                        # siempre 0? r. = partes[9]
                        # siempre 0? r. = partes[10]
                        # siempre 0? r. = partes[11]

