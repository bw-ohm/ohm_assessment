
from app_main import app
from tests import OhmTestCase


class DashboardTest(OhmTestCase):
    def test_get(self):
        with app.test_client() as c:
            response = c.get('/community')
            assert "Community" in response.data
            assert "community-table" in response.data
            # Ensure there are at most 5 users shown
            rows = response.data.count('class="row community-row"')
            assert rows <= 5
