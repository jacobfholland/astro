from astro import db
from astro.modules.app.user.models.message import Message


class Notification(Message, db.Model):

    def get(self, id=None):
        record = super().get(id)
        json = {"id": record.id}
        record.update(json=json)
        return super().get(id)


Notification()
