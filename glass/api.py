import frappe
import copy

@frappe.whitelist()
def multi_stock_entry(doc, split_key):
    stock_en = frappe.get_doc('Stock Entry', doc)
    print(split_key)
    split_items = {}
    for item in stock_en.items:
        if item.get(split_key) in split_items.keys():
            split_items[item.get(split_key)].append(copy.copy(item))
        else:
            split_items[item.get(split_key)] = [copy.copy(item)]

    print(split_items)
    for k in split_items:
        n_stock = copy.copy(frappe.get_doc('Stock Entry', doc))
        n_stock.name = ''
        n_stock.items = split_items[k]
        for i in range(len(n_stock.items)):
            n_stock.items[i].idx = i + 1
        n_stock.operation = n_stock.items[0].operation
        n_stock.save()

    stock_en.delete()
    frappe.db.commit()
    return 'done'
