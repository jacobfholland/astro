from flask import Blueprint
from flask_login import login_required
from astro.modules.app.utils.functions.utils import to_json
from astro.modules.custom.genre.models.genre import Genre
from astro.modules.app.base.controllers.base import BaseController
from astro.modules.custom.genre.controllers.genre import GenreController

genre = Blueprint("genre", __name__)


@genre.route("/create", methods=["POST"])
@login_required
def create():
    return to_json(BaseController(Genre()).create())


@genre.route("/seed", methods=["POST"])
@login_required
def seed():
    return to_json(GenreController().seed())


@genre.route("/get/all", methods=["GET"])
def get_all():
    return to_json(BaseController(Genre()).get_all())


@genre.route("/get", methods=["GET"])
def get():
    return to_json(BaseController(Genre()).get())


@genre.route("/delete/all", methods=["DELETE"])
@login_required
def delete_all():
    return to_json(BaseController(Genre()).delete_all())


@genre.route("/delete", methods=["DELETE"])
@login_required
def delete():
    return to_json(BaseController(Genre()).delete())


@genre.route("/update/all", methods=["PATCH"])
@login_required
def update():
    return to_json(BaseController(Genre()).update_all())


@genre.route("/update", methods=["PATCH"])
@login_required
def update_all():
    return to_json(BaseController(Genre()).update())