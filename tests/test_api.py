import pytest
from tests.factories import ClientFactory, ParkingFactory


def test_create_client(client):
    client_data = ClientFactory.build()

    response = client.post(
        "/clients",
        json={
            "name": client_data.name,
            "surname": client_data.surname,
            "credit_card": client_data.credit_card,
            "car_number": client_data.car_number,
        },
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["client"]["name"] == client_data.name
    assert data["client"]["surname"] == client_data.surname
    assert data["client"]["credit_card"] == client_data.credit_card
    assert data["client"]["car_number"] == client_data.car_number
    assert "id" in data["client"]


def test_create_parking(client):
    parking_data = ParkingFactory.build()

    response = client.post(
        "/parkings",
        json={
            "address": parking_data.address,
            "count_places": parking_data.count_places,
            "opened": parking_data.opened,
        },
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["parking"]["address"] == parking_data.address
    assert data["parking"]["count_places"] == parking_data.count_places
    assert data["parking"]["opened"] == parking_data.opened
    assert data["parking"]["count_available_places"] == parking_data.count_places
    assert "id" in data["parking"]


def test_get_clients(client):
    client_data = ClientFactory.build()
    client.post(
        "/clients",
        json={
            "name": client_data.name,
            "surname": client_data.surname,
            "credit_card": client_data.credit_card,
            "car_number": client_data.car_number,
        },
    )

    response = client.get("/clients")
    assert response.status_code == 200
    data = response.get_json()
    assert "clients" in data
    assert len(data["clients"]) >= 1


def test_get_client_by_id(client):
    client_data = ClientFactory.build()
    create_response = client.post(
        "/clients",
        json={
            "name": client_data.name,
            "surname": client_data.surname,
            "credit_card": client_data.credit_card,
            "car_number": client_data.car_number,
        },
    )
    client_id = create_response.get_json()["client"]["id"]

    response = client.get(f"/clients/{client_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["client"]["id"] == client_id
    assert data["client"]["name"] == client_data.name


def test_park_in(client):
    client_data = ClientFactory.build()
    create_client = client.post(
        "/clients",
        json={
            "name": client_data.name,
            "surname": client_data.surname,
            "credit_card": client_data.credit_card,
            "car_number": client_data.car_number,
        },
    )
    client_id = create_client.get_json()["client"]["id"]

    parking_data = ParkingFactory.build()
    create_parking = client.post(
        "/parkings",
        json={
            "address": parking_data.address,
            "count_places": parking_data.count_places,
        },
    )
    parking_id = create_parking.get_json()["parking"]["id"]

    response = client.post(
        "/client_parkings", json={"client_id": client_id, "parking_id": parking_id}
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Parked successfully"
    assert data["client_parking"]["client_id"] == client_id
    assert data["client_parking"]["parking_id"] == parking_id


def test_park_out(client):
    client_data = ClientFactory.build()
    create_client = client.post(
        "/clients",
        json={
            "name": client_data.name,
            "surname": client_data.surname,
            "credit_card": client_data.credit_card,
            "car_number": client_data.car_number,
        },
    )
    client_id = create_client.get_json()["client"]["id"]

    parking_data = ParkingFactory.build()
    create_parking = client.post(
        "/parkings",
        json={
            "address": parking_data.address,
            "count_places": parking_data.count_places,
        },
    )
    parking_id = create_parking.get_json()["parking"]["id"]

    client.post(
        "/client_parkings", json={"client_id": client_id, "parking_id": parking_id}
    )

    response = client.delete(
        "/client_parkings", json={"client_id": client_id, "parking_id": parking_id}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Exited successfully"


@pytest.mark.parametrize("endpoint", ["/clients", "/clients/{client_id}"])
def test_get_endpoints_return_200(client, endpoint):
    """Параметризованный тест для GET-методов (требование из ТЗ)."""
    # Создаём клиента, чтобы был id для второго эндпоинта
    create_response = client.post(
        "/clients",
        json={
            "name": "Test",
            "surname": "User",
            "credit_card": "1234567890123456",
            "car_number": "A123BC",
        },
    )
    assert create_response.status_code == 201
    client_id = create_response.get_json()["client"]["id"]

    # Подставляем client_id в эндпоинт
    url = endpoint.format(client_id=client_id)
    response = client.get(url)
    assert response.status_code == 200
