{
    'name': 'Book Reading Tracker',
    'version': '1.0',
    'summary': 'Track which days you read books, GitHub-style',
    'category': 'Productivity',
    'depends': ['base', 'website'],  # ⬅️ pastikan 'website' ada karena pakai template web
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/reading_day_views.xml',
        'templates/dashboard.xml',  # ⬅️ ini yang sebelumnya hilang
    ],
    'qweb': [
        'templates/dashboard.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
