import frappe
import copy

@frappe.whitelist()
def multi_stock_entry(doc):
    stock_en = frappe.get_doc('Stock Entry', doc)

    s_warehouses = {}
    for item in stock_en.items:
        if item.s_warehouse in s_warehouses.keys():
            s_warehouses[item.s_warehouse].append(copy.copy(item))
        else:
            s_warehouses[item.s_warehouse] = [copy.copy(item)]

    for warehouse in s_warehouses:
        n_stock = copy.copy(frappe.get_doc('Stock Entry', doc))
        n_stock.name = ''
        n_stock.items = s_warehouses[warehouse]
        n_stock.save()

    stock_en.delete()
    frappe.db.commit()
    return 'done'
