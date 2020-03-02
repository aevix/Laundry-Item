from datetime import datetime
from app import db

#Main Laundry tracking table
class Laundry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(20), index = True)
    item_type = db.Column(db.String(10), index = True)
    item_size = db.Column(db.String(10), index = True)
    item_note = db.Column(db.String(20), index = True)
    status = db.Column(db.Boolean(), index=True)

    def __repr__(self):
        return '<Item: {} {} {} {} {}>'.format(self.barcode, self.item_type, self.item_size, self.item_note, self.status)

#Time stamp table that keeps track any time laundry is moved
class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(20), index = True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    status = db.Column(db.Boolean(), index=True)

    def __repr__(self):
        return '<time: {}>'.format(self.timestamp)

#Temporary Search table to create a queue while entering items in or out of the facility
class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(20), index = True)
    item_type = db.Column(db.String(10), index = True)
    item_size = db.Column(db.String(10), index = True)
    item_note = db.Column(db.String(20), index = True)
    status = db.Column(db.Boolean(), index=True)
    
    def __repr__(self):
        return '<Searched: {} {} {} {} {}>'.format(self.barcode, self.item_type, self.item_size, self.item_note, self.status)