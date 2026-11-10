# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# GNU GPLv3 License. See license.txt

from __future__ import unicode_literals

import frappe

no_cache = 1


def get_context(context):
    csrf_token = frappe.sessions.get_csrf_token()
    frappe.db.commit()
    context.csrf_token = csrf_token
    context.site_name = frappe.local.site
    # Insights Settings > Brand Logo; empty keeps the Insights logo
    context.brand_logo = frappe.db.get_single_value("Insights Settings", "brand_logo") or ""
