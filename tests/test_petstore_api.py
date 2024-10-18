import pytest

def test_add_pet(petstore_api):
    pet_data = {
        "id": 123,
        "name": "Doggo",
        "status": "available"
    }
    response = petstore_api.add_pet(pet_data)
    assert response.ok
    assert response.json()["name"] == "Doggo"

def test_get_pet(petstore_api):
    pet_id = 123
    response = petstore_api.get_pet(pet_id)
    assert response.ok
    assert response.json()["id"] == pet_id

def test_update_pet(petstore_api):
    pet_data = {
        "id": 123,
        "name": "DoggoUpdated",
        "status": "sold"
    }
    response = petstore_api.update_pet(pet_data)
    assert response.ok
    assert response.json()["name"] == "DoggoUpdated"

def test_delete_pet(petstore_api):
    pet_id = 123
    response = petstore_api.delete_pet(pet_id)
    assert response.ok
