import pytest


class TestDemo:
    @pytest.mark.dependency(name='case1')
    def test_login(self, lunch):
        lunch.goto("https://www.google.com/")
        lunch.get_by_role("combobox", name="Search").click()
        lunch.get_by_role("combobox", name="Search").fill("测试playwright")
        lunch.get_by_role("combobox", name="Search").press("Enter")
