from models import Distro
from flask import jsonify, Blueprint, request
from extensions import db


bp = Blueprint('api', __name__)

@bp.route('/distros', methods=['GET'])
def get_distros():
    distros = Distro.query.all()
    return jsonify([d.to_dict() for  d in distros])

@bp.route('/distros/<int:id>', methods=['GET'])
def get_single(id):
    distro = Distro.query.get_or_404(id)
    return jsonify(distro.to_dict())


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

@bp.route('/distros/<int:id>', methods=['PUT'])
def update_distro(id):
    distro = Distro.query.get_or_404(id)
    data = request.json

    distro.name = data.get('name', distro.name)
    distro.based_on = data.get('based_on', distro.based_on)
    distro.release_date = data.get('release_date', distro.release_date)
    distro.version = data.get('version', distro.version)
    distro.developers = data.get('developers', distro.developers)

    db.session.commit()

    return jsonify(distro.to_dict())



@bp.route('/distros/<int:id>', methods=['DELETE'])
def delete_distro(id):
    distro = Distro.query.get_or_404(id)
    db.session.delete(distro)
    db.session.commit()

    return jsonify({"message": "Distribution deleted successfully"}) 