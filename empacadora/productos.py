# -*- coding: utf-8 -*-
from odoo import models,fields


class productos(models.Model):
    _name = 'empacadora.productos'

    socio_id = fields.Many2one('empacadora.socios',string='Socio')
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    stock = fields.Integer(string="cantidad")
    unidad_medida = fields.Selection([('tons','Toneladas'),('kg','Kilogramos'),('gr','gramos')],string='Ingreso')
    
    _order = 'socio_id,name'

    _sql_constraints = [('productos_uniq', 'unique(socio_id,producto_id)', 'producto duplicado, intenta con otro...'),]
    
    
        
        