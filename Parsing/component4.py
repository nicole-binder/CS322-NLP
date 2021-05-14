from grammar_engine import GrammarEngine
from island_parser import IslandParser

def component4():
  grammar_engine = GrammarEngine("component4.txt")
  grammar = grammar_engine.grammar
  generated_texts = []

  for i in range(1):
    text = grammar_engine.generate("origin")
    generated_texts.append(text)

  final_sentence = " ".join(generated_texts)
  print(final_sentence)
  parser = IslandParser(grammar)
  result = parser.parse(final_sentence) 
  for element in result:
      substrings = element.split()
      print(substrings[0][1:]+ ":" + substrings[1][:-1])

if __name__ == "__main__":
  component4()
