BASE_URL = 'https://example.com'
urls = {
    'home': BASE_URL,
    'login': {
        'page':        BASE_URL + '/login',
        'success':     BASE_URL + '/?sess=<SESS>',
        'fail':        BASE_URL + '/login?msg=fail',
        'invalid':     BASE_URL + '/login?msg=invalid'
    }
}