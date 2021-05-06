from flask import Blueprint, request, session, jsonify

from party_control import *


blueprint = Blueprint("auth", __name__)


@blueprint.route('/create_party')
