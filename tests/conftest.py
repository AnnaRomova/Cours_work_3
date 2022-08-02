import pytest
from coursework2_source import run

# создаем фикстуру для тестирования всех вьюшек (lenta, candidates)
@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()