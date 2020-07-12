from datetime import datetime
from app.entities.Integration import Integration
from app.models.Orders import Orders
from app.models.Products import Products
from app.repositories import session


class ManageOrders(Integration):

    def get_orders(self, data):
        for row in data['data']['Orders']:
            order = row['Order']
            products = order['ProductsSold']
            order.pop('ProductsSold')

            order.update({
                'date': datetime.strptime(order['date'], '%Y-%m-%d'),
                'modified': datetime.strptime(order['modified'], '%Y-%m-%d %H:%M:%S')
            })

            self.upinsert_data(Orders, order, {'id': order['id']})
            for product in products:
                self.upinsert_data(Products, product['ProductsSold'], {'id': product['ProductsSold']['id']})

    def upinsert_data(self, model, params, search={}):
        try:
            # Try to insert
            data = model(**params)
            session.add(data)
            session.commit()
            return {'data': 'successfully inserted', 'status': 201}
        except Exception as error:
            # Rollback to insert
            session.rollback()

            # Update data
            session.query(model).filter_by(**search).update({k: v for k, v in params.items() if v is not None})
            session.commit()
            return {'data': 'successfully updated', 'status': 200}
        finally:
            # Close the session
            session.close()
            