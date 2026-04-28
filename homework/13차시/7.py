try:
    raise KeyError("Key is missing!")
except KeyError as e:
    print(e)