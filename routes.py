from models import Distro
from flask import jsonify, Blueprint, request
from extensions import db


bp = Blueprint('api', __name__)

@bp.route('/distros', methods=['GET'])
def det_distros():
    distros = Distro.query.all()
    return jsonify([d.to_dict() for  d in distros])


@bp.route('/distros', methods=['POST'])
def create_distro():
    data = request.json

    new_distro = Distro(
        name=data.get("name"),
        based_on=data.get("based_on"),
        release_date=data.get("release_date"),
        version=data.get("version"),
        developers=data.get("developers"),
        image=data.get("image")
    )

    db.session.add(new_distro)
    db.session.commit()

    return jsonify(new_distro.to_dict()), 201