from playwright.sync_api import sync_playwright

#the command for the terminal: pytest -v -s

def test_get(playwright: sync_playwright()):
    context = playwright.request.new_context()
    response = context.get(url="https://reqres.in/api/users/2")
    print(response)
    assert response.status == 200
    assert response.status_text == 'OK'
    json_data = response.json()["data"]
    assert json_data["first_name"] == "Janet"
    print(json_data["first_name"])
    #assert response.json()["first_name"] == "Janet"
    # res = response.json()
    # assert res.get("first_name") == "Janet"
