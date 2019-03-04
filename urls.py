BASE_URL = 'https://example.com'
urls = {
    'home': BASE_URL,
    'login': {
        'success': BASE_URL + '/?sess=<SESS>',
        'fail': BASE_URL + '/login?fail=fail'
    }
}