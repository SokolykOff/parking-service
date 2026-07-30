from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Client, Parking, ClientParking
from datetime import datetime, timezone

bp = Blueprint("api", __name__, url_prefix="/")


@bp.route("/clients", methods=["GET"])
def get_clients():
    clients = Client.query.all()
    return jsonify({"clients": [c.to_dict() for c in clients]})


@bp.route("/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
    client = db.session.get(Client, client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404
    return jsonify({"client": client.to_dict()})


@bp.route("/clients", methods=["POST"])
def create_client():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if not data.get("name") or not data.get("surname"):
        return jsonify({"error": "name and surname are required"}), 400

    client = Client(
        name=data["name"],
        surname=data["surname"],
        credit_card=data.get("credit_card"),
        car_number=data.get("car_number"),
    )
    db.session.add(client)
    db.session.commit()

    return jsonify({"client": client.to_dict()}), 201


@bp.route("/parkings", methods=["POST"])
def create_parking():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if not data.get("address") or not data.get("count_places"):
        return jsonify({"error": "address and count_places are required"}), 400

    parking = Parking(
        address=data["address"],
        opened=data.get("opened", True),
        count_places=data["count_places"],
        count_available_places=data["count_places"],
    )
    db.session.add(parking)
    db.session.commit()

    return jsonify({"parking": parking.to_dict()}), 201


@bp.route("/client_parkings", methods=["POST"])
def park_in():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    client_id = data.get("client_id")
    parking_id = data.get("parking_id")

    if not client_id or not parking_id:
        return jsonify({"error": "client_id and parking_id are required"}), 400

    client = db.session.get(Client, client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404

    parking = db.session.get(Parking, parking_id)
    if not parking:
        return jsonify({"error": "Parking not found"}), 404

    if not parking.opened:
        return jsonify({"error": "Parking is closed"}), 400

    if parking.count_available_places <= 0:
        return jsonify({"error": "No available places"}), 400

    parking.count_available_places -= 1

    client_parking = ClientParking(
        client_id=client.id,
        parking_id=parking.id,
        time_in=datetime.now(timezone.utc)
    )
    db.session.add(client_parking)
    db.session.commit()

    return jsonify({
        "message": "Parked successfully",
        "client_parking": client_parking.to_dict()
    }), 201


@bp.route("/client_parkings", methods=["DELETE"])
def park_out():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    client_id = data.get("client_id")
    parking_id = data.get("parking_id")

    if not client_id or not parking_id:
        return jsonify({"error": "client_id and parking_id are required"}), 400

    client_parking = ClientParking.query.filter(
        ClientParking.client_id == client_id,
        ClientParking.parking_id == parking_id,
        ClientParking.time_out.is_(None)
    ).first()

    if not client_parking:
        return jsonify({"error": "No active parking session found"}), 404

    client = db.session.get(Client, client_id)
    if not client.credit_card:
        return jsonify({"error": "No credit card attached. Payment failed"}), 400

    client_parking.time_out = datetime.now(timezone.utc)

    parking = db.session.get(Parking, parking_id)
    parking.count_available_places += 1

    db.session.commit()

    return jsonify({
        "message": "Exited successfully",
        "client_parking": client_parking.to_dict()
    }), 200