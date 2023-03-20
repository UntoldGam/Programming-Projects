def run(dataSet, query):
  for index, item in enumerate(dataSet):
    if item == query:
      return True
    else:
      continue