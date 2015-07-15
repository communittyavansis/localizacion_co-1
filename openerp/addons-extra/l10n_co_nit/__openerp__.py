# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 I.A.S. INGENIERÍA, APLICACIONES Y SOFTWARE Johan Alejandro Olano (<http:http://www.ias.com.co).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Colombian NIT validate location  by I.A.S. INGENIERÍA, APLICACIONES Y SOFTWARE",
    "version": "1.0",
    "description": """
    VALIDACIÓN DE AUTENTICIDAD DEL NIT O RUT (LOCALIZACION COLOMBIANA)
    Collaborators:
   - Johan Alejandro Olano <jolano@ias.com.co>

    """,
    "author": "I.A.S. Ingenieria, Aplicaciones y Software",
    "website": "http://www.ias.com.co",
    "category": "Localization",
    "depends": [
            "base",
		    "base_vat",
			],
	"data":[
		    "views/res_partner_view.xml",
			],
    "demo_xml": [
			],
    "update_xml": [
			],
    "active": False,
    "installable": True,
    "certificate" : "",
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
