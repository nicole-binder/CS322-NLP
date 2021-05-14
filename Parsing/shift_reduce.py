from grammar_engine import GrammarEngine

class Node:
  def __init__(self, symbol, child = None, next = None):
    self.symbol = symbol
    self.child = child
    self.next = next
  
  def __repr__(self):
    return f"Node({self.symbol.name})"

# Yemi
class ShiftReduceParser2:
  def __init__(self, grammar_file):
    '''
    GrammarEngine.grammar returns a Grammar object 
    to get the actual dictionary, do GrammarEngine.grammar.grammar
    '''
    self.grammar = GrammarEngine(grammar_file).grammar.grammar
    self.verbose = False
  
  def parse(self, string, verbose = False):
    self.verbose = verbose

    stack = []
    remaining = string.split()

    # if there are tokens remaining to be parsed
    while len(remaining) > 0:
      token = remaining[0]
      remaining = remaining[1:]
      self.shift(stack, token)
      self.reduce(stack)
    
    # if you've exhausted all tokens but still need to reduce
    while len(stack) != 1:
      self.reduce(stack)
    
    return stack.pop()
  
  def shift(self, stack, token):
    if self.verbose:
      print(f"Appending '{token}'")
    stack.append(token)

  def reduce(self, stack):
    '''
    rules = {
        S -> <NP> <VP>
        NP -> <Det> <Nom> | <PropN>
        Nom -> <Adj> <Nom> | <N>
        VP -> <V> <NP> | <V> <S> | <V> <NP> <PP>
        PP -> <P> <NP>
        PropN -> Buster | Schiller | Joe
        Det -> the | a | every
        N -> bear | squirrel | tree | fish | log
        Adj -> angry | frightened | little | tall
        V -> chased | saw | dodged | loved | ghosted | said
        P -> under | over | near
    }

    Progression:

    ["Buster"]
    [(PropN "Buster")]
    [(NP (PropN "Buster"))]
    [(NP (PropN "Buster")), "ghosted"]
    [(NP (PropN "Buster")), (V "ghosted")]
    [(NP (PropN "Buster")), (V "ghosted"), "a"]
    [(NP (PropN "Buster")), (V "ghosted"), (DET "a")]
    [(NP (PropN "Buster")), (V "ghosted"), (DET "a"), "little"]
    [(NP (PropN "Buster")), (V "ghosted"), (DET "a"), (ADJ "little")]
    [(NP (PropN "Buster")), (V "ghosted"), (DET "a"), (ADJ "little"), "tree"]
    [(NP (PropN "Buster")), (V "ghosted"), (DET "a"), (ADJ "little"), "tree"]
    [(NP (PropN "Buster")), (V "ghosted"), (DET "a"), (ADJ "little"), (N "tree")]
    [(NP (PropN "Buster")), (V "ghosted"), (DET "a"), (ADJ "little"), (Nom (N "tree"))]
    [(NP (PropN "Buster")), (V "ghosted"), (DET "a"), (Nom (ADJ "little") (Nom (N "tree")))]
    [(NP (PropN "Buster")), (V "ghosted"), (NP (DET "a") (Nom (ADJ "little") (Nom (N "tree"))))]
    [(NP (PropN "Buster")), (VP (V "ghosted") (NP (DET "a") (Nom (ADJ "little") (Nom (N "tree")))))]
    [(S (NP (PropN "Buster")) (VP (V "ghosted") (NP (DET "a") (Nom (ADJ "little") (Nom (N "tree"))))))]

    return S 

    Pop an item 

    if it's a string, reduce it to a nonterminal as much as possible, each time creating a new node, subordinating the previous value as its child, push the node back into the stack

    if it's a nonterminal 
    while stack is not empty
      pop it off, save it,
      check if it matches any of the terminal symbols' rules
      if not, pop another nonterminal symbol, concatenate it to the previous nonterminal in the correct order in the expected format with white space between things, see if this grammar rule matches any of the terminal symbol's rules.

      if there is a match, create a new node where the child is matching list of nonterminal, push this node back onto the stack 

      self.grammar is a dictionary of nonterminal symbols
    '''
    token = stack.pop()
    used_token = False

    # if it's a string, reduce it to a nonterminal
    if type(token) == str:
      for nonterminal in self.grammar.keys():
        nonterminal_symbol_obj = self.grammar[nonterminal]
        for rule in nonterminal_symbol_obj.rules:
          if [token] == rule.body:
            new_node = Node(symbol = nonterminal_symbol_obj, child = Node(token))
            stack.append(new_node)
            used_token = True
            if self.verbose:
              print(f"Appending new node '{new_node.symbol.name}' from terminal symbol '{token}'")
              print("stack looks like:")
              print(stack)
  
    # if the popped token was not used because it was a nonterminal symbol, push it back in
    if not used_token:
      if self.verbose:
        print(f"Because {token.symbol} was not used, appended back on the stack." )
      stack.append(token)

    # if it's a nonterminal, combine nonterminals if necessary to reduce 
    token_list = [] # list containing nonterminal symbol objects
    token_list_to_be_modified = [] # list containing nodes
    reduced = False
    while len(stack) > 0 and not reduced:
      # if the token_list already contains something, add an white space before adding a new token to account for white space
      if len(token_list) != 0:
        token_list.append(' ') 
      node = stack.pop()
      token_list.append(node.symbol) # [obj(NP), obj(VP)]
      token_list_to_be_modified.append(node) # [Node(obj(NP)), Node(obj(VP))]
      # reverse the list because due to the property of "popping" in the opposite order, you need to correct the order 
      token_list.reverse() 
      token_list_to_be_modified.reverse()
      if self.verbose:
        print(f"Trying out production rule: {token_list}")

      # check if there's a matching rule to this token_list
      for nonterminal in self.grammar.keys():
        nonterminal_symbol_obj = self.grammar[nonterminal]
        for rule in nonterminal_symbol_obj.rules:
          if token_list == rule.body:
            # link the nodes that are adjacent to one another
            for i in range(len(token_list_to_be_modified) - 1):
              token_list_to_be_modified[i].next = token_list_to_be_modified[i + 1]
            new_node = Node(symbol = nonterminal_symbol_obj, child = token_list_to_be_modified[0])
            stack.append(new_node)
            reduced = True
            if self.verbose:
              print(f"Appending new node '{new_node.symbol.name}' from nonterminal symbol '{nonterminal_symbol_obj.name}'")
            break
        # tiny little optimization to stop it from going allll they way down the list
        if reduced:
          break

      # if there was a reduction, clear the intermediate lists, and move on 
      if reduced:
        if self.verbose:
          print("Reduced")
        token_list = []
        token_list_to_be_modified = []

      # if there wasn't a reduction, and you still have stuff in the stack, pop another item and add it to the token_list 
      elif not reduced and len(stack) > 0:
        if self.verbose:
          print("It was not reduced but trying again")
          print("stack looks like:")
          print(stack)
        token_list.reverse() # you need to re-reverse it so that when you add a new item it won't be all jacked up
        token_list_to_be_modified.reverse()

      # if there was not a reduction, and there are no more things to pop off the stack,
      else:
        for node in token_list_to_be_modified:
          stack.append(node)
        reduced = True
        if self.verbose:
          print("It was not reduced and there are no more things to pop off the stack, so quitting, while restoring stack to original condition")
          print("stack looks like:")
          print(stack)
  
  def print_tree(self, root):
    if type(root.symbol) == str:
      return root.symbol
    else:
      string = ""

      if root.child != None:
        string += "(" + root.symbol.name + " " + self.print_tree(root.child) + ")"
      
      if root.next != None:
        string += self.print_tree(root.next)

      return string

if __name__ == "__main__":
  parser = ShiftReduceParser2("component2.txt")
  tree = parser.parse("Joe said Buster ghosted Schiller", False)
  print(parser.print_tree(tree))