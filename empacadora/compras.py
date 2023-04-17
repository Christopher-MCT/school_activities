# -*- coding: utf-8 -*-
import random
from odoo import models,fields, api
from datetime import datetime
from odoo.exceptions import UserError

class compras (models.Model):
    
    _name = 'empacadora.compras'
    _description = 'Compras de productos'
  

    socio_id = fields.Many2one('empacadora.socios', string='socio')
    id_producto = fields.Many2one('empacadora.productos' , string='Producto')
    fecha = fields.Date(string='Fecha', default=fields.Date.today(), required=True)
    
    cantidad = fields.Float(string='Cantidad tons ', required=True)
    precio_unitario = fields.Float(string='Precio Unitario', required=True)
    total = fields.Float(string='Total', compute='_compute_total')
    state = fields.Selection([('cre','Creado'),('env','Enviada'),('can','Cancelado')],string='Estado',readonly=True, default='cre', required="True")
    _order = 'socio_id, id_producto'

    def registrar(self):
        raise UserError('Cambiar status')
   

    @api.depends('cantidad', 'precio_unitario')
    def _compute_total(self):
        for record in self:
            record.total = ((record.cantidad * 1000 )* record.precio_unitario)
            
    


