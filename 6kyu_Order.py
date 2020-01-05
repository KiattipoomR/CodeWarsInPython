def order(sentence):
  result = []
  sentence = sentence.split();
  for i in range(1, len(sentence)+1):
      for block in sentence:
          if str(i) in block: result.append(block)
  return " ".join(result)
