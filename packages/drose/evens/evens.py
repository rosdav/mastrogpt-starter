def evens(args):
  strIN = args.get("input", "IINNVVAALLIIDD  IINNPPUUTT!!")
  strOUT = strIN[::2]
  return { "output": strOUT }
