{
    'name': 'Test theme',
    'description': 'This is my first theme',
    'version': '1.0',
    'author': 'Divyesh vyas',
    'category': 'Theme/creative',
    'depends': ['website'],

    'data': [
        'views/assets.xml',
        'views/layout.xml',
        'views/pages.xml',
        'views/snippets.xml',
        'views/options.xml'

    ],
    'assets': {
        'web.assets_frontend': [
            'theme_test/static/scss/style.scss',
        ],
        'website.assets_editor':[
            'theme_test/static/test_editor.js'
        ]
        
    }
}
