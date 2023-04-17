# -*- coding: utf-8 -*-
from odoo import models,fields




class ligas(models.Model):
    _name = 'empacadora.socios'

    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Logo')
    direccion = fields.Char(string='Direción', required="True")
    type_client = fields.Selection([('seller','Vendedor'),('buyer','comprador'),('both','comprador/vendedor')],string='Tipo Cliente', required="True")
    celular= fields.Char(string="Numero cel", required="True")
    cp= fields.Char(string="codigo postal")
    localidad = fields.Char(string='Localidad', required="True")
    producto_id = fields.Many2one('empacadora.productos',string='Producto')

    
    _order = 'name, producto_id'
    
   


