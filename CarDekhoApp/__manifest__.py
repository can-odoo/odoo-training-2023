{
  'Name':'Car App Module',
  'Description':'This is Car Dekho App Module',
  'version': '1.0',
  'category': 'App/CRM',
  'sequence': 25,
  'summary': 'carDekho',
  'description': "Finds car on cheapest price and beautiful look",
  'depends': ['website','base'],
  'data':[
         'security/ir.model.access.csv',
         'views/template.xml',
         'views/carList_menu.xml',
         'wizard/cardekho_wizard_view.xml',
         'views/cardekho_details_views.xml',
         'views/cardekho_offer_view.xml',
         'views/cardekho_type_view.xml',
         'views/cardekho_tag_view.xml',
         'views/cardekho_menus.xml',
         'views/res_users_views.xml',
         
  ]
}
