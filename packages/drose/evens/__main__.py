#--kind python:default
#--web true
import evens
def main(args):
  return { "body": evens.evens(args) }
