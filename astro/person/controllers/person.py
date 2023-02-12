from astro.person.models.person import Person


class PersonController:

    def create(self):
        return Person().create()

    def get_all(self):
        return Person().get_all()

    def get(self):
        return Person().get()

    def delete_all(self):
        return Person().delete_all()

    def delete(self):
        return Person().delete()

    def update_all(self):
        return Person().update_all()

    def update(self):
        return Person().update()

    def select(self):
        return Person().select()

    def search(self):
        return Person().search()

    def tmdb_import(self):
        return Person().tmdb_import()