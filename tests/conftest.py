import pytest

@pytest.fixture()
def triangle_area_data():

    def _wrapper(data: str):
        """Return data by type"""
        if data == "integer":
            return 5, 6, 7, 14.7
        if data == "float":
            return 5.4, 6.5, 7.6, 17.22

    yield _wrapper

    print("\n Success")


@pytest.fixture()
def triangle_perimetr_data_int():
    """Return data by type==integer"""
    side_a, side_b, side_c, perimetr = 5, 6, 7, 18

    yield side_a, side_b, side_c, perimetr

    print("\n Success")


@pytest.fixture()
def triangle_perimetr_data_flot():
    """Return data by type==float"""
    side_a, side_b, side_c, perimetr = 5.5, 6.4, 7.3, 19.2

    yield side_a, side_b, side_c, perimetr

    print("\n Success")


@pytest.fixture()
def circle_area_data():

    def _wrapper(data: str):
        """Return data by type"""
        if data == "integer":
            return 3, 28.274
        if data == "float":
            return 4.4, 60.821

    yield _wrapper

    print("\n Success")


@pytest.fixture()
def circle_perimetr_data():

    def _wrapper(data: str):
        """Return data by type"""
        if data == "integer":
            return 3, 18.85
        if data == "float":
            return 4.4, 27.646

    yield _wrapper

    print("\n Success")


@pytest.fixture()
def circle_negative_data():

    def _wrapper(data: str):
        """Return data for negative tests"""
        if data == "zero":
            return 0
        if data == "below_zero":
            return -2

    yield _wrapper

    print("\n Success")