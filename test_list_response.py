import logging

from playwright.sync_api import sync_playwright
from utils import LoggerDemo

def test_response(playwright: sync_playwright()):
    log = LoggerDemo().custom_logger(log_level=logging.WARNING)
    context = playwright.request.new_context(base_url="https://reqres.in/")
    query_params = {
        "page": "2"
    }
    response = context.get(url="/api/users", params=query_params, headers={
        "content-type":"application/json",
        "x-api-key":"reqres-free-v1"
    })
    #print(response)
    log.warning(response)
    assert response.status == 200
    assert response.status_text == 'OK'
    res = response.json()["data"]
    log.warning(res)
    assert res != ""
    #print(res)
    #assert "Lindsay" == res[0].get("first_name")

    size = len(res)
    print(size)

    for i in range(0, size+1):
        if "Lindsay" == res[0].get("first_name"):
            assert "Lindsay" == res[0].get("first_name")
            break

    for j in res:
        j_res = j
        assert j_res["id"] != ""
        assert j_res["email"] != ""
        assert j_res["first_name"] != ""
        assert j_res["last_name"] != ""
        assert j_res["avatar"] != ""
        print(j) #for debugging