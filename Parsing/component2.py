from recursive_descent_parser import RecursiveDescentParser
from grammar_engine import GrammarEngine

def component2():
  grammar_engine = GrammarEngine("component2.txt")
  grammar = grammar_engine.grammar
  parser = RecursiveDescentParser(grammar, False)
  result = parser.parse("Joe said Buster ghosted Schiller", "S")
  
  ##keys = grammar.keys()
  # for symbol in grammar:
  #   rules[symbol] = grammar[symbol].body
  # print(rules)
  # print(grammar.variables)
  print(result)

if __name__ == "__main__":
  component2() 