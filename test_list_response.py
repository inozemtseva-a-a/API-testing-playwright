from playwright.sync_api import sync_playwright

def test_response(playwright: sync_playwright()):
    context = playwright.request.new_context(base_url="https://reqres.in/")
    query_params = {
        "page": "2"
    }
    response = context.get(url="/api/users", params=query_params, headers={
        "content-type":"application/json",
        "x-api-key":"reqres-free-v1"
    })
    print(response)
    assert response.status == 200
    assert response.status_text == 'OK'
    res = response.json()["data"]
    assert res != ""
    print(res)
    #assert "Lindsay" == res[0].get("first_name")

    size = len(res)
    print(size)

    for i in range(0, size+1):
        if "Lindsay" == res[0].get("first_name"):
            assert "Lindsay" == res[0].get("first_name")
            break