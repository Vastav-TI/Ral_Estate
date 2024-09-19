{
    'name': 'Real Estate Management',
    'version': '17.0.1.0',
    'category': 'Real Estate',
    'summary': 'Manage Real Estate Properties, Sales, and Customers',
    'description': """
        This module provides features for managing real estate properties, including property listings, customer details, and sales information. It inherits functionality from `res.partner`, `sale`, and `product` models.
    """,
    'author': 'Vatsav Taneja',
    'depends': ['base', 'sale', 'product', 'contacts'],
    'data': [
        # Data files like views, actions, and security
        'security/ir.model.access.csv',
        'views/wizard_property_action_views.xml',
        'views/save_Default_view.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/client_view.xml',
        'views/tenant.xml',
        'views/sale_view.xml',
        'views/menu.xml',

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
