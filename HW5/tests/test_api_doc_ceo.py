import pytest
from jsonschema import validate
from HW5.schemas import schema_list_breeds, schema_any_images, schema_one_image
from HW5.site_api_clients.dog_ceo_api_client import DogCeoSite

client_first = DogCeoSite()


def test_get_list_all_pets():
    response = client_first.get_list_all_pets()
    json_response = response.json()
    assert response.status_code == 200
    assert json_response['status'] == 'success'
    assert json_response
    validate(instance=json_response, schema=schema_list_breeds)


def test_get_random_image():
    response = client_first.get_random_image()
    json_response = response.json()
    assert response.status_code == 200
    assert json_response['status'] == 'success'
    assert json_response
    validate(instance=json_response, schema=schema_one_image)


def test_get_random_image_by_breed():
    breed = 'african'
    response = client_first.get_random_image_by_breed(breed)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response['status'] == 'success'
    assert json_response
    validate(instance=json_response, schema=schema_one_image)


@pytest.mark.parametrize("breed", ["akita", "boxer", "husky"])
def test_get_image_by_breed(breed):
    response = client_first.get_image_by_breed(breed)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response['status'] == 'success'
    assert json_response
    validate(instance=json_response, schema=schema_any_images)


@pytest.mark.parametrize("breed", ["bulldog", "hound", "mastiff"])
def test_get_list_by_sub_breed(breed):
    response = client_first.get_image_by_breed(breed)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response['status'] == 'success'
    assert json_response
    validate(instance=json_response, schema=schema_any_images)
