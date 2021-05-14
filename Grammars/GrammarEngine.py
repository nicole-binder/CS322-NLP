import random

class GrammarEngine:
  def __init__(self, path_to_file):
    self.grammar_file = self._load_corpus(path_to_file)
    self.grammar = self.parse_grammar(self.grammar_file)
    self.variables = dict()
  
  @staticmethod
  def _load_corpus(corpus_filename):
    '''
    Returns the contents of a corpus loaded from a corpus file.

    Credit to James (Took from Comp Med HW file)

    Args:
      corpus_filename:
        The filename for the corpus that's to be loaded.

    Returns:
      A single string

    Raises:
      IOError:
        There is no corpus file with the given name in the 'corpora' folder.
    '''
    corpus_text = open(f"{corpus_filename}").read()
    return corpus_text
  
  # Yemi, Maanya
  @staticmethod
  def parse_grammar(grammar_file):
    '''
    parse the grammar file to create a bunch of NonterminalSymbol objects and ProductionRule objects.

    Syntax:
    greeting -> <greeting word> <#name> <punct> blah
    greeting -> Hello
    greeting word -> Hello|Hey|Hi|Yo
    name -> <first name> <last name> | <first name>
    first name -> Abdul|Betty|Caesar
    last name -> Xavier|Yi|Zimmer
    punct -> .|! 
    
    dictionary
    key: nonterminal_symbol
    value: a list of production rules for which this symbol is the head

    {greeting: [Object([<greeting word>,<name>,<punct>]), Object([Hello])]}
    '''
    punctuations_for_parse = '''!()-[]{};:'"\,./?@#$%^&*_~\t'''
    dictionary = dict()
    dictionary_of_nonterminal_symbols = dict()
    grammar = grammar_file.split("\n")

    for line in grammar:
      split_text = line.split("->")
      head, body = split_text[0].strip(), split_text[1].strip()
      if head not in dictionary_of_nonterminal_symbols:
        head_nonterminal = NonterminalSymbol(symbol = head)
        dictionary_of_nonterminal_symbols[head] = head_nonterminal
      if head not in dictionary:
        dictionary[head] = list()
    
      list_of_symbols = list()
      if "<" in body:
        index = 0
        while index < len(body):
          if body[index] == "<":
            index += 1
            savable = False
            if body[index] == "#":
              savable = True
              index += 1
            index_of_end_symbol = body.index(">", index) # start looking for the symbol from index
            nonterminal_symbol = NonterminalSymbol(symbol = body[index:index_of_end_symbol], savable = savable)
            dictionary_of_nonterminal_symbols[nonterminal_symbol.symbol] = nonterminal_symbol
            list_of_symbols.append(nonterminal_symbol)
            index = index_of_end_symbol + 1
          elif body[index] == "|":
            dictionary[head].append(list_of_symbols)
            list_of_symbols = list()
            index += 1
          elif body[index] == " ":
            index += 1
          else:
            string = ""
            while index < len(body) and body[index] != "<" and body[index] != "|":
              string += body[index]
              index += 1
            list_of_symbols.append(string)
        dictionary[head].append(list_of_symbols)
      else:
        split_string = body.split("|") 
        for item in split_string:
          dictionary[head].append([item.strip()])
      list_of_symbols = list()

    for key in dictionary.keys():
      list_of_production_rules = list()
      for value in dictionary[key]:
        production_rule = ProductionRule(key, value)
        list_of_production_rules.append(production_rule)
      nonterminal_symbol = dictionary_of_nonterminal_symbols[key]
      nonterminal_symbol.rules = list_of_production_rules
    
    return dictionary_of_nonterminal_symbols
  
  # Sue
  def generate(self,start_symbol):
    '''
    while there is at least one nonterminal symbol in the intermediate output, rewrite the leftmost nonterminal symbol in that intermediate output; once you have only terminal symbols (strings), concatenate them to form your final output. 
    '''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~\t'''
    intermediate_list = [start_symbol]
    symbols_list = self._rewrite_symbols(intermediate_list, 0)
    concatenated_string = ""
    for item in symbols_list:
      if item not in punctuations and len(concatenated_string) != 0 and item[0] not in punctuations:
        concatenated_string = concatenated_string + " " + item
      else:
        concatenated_string = concatenated_string + item
    return concatenated_string

  def _rewrite_symbols(self, intermediate_list, curr_index): 
    while curr_index < len(intermediate_list):
      curr_symbol = intermediate_list[curr_index]
      if curr_symbol in self.variables.keys():
        intermediate_list.insert(curr_index + 1, self.variables[curr_symbol])
        intermediate_list.remove(curr_symbol)
        self._rewrite_symbols(intermediate_list, curr_index)
      elif curr_symbol in self.grammar:
        random_rule = random.choice(self.grammar[curr_symbol].rules)
        if self.grammar[curr_symbol].savable:
          self.set_variable(curr_symbol, random_rule.body[0])
        insert_index = curr_index
        for symbol in random_rule.body:
          insert_index += 1
          intermediate_list.insert(insert_index, str(symbol))
        intermediate_list.remove(curr_symbol)
        self._rewrite_symbols(intermediate_list, curr_index)
      curr_index += 1
    return intermediate_list

  # Nicole
  def set_variable(self, key, value):
    '''
    accepts a key and value, and makes an entry in the self.variables dictionary
    '''
    self.variables[key] = value

class NonterminalSymbol:
  def __init__(self, symbol, production_rules = list(), savable = False):
    '''
    Each NonterminalSymbol object will have a rules instance variable, which stores a list of ProductionRule objects where this symbol is the head
    '''
    self.symbol = symbol
    self.rules = production_rules
    self.savable = savable
  
  def __repr__(self):
    return f"{self.symbol}"

class ProductionRule:
  def __init__(self, head, body):
    '''
    Each ProductionRule object will have a head instance variable, which stores the NonterminalSymbol object associated with the symbol on the left-hand side of the rule, and a body instance variable, which stores the body of the rule (i.e., the right-hand side of the rule); the body should be represented as a list of NonterminalSymbol objects and strings (the latter being the terminal symbols). 
    '''
    self.head = head
    self.body = body
  
  def __repr__(self):
    return f"{self.body}"

if __name__ == "__main__":
  grammar_engine = GrammarEngine("component4.txt")
  result = grammar_engine.generate("origin")
  print(result)