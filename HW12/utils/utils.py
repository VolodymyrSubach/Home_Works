from requests import request


def get_json():
    url = ' https://bitpay.com/api/rates'
    try:
        response = request('GET', url)
    except:
        print('Exception')
    else:
        if 300 > response.status_code >= 200 and response.headers.get('Content-Type') == \
                    'application/json; charset=utf-8' and response.json() != []:
            resp_json = response.json()
        else:
            return TypeError

        return resp_json




