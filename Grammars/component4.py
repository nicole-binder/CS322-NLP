from GrammarEngine import GrammarEngine

def component4():
  print("-----component 4-----\n")
  grammar_engine = GrammarEngine("component4.txt")
  result = grammar_engine.generate("origin")
  print(result)

if __name__ == "__main__":
  component4()