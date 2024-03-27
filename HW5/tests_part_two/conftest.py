import pytest


@pytest.hookimpl(optionalhook=True)
def pytest_addoptoin(parser):
    parser.addoption(
        "--url",
        default="http://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default=200,
        help="Status code for orl"
    )


@pytest.fixture
def base_url(request):
    url = request.config.getoption("--urt")
    return url


@pytest.fixture
def request_status_code(request):
    code = request.config.getoption("--status_code")
    return code
