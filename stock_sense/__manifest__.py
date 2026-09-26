{
    'name': 'Stock Sense',
    'version': '1.0',
    'summary': 'Smart low stock alerts for products',
    'category': 'Inventory',
    'depends': ['product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_stock_views.xml',
    ],
    'installable': True,
    'application': True,
}