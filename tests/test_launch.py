import pytest

@pytest.mark.usefixtures("setup")
class TestLaunch:

    def test_open_site(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        assert "GreenKart" in self.driver.title
