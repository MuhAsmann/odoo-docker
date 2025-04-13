{
    'name': 'Book Reading Tracker',
    'version': '1.0',
    'summary': 'Track which days you read books, GitHub-style',
    'category': 'Productivity',
    'depends': ['base'],
    'data': [
        'views/menu.xml',
        'views/reading_day_views.xml',
    ],
    'qweb': [
        'templates/dashboard.xml',
    ],
    'installable': True,
    'application': True,
}
