from astro import db
from astro.base.models.base import Base
from astro.language.seeders.language import languages as seeds


class Language(db.Model, Base):
    name = db.Column(db.String)
    iso_639_1 = db.Column(db.String)
    english_name = db.Column(db.String)
