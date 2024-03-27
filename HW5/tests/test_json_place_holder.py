import pytest
from jsonschema import validate
from HW5.schemas import schema_posts, schema_posts_object, schema_user
from HW5.site_api_clients.json_place_holder_api_client import JsonPlaceHolderSite

client_third = JsonPlaceHolderSite()


def test_get_all_posts():
    response = client_third.get_all_posts()
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=schema_posts)


@pytest.mark.parametrize("id_", [1, 2, 3])
def test_get_user_by_id(id_):
    response = client_third.get_user_by_id(id_)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=schema_user)


@pytest.mark.parametrize("id_", [2, 3, 4])
def test_get_posts_by_id(id_):
    response = client_third.get_posts_by_id(id_)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=schema_posts_object)


def test_post_create_post_by_user():
    data = {
        "userId": 2,
        "title": "test1",
        "body": "body for test1"
    }
    response = client_third.post_create_post_by_user(data)
    json_response = response.json()
    assert response.status_code == 201
    assert json_response
    validate(instance=json_response, schema=schema_posts_object)


@pytest.mark.parametrize("id_", [2, 3, 4])
def test_patch_posts(id_):
    data = {
        "title": "test edit1",
        "body": "body edit2"
    }
    response = client_third.patch_post_by_post_id(id_, data)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response
    validate(instance=json_response, schema=schema_posts_object)
