#--kind python:default
#--web true
import odds
def main(args):
  return { "body": odds.odds(args) }
