import os, requests as req
def test_odds():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/drose/odds"
    res = req.get(url).json()
    assert res.get("output") == "INVALID INPUT!"
    args = { "input": "12345678"}
    res = req.post(url, json=args).json()
    assert res["output"] == "2468"
