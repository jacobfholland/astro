from flask import Blueprint
from flask_login import login_required
from astro import to_json
from astro.user.models.user import User
from astro.base.controllers.base import BaseController
from astro.user.controllers.user import UserController
user = Blueprint("user", __name__)


@user.route("/create", methods=["POST"])
def create():
    return to_json(BaseController(User()).create())


@user.route("/register", methods=["POST"])
def register():
    return to_json(UserController().register())


@user.route("/login", methods=["POST"])
def login():
    return to_json(UserController().login())


@user.route("/logout", methods=["POST"])
def logout():
    return to_json(UserController().logout())


@user.route("/factory", methods=["POST"])
def factory():
    return to_json(UserController().factory())


@user.route("/current", methods=["GET"])
def current():
    return to_json(UserController().current())


@user.route("/get/all", methods=["GET"])
def get_all():
    return to_json(BaseController(User()).get_all())


@user.route("/get", methods=["GET"])
def get():
    return to_json(BaseController(User()).get())


@user.route("/comments", methods=["GET"])
def comments():
    return to_json(UserController().comments())


@user.route("/delete/all", methods=["DELETE"])
@login_required
def delete_all():
    return to_json(BaseController(User()).delete_all())


@user.route("/delete", methods=["DELETE"])
@login_required
def delete():
    return to_json(BaseController(User()).delete())


@user.route("/update/all", methods=["PATCH"])
@login_required
def update():
    return to_json(BaseController(User()).update_all())


@user.route("/update", methods=["PATCH"])
@login_required
def update_all():
    return to_json(BaseController(User()).update())
