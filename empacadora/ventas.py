# -*- coding: utf-8 -*-
from odoo import models,fields, api
from odoo.exceptions import UserError
from datetime import datetime
import random



class ventas(models.Model):
    _name = 'empacadora.ventas'
    _description = 'venta del producto'
    
    socio_id = fields.Many2one('empacadora.socios', string='socio')
    id_producto = fields.Many2one('empacadora.productos' , string='Producto')
    fecha =  fields.Date(string='Fecha', default=fields.Date.today(), required=True)
    direccion = fields.Char(string='Direción', required=True)
    type_client = fields.Selection([('seller','Vendedor'),('buyer','comprador'),('both','comprador/vendedor')],string='Tipo Cliente', required="True")
    cantidad = fields.Float(string='Cantidad tons ', required=True)
    precio_unitario = fields.Float(string='Precio Unitario', required=True)
    precio_venta = fields.Float(string='Cantidad venta tons ', required=True)
    total_venta =fields.Float(string='Total de venta', compute='_compute_total')
    state = fields.Selection([('cre','Creado'),('env','Enviada'),('can','Cancelado')],string='Estado',readonly=True, default='cre', required="True")
    folio = fields.Char(string='Folio', size=12)
    
    _order = 'socio_id, id_producto'
    
   
    """
    generea el resultado de la venta
    """

    @api.depends('cantidad', 'precio_venta')
    def _compute_total(self):
        for record in self:
            record.total_venta = ((record.cantidad * 1000) * record.precio_venta)
            
            
            
        
    @api.model
    def generar_folio(self):
       
        secuencia = self.search_count([]) + 1
        fecha_actual = fields.Date.today().strftime('%Y%m%d')
        folio = f"{fecha_actual}{secuencia:06d}"
        while self.search_count([('folio', '=', folio)]) > 0:
            secuencia += 1
            folio = f"{fecha_actual}{secuencia:06d}"
        return folio
    
    """
        Crea un registro del modelo con un número de folio único de 12 dígitos.
    """
            
    @api.model
    def create(self, vals):
       
        if not vals.get('folio'):
            vals['folio'] = self.generar_folio()
        return super().create(vals)

    
   
            
     
    
    

    
            
            
    def registrar(self):
        raise UserError('Cambiar status')
