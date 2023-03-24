{
	'name':'Franchise Manager',
	'summary':'Hey! I am your showroom manager, Lets have a managed showroom',
    'depends':['website'],
    'data':[
		'security/ir.model.access.csv', 
        
        'views/website_template.xml',
		'views/franchise_store_property_view.xml',
        'views/franchise_product_type_view.xml',
        'views/franchise_product_view.xml',
        'views/franchise_product_order_view.xml',
		'views/franchise_product_stock_view.xml',
		'views/franchise_menus.xml',
	]

}