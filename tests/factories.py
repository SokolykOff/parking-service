import factory
from factory import Faker

from app.models import Client, Parking


class ClientFactory(factory.Factory):
    class Meta:
        model = Client

    name = Faker("first_name")
    surname = Faker("last_name")
    credit_card = Faker("credit_card_number")
    car_number = Faker("license_plate")


class ParkingFactory(factory.Factory):
    class Meta:
        model = Parking

    address = Faker("street_address")
    opened = True
    count_places = factory.Faker("random_int", min=5, max=20)
    count_available_places = factory.LazyAttribute(lambda obj: obj.count_places)
