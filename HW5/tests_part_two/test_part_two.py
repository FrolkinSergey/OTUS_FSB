import pytest
from HW5.tests_part_two.conftest import request_status_code


@pytest.mark.parametrize(["url", "code"],
                         [("https://ya.ru", 200), ("https://mail.ru", 200), ("https://ya.ru/sfhfh", 400)]
                         )
def test_status_code_by_url(url, code):
    response = request_status_code(url)
    assert response.status_code == code
