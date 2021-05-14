

#Nicole
class ShiftReduceParser:

  def __init__(self):
    self.rules = self.set_rules()
    self.stack = [] #instance variable to reduce passing back n forth between functions
    #stack using list methods: stack[-1] --> peek, pop(), append() --> push, clear() --> empty
    self.unread = [] #stuff not in the stack
    self.parse_tree = []

  def set_rules(self):
    rules = {
        'S': ["#NP# #VP#"],
        'NP': ["#Det# #Nom#", "#PropN#"],
        'Nom': ["#Adj# #Nom#", "#N#"],
        'VP': ["#V# #NP#", "#V# #S#", "#V# #NP# #PP#"],
        'PP': ["#P# #NP#"],
        'PropN': ["Buster", "Schiller", "Joe"],
        'Det': ["the", "a", "every"],
        'N': ["bear", "squirrel", "tree", "fish", "log"],
        'Adj': ["angry", "frightened", "little", "tall"],
        'V': ["chased", "saw", "dodged", "loved", "ghosted", "said"],
        'P': ["under", "over", "near"],
    }
    return rules
  
  def parse_string(self, string):
    parse_tree = []
    if len(string) == 0:
      return "Nothing to parse"
    tokens = string.split()
    self.unread = tokens
    while len(self.unread) != 0:
      self.shift()
    return self.parse_tree

  def shift(self):
    #push token to stack and remove token from unread tokens
    self.stack.append(self.unread[0])
    self.unread = self.unread[1:]
    self.reduce(Node("", Node("")))

  def reduce(self, previous_node, add_to_top = False, size = 1):
    starting_stack = self.stack.copy()
    #only look at the 1st item on the stack
    if not add_to_top:
      top_of_stack = self.stack[-1]
      nth_items = []
      nth_items.append(1)
    #look at n first items on stack and concat into string for search
    else:
      nth_items = []
      num = size #new variable so original size isn't changed
      for i in range(size):
        nth_items.append(self.stack[-1-num])
        num-=1
      nth_items.append(self.stack[-1])
      #concat into string so search of values can be done
      top_of_stack = ""
      for item in nth_items:
        top_of_stack += item + " "
      top_of_stack = top_of_stack[0:len(top_of_stack)-1] #remove ending space
    #search through values of rules, if match found, replace n items with left value
    for rule in self.rules.keys():
      if top_of_stack in self.rules[rule]:
        #check if the previously added node's parent is now the current node
        if top_of_stack == previous_node.parent.symbol:
          on_previous = True
          new_node = previous_node.parent
        else:
          on_previous = False
          new_node = Node(top_of_stack)
        for i in range(len(nth_items)):
          self.stack.pop()
        self.stack.append("#" + rule + "#")
        new_node.parent = Node(self.stack[-1])
        previous_node = new_node
        #only add to parse tree if symbol isn't a parent
        if not on_previous:
          self.parse_tree.append(new_node)
        add_to_top = False
        break
    #keep reducing first items on stack until nothing changes
    if add_to_top == False and starting_stack != self.stack:
      self.reduce(previous_node)
    #if no changes occur, add more items to search value
    # e.g. stack = #V# #Det# #Adj# doesn't reduce, next round search #Det# #Adj#
    elif add_to_top == False and len(self.stack) > size:
      self.reduce(previous_node, True)
    # keep adding until change in stack (or stack is exhausted)
    # e.g. stack = #V# #Det# #Adj#, now search #V# #Det# #Adj# in values
    elif starting_stack == self.stack and add_to_top == True and len(self.stack) > size + 1: #reduce again if nothing changes
      self.reduce(previous_node, True, size + 1)

  def print_parse_tree(self):
    #not correct
    for node in self.parse_tree:
      print(node.symbol + " --> " + node.parent.symbol, end = " ")
      try:
        print("--> " + node.parent.parent.symbol)
      except:
        print("")   

class Node:
  def __init__(self, symbol, parent = ""):
    self.symbol = symbol
    self.parent = parent

def main():
  parser = ShiftReduceParser()
  parse_tree = parser.parse_string("Buster ghosted a little tree")
  #parse tree notation:
  #(S (NP (PropN Buster)) (VP (V ghosted) (NP (Det a) (Nom (Adj little (Nom (N tree)))))))
  parser.print_parse_tree()

main()