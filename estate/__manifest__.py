{
  'name':'estate',
  'description':'Real state module description',

  'depends': ['website','base'],

  'data':[
           'security/ir.model.access.csv',
           'views/properties_menu.xml',
           'views/templates.xml',
           'views/estate_property_views.xml',
           'views/estate_property_views_tags.xml',
           'views/estate_property_views_offer.xml',
           'views/estate_property_views_type.xml',
           'views/estate_menus.xml',
           'views/res_users_views.xml',
           'reports/estate_property_reports.xml',
           'reports/estate_property_templates.xml',
  ],
   "images":['static/image/p1.jpeg',],

}
