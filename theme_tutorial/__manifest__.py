{
    'name': 'Tutorial theme',
    'description': 'A description for your theme.',
    'version': '1.0',
    'author': 'Your name',
    'category': 'Theme/Creative',

    'depends': ['website'],
    'data': [
        'views/assets.xml',
        'views/layout.xml',
        'views/pages.xml'
    ],
    'assets': {
        'web.assets_frontend': [          
            'theme_tutorial/static/scss/style.scss'
        ]
    }
}