BASE_URL = 'https://example.com'
urls = {
    'home': BASE_URL,
    'login': {
        'page':        BASE_URL + '/login',
        'logout':      BASE_URL + '/login?msg=logout',
        'success':     BASE_URL + '/?sess=<SESS>',
        'fail':        BASE_URL + '/login?msg=fail',
        'invalid':     BASE_URL + '/login?msg=invalid',
        'insuf':       BASE_URL + '/?msg=insufficient',
        'why':         BASE_URL + '/err?msg=You%20are%20not%20supposed%20to%20be%logged%20in%20to%20perform%20this%20action.%20Please%20logout.',
        'created':     BASE_URL + '/login?msg=created',
        'granted':     BASE_URL + '/?msg=granted'
    },
    'input': {
        'illegal': {
            'chars':   BASE_URL + '/err?msg=%23ERROR%0AIllegal%20input.%20Alphanumeric%20chacters%20only.',
            'absent':  BASE_URL + '/err?msg=%23ERROR%0ANot%20all%20required%20parameters%20present.%20This%20is%20probably%20Frontend%27s%20fault.'
        }
    }
}