def odds(args):
  strIN = args.get("input", "IINNVVAALLIIDD  IINNPPUUTT!!")
  strOUT = strIN[1::2]
  return { "output": strOUT }
