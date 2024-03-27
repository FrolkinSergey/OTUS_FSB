import pytest
from jsonschema import validate
from HW5.schemas import schema_any_brewery, schema_one_brewery2
from HW5.site_api_clients.open_brewery_api_client import OpenBrewerySite

client_second = OpenBrewerySite()


def test_get_list_all_breweries():
    response = client_second.get_list_all_breweries()
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=schema_any_brewery)


@pytest.mark.parametrize("id_", ["5128df48-79fc-4f0f-8b52-d06be54d0cec",
                                 "34e8c68b-6146-453f-a4b9-1f6cd99a5ada"]
                         )
def test_get_brewery_by_id(id_):
    response = client_second.get_brewery_by_id(id_)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=schema_one_brewery2)


@pytest.mark.parametrize("size", [2, 5, 10])
def test_get_random_any_breweries(size):
    response = client_second.get_random_any_breweries(size)
    json_response = response.json()
    first_dict = json_response[0]
    second_dict = json_response[1]
    assert response.status_code == 200
    assert first_dict['id'] != second_dict['id']
    assert json_response
    validate(instance=json_response, schema=schema_any_brewery)


@pytest.mark.parametrize("id_", ["5128df48-79fc-4f0f-8b52-d06be54d0cec",
                                 "9c5a66c8-cc13-416f-a5d9-0a769c87d318",
                                 "597c06aa-6c9f-4652-a0b0-7db11364374f"]
                         )
def test_get_search_brewer_by_id(id_):
    response = client_second.get_search_brewery_by_id(id_)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=schema_any_brewery)


@pytest.mark.parametrize(["params", "value"],
                         [("by_city", "san_diego"), ("by_type", "micro")]
                         )
def test_get_search_by_another_params(params, value):
    response = client_second.get_search_brewery_by_another_params(params, value)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=schema_any_brewery)
