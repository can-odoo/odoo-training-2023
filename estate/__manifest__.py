{
	'name':'Real Estate',
	'summary': 'Track leads and close opportunities',
	'version' : '1.2',
	'depends':['website'],
    'data':[
		'security/ir.model.access.csv', 
        
        'wizard/estate_property_wizard_view.xml',
		'views/estate_property_view.xml',
        'views/estate_property_offer_view.xml',
		'views/estate_property_type_view.xml',
		'views/estate_property_tag_view.xml',
        'views/res_users_view.xml',
        'views/website_template.xml',
        'report/estate_property_report.xml',
        'report/estate_property_template.xml',
        'report/res_user_report.xml',
        'report/res_user_template.xml'
		# 'views/estate_menus.xml'
	],
    'application' : True

}