import sys 
sys.path.append("packages/drose/evens")
import evens

def test_evens():
    res = evens.evens({})
    assert res["output"] == "INVALID INPUT!"
    args = { "input": "12345678"}
    res = evens.evens(args)
    assert res["output"] == "1357"
