{
    'name':'Theme Tutorial',
    'description':'A description for your theme',
    'version':'1.0',
    'author':'XYZ',
    'category':'Theme/Creative', #category/subcategory
    'depends':['website',],
    'data':[
        'views/assets.xml',
        'views/layout.xml',
        'views/pages.xml',
    ],  
    'assets': {
        'web.assets_frontend': [
            'theme_tutorial/static/scss/style.scss',
        ],
        'web._assets_primary_variables':[
            'theme_tutorial/static/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers':[
            'theme_tutorial/static/scss/primary_variables.scss',
        ]
    }
}