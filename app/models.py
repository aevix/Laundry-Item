from datetime import datetime
from app import db

class Outgoing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(20), index = True)
    item_type = db.Column(db.String(10), index = True)
    item_size = db.Column(db.String(10), index = True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    status = db.Column(db.Boolean(), index=True)

    def __repr__(self):
        return '<Item: {} {} {} {} {}>'.format(self.barcode, self.item_type, self.item_size, self.timestamp, self.status)