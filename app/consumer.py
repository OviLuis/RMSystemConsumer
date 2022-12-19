import sys
import requests
import datetime as dt


class Consumer:

    def __init__(self, connection):
        self.connection = connection

    def get_data(self):
        last_id = 0
        sleep_ms = 5000
        while True:
            try:
                resp = self.connection.xread(
                    {'RMSystem': last_id}, count=1, block=sleep_ms
                )
                if resp:
                    key, messages = resp[0]
                    last_id, data = messages[0]
                    print("REDIS ID: ", last_id)
                    print("      --> ", data)
                    parsed_data = {key.decode(): val.decode() for key, val in data.items()}

                    measure_data = {
                        'device_id': parsed_data.get('device_id'),
                        'measure_value': round(float(parsed_data.get('measure_value')), 2),
                        'measure_unit': parsed_data.get('measure_unit'),
                        'measure_date': parsed_data.get('measure_date')
                    }
                    self.record_data(measure_data)

            except ConnectionError as e:
                print("ERROR REDIS CONNECTION: {}".format(e))
            except Exception as e:
                print('ERROR NO CONTROLADO: {}'.format(str(e)))
                sys.exit()

    def record_data(self, data):
        url = 'http://microserviceapi:8000/api/measures/'

        req = requests.post(url=url, data=data, timeout=60, verify=False)
        print(req.status_code)
        if req.status_code != 201:
            print('ERROR AL REGISTRAR MEDICION: {}'.format(req.text))
        else:
            print('Registro almanenado correctamente: {}'.format(req.text))
