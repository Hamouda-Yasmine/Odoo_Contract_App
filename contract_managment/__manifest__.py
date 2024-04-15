{
    'name': 'Contract Management',
    'description': ' contract management for buildings',
    'version': '1.0',
    'category': 'Administration',
    'depends': ['base', 'base_address_extended', 'sale', 'sale_management'],
    'data': ["views/contract_managment_menus.xml", "views/project_view.xml", "security/ir.model.access.csv", "views/building_view.xml", "views/project_view.xml", "views/contract_view.xml","views/sale_order_view.xml","views/unit_view.xml"],
    'application': True,

}
