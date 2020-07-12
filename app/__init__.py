import logging
import logging
import threading
import time
from app.models import Base
from app.repositories.ManageOrders import ManageOrders
from app.entities.Integration import Integration

def create_app():
    format_log = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_log, level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")

    page = 1
    while True:
        logging.info(f'Requesting data for API on page {page}')
        payload = {
            'url': 'https://gist.githubusercontent.com/Tinocoo/dc331c5e94028ff37e76cab6b77c8464/raw/9a11cffc9e44dbe427feb74e3d2622ad8e4fa756/preco_certo.json',
            'method': 'GET',
            'params': {
                'page': page,
                'apikey': 123
            }
        }

        integration  = Integration()
        result = integration.send_request(payload)
        if result['result'] == 'success' and result['status'] == 200:
            logging.info('Before creating thread')
            orders = ManageOrders()
            x = threading.Thread(target=orders.get_orders(result))
            logging.info('Before running thread')
            x.start()
            logging.info('Wait for the thread to finish')
            page = 1 if result['data']['paging']['total'] == page else page + 1

            logging.info(f'All ready, the next page will be: {page}')
        
        time_cycle = 60 * 30
        logging.info(f'Next cycle in {time_cycle} seconds')

        time.sleep(time_cycle)
