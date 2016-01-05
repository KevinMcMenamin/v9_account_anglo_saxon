# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013- Solnet Solutions (<http://www.solnetsolutions.co.nz>).
#    Copyright (C) 2010 OpenERP S.A. http://www.openerp.com
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Account Anglo Saxon",
    "version": "1.0",
    "depends": ["base", "account", "stock",
                "purchase", "sale"],
    "author": "Solnet Solutions Ltd",
    "website": "http://www.solnetsolutions.co.nz",
    "category": "Accounting",
    "description": ("Provides additional functionality to manage use cases not provided by Odoo. See also account_stock_return"),
    "data": [],
    "update_xml": [],
    "demo": [],
    "test": [],
    "installable": True,
    "active": False
}

#    Use cases covered:
#     - financial invoice / credit for a supplier - code lines to expense account as will not have any stock moves
