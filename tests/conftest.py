import pytest
import os

from tapioca_iugu import Iugu


@pytest.fixture
def api_client():
    return Iugu(user=os.getenv('IUGU_TOKEN', default=''), password='')
