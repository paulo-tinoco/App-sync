import json
import requests


class Integration(object):

    def converter_response(self, data):
        try:
            result = json.loads(data)
            return {'data': result}
        except Exception as error:
            return {'data': data}

    def send_request(self, params):
        try:
            res = requests.request(**params)
            result = 'success' if res.ok else 'error'
            response = self.converter_response(res.text)
            response.update({'status': res.status_code, 'result': result })
            return response
        except Exception as error:
            return {'data': str(error), 'status': 406, 'result': 'error'}
            