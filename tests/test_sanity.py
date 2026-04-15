def test_automationdemo_loads(page):
    page.goto("https://www.saucedemo.com")
    assert "Swag Labs" in page.title()