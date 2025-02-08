import sys 
sys.path.append("packages/drose/odds")
import odds

def test_odds():
    res = odds.odds({})
    assert res["output"] == "INVALID INPUT!"
    args = { "input": "12345678"}
    res = odds.odds(args)
    assert res["output"] == "2468"    
