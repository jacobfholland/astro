from datetime import datetime
from uuid import uuid4
from astro import db
from flask import request


class Base():
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String())
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return str(self.__dict__)

    def create(self, json=None):
        if not json:
            json = request.json
        self.uuid = str(uuid4())
        self.created_at = datetime.now()
        self.bind_attributes()
        db.session.add(self)
        db.session.commit()
        record = self.query.order_by(self.__class__.created_at.desc()).first()
        print(
            f"ASTRO: {self.__class__.__name__} record # {record.id} added succesfully.\n \n")
        return record

    def get_all(self, attr=None):
        if attr:
            records = self.query.order_by(attr).all()
        else:
            records = self.query.all()
        if not records == []:
            print(
                f"ASTRO: {self.__class__.__name__} records found: \n {records}.\n \n")
            return records
        else:
            print(
                f"ASTRO: {self.__class__.__name__} records not found.\n \n")
            return None

    def get(self, id=None):
        if self.id:
            return self
        elif id:
            id = self.validate_int()
            if id:
                return self.query.filter_by(id=id).first()
            else:
                print(
                    f"ASTRO: {self.__class__.__name__} record invalid.\n \n")
                return None
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record not found.\n \n")
            return None

    def update(self, json=None, id=None):
        if not json:
            json = request.json
        if self.id:
            id = self.id
        else:
            id = request.args.get('id')
        record = self.query.filter_by(id=id).first()
        if not record == None:
            record.updated_at = datetime.now()
            record.bind_attributes()
            db.session.commit()
            print(
                f"ASTRO: {self.__class__.__name__} record # {record.id} updated succesfully.\n \n")
            return self.query.order_by(self.__class__.updated_at.desc()).first()
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record id {request.args.get('id')} not found.\n \n")
            return None

    def update_all(self, json=None):
        if not json:
            json = request.json
        records = self.get_all()
        if records == []:
            return None
        for record in records:
            record.update()
        return self.get_all(attr="updated_at")

    def bind_attributes(self, json=None):
        self.updated_at = datetime.now()
        if request.data and request.json:
            for arg in request.json:
                setattr(self, arg, request.json.get(arg))

    def delete(self, id=None):
        if self.id:
            id = self.id
        else:
            id = request.args.get('id')
        record = self.query.filter_by(id=id).first()
        if not record == None:
            record.updated_at = datetime.now()
            db.session.delete(record)
            db.session.commit()
            print(
                f"ASTRO: {self.__class__.__name__} record # {record.id} deleted succesfully.\n \n")
            return self.query.order_by(self.__class__.updated_at.desc()).first()
        else:
            print(
                f"ASTRO: {self.__class__.__name__} record id {request.args.get('id')} not found.\n \n")
            return None

    def delete_all(self):
        records = self.get_all()
        if records == []:
            return None
        temp_records = records
        for record in records:
            record.delete()
        return temp_records

    def validate_int(self, id):
        if isinstance(id, str) and id.isdigit():
            return int(id)
        elif isinstance(id, int):
            return id
        else:
            return None
