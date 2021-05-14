import tracery #must do: pip install tracery
from tracery.modifiers import base_english

def greeting():

  rules = {
      'origin': '#greeting.capitalize#, #name##punctuation#',
      'greeting': ["Hi there", "Hello", "Hi", "What's up", "Long time no see", "Why hello"],
      'name': ["#firstAndLast#", "#firstName#"],
      'firstName': ["Nicole", "Maanya", "Yemi", "Sue"],
      'firstAndLast': ["Nicole Binder", "Maanya Goenka", "Yemi Shin", "Sue He"],
      'punctuation': [".", "!"]
  }
  grammar = tracery.Grammar(rules)
  grammar.add_modifiers(base_english)
  print(grammar.flatten("#origin#"))


def how_are_you():
  rules = {
      'origin': '#generalStatement#, how are you?',
      'generalStatement': ["It's been awhile", "I heard you have been up to a lot", "Let's catch up", "You look great", "I'm so happy to see you"]
  }
  grammar = tracery.Grammar(rules)
  grammar.add_modifiers(base_english)
  print(grammar.flatten("#origin#"))

def response():
  rules = {
      'origin': "I have been #activity# and recently got a new #thing#, thanks for asking!",
      'activity': ["working #amount#", "traveling around #place#", "writing a #writtenObject#", "studying #amount#"],
      'amount': ["a lot", "here and there", "too much", "less", "more"],
      'place': ["Thailand", "South Africa", "Europe", "Spain", "Argentina", "Papau New Guinea", "Bulgaria", "Japan"],
      'writtenObject': ["book", "research paper", "magazine submission", "travel blog"],
      'thing': ["dog", "cat", "car", "house", "job", "partner", "passion for #hobby#"],
      'hobby': ["baking", "singing", "running", "teaching", "gaming", "crosswords"]
  }
  grammar = tracery.Grammar(rules)
  grammar.add_modifiers(base_english)
  print(grammar.flatten("#origin#"))

def farewell():
  rules = {
      'origin': "#niceStatement#! #reasonForLeaving.capitalize#, #goodbye#!",
      'niceStatement': ["That is amazing", "I am so glad to hear", "You rock", "So cool"],
      'reasonForLeaving': ["well, I've got to get to class", "oops, my parents are expecting me soon", "sorry got to go, I have a lunch date"],
      'goodbye': ["let's talk again soon", "see you soon", "I'll text you", "take care", "cheers"]
  }
  grammar = tracery.Grammar(rules)
  grammar.add_modifiers(base_english)
  print(grammar.flatten("#origin#"))

def component1():
  print("-----component 1-----\n")
  greeting()
  how_are_you()
  response()
  farewell()


if __name__ == "__main__":
  component1()


