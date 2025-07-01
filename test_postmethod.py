from playwright.sync_api import sync_playwright

#the command for the terminal: pytest -v -s

def test_post(playwright: sync_playwright()):
    context = playwright.request.new_context()
    response = context.post(url="https://reqres.in/api/users", headers={
        "content-type":"application/json",
        "x-api-key":"reqres-free-v1"
    }, data = {
    "name": "morpheus",
    "job": "leader"
})
    assert response.status == 201
    assert response.status_text == 'Created'
    assert response.json()["name"] == "morpheus"
    assert response.json()["job"] == "leader"
    assert response.json()["id"] != ""
    assert response.json()["createdAt"] != ""
    # print(response)
    # print(response.json()) #for debug

