import tracery
from tracery.modifiers import base_english

def component2():
  print("-----component 2-----\n")
  # replace with your rules
  rule1 = {
  "origin": ["#[#setNumbers#][#setObject#][#setHabitat#][#setTravelVerbs#][#setPastTenseDirectionalVerb#]poem#"],

  "setNumbers": ["[number:three][quantifier:all][smallerNumber:two]", "[number:four][quantifier:all][smallerNumber:three]", "[number:five][quantifier:many][smallerNumber:three]", "[number:six][quantifier:many][smallerNumber:four]", "[number:seven][quantifier:many][smallerNumber:four]", "[number:eight][quantifier:several][smallerNumber:five]", "[number:nine][quantifier:several][smallerNumber:five]"],

  "setHabitat": ["[natureHabitat:forest][natureNoun:overgrown weeds][color:green][habitatTrait:lush][habitatObject:bushes]","[natureHabitat:rainforest][natureNoun:streams][color:powder blue][habitatTrait:lush][habitatObject:orchids]", "[natureHabitat:tundra][natureNoun:snow piles][color:white][habitatTrait:freshly packed][habitatObject:ice]", "[natureHabitat:desert][natureNoun:gust of sand][color:beige][habitatTrait:smooth][habitatObject:brush]","[natureHabitat:savanna][natureNoun:grasses][color:olive][habitatTrait:tall][habitatObject:bluestem]", "[natureHabitat:mountain][natureNoun:peak][color:slate][habitatTrait:untouched[habitatObject:mosses]"],

  "setTravelVerbs": ["[travelVerb:wander][travelVerb-er:wanderer]","[travelVerb:traverse][travelVerb-er:traverser]","[travelVerb:walk][travelVerb-er:walker]","[travelVerb:run][travelVerb-er:runner]","[travelVerb:trek][travelVerb-er:trekker]","[travelVerb:voyage][travelVerb-er:voyager]","[travelVerb:hike][travelVerb-er:hiker]","[travelVerb:traipse][travelVerb-er:traipser]", "[travelVerb:meander][travelVerb-er:meanderer]","[travelVerb:roam][travelVerb-er:roamer]"],

  "setObject":["[object:trail]", "[object:avenue]", "[object:track]", "[object:route]", "[object:road]", "[object:passway]", "[object:passage]"],

  "setPastTenseDirectionalVerb":["[pastTenseDirectionalVerb:deviated]", "[pastTenseDirectionalVerb:divided]", "[pastTenseDirectionalVerb:strayed]", "[pastTenseDirectionalVerb:departed]", "[pastTenseDirectionalVerb:split]", "[pastTenseDirectionalVerb:diffused]"],

  "timeFrame":["prolonged", "presently", "briefly", "little", "momentarily"],

  "stillVerb":["paused", "gazed", "sat", "settled", "perched", "observed", "peered", "wondered"],

  "direction":["up", "beyond", "about", "across", "along", "around", "before", "between", "over", "admist", "past", "towards"],

  "adjective":["curved", "angled", "crossed", "dissapeared", "fell", "bowed", "arched", "looped", "twined", "sweeped"],

  "choiceVerb":["chose", "selected", "elected", "preffered", "favored"],

  "niceAdjective":["adequate", "reasonable", "satisfactory", "swell", "amiable", "inviting", "pleasant", "affable", "charming"],

  "uncertaintyAdverb":["possibly", "maybe", "slightly", "perchance", "conceivably", "likely", "mayhap"],

  "comparisonAdjective":["finer", "greater", "superior", "more exceptional", "more remarkable", "more preferable", "more admirable"],

  "adverb":["quite", "just", "utterly", "actually", "altogether", "truly", "all", "thoroughly"],

  "timeOfDay":["night", "evening", "afternoon", "dawn", "dusk"],

  "equallySynonym":["uniformly", "justly", "impartially", "evenly"],

  "troddenSynonym":["trampled", "trudged", "stomped", "walked", "paced"],

  "anotherSynonym":[" a different", "some other", "one other", "a distant", "a separate"],

  "knowingSynonym":["realizing", "observing", "sensing", "discerning", "understanding", "grasping", "recognizing"],

  "leadsSynonym":["follows", "points", "directs", "tracks"],

  "doubtedSynonym":["questioned", "hesitated", "debated"],

  "tellingSynonym":["discussing", "confessing", "reporting", "speaking", "expressing", "revealing", "stating"],

  "keptSynonym":["left", "retained", "reserved", "saved", "withheld", "held"],

  "place":["Elsewhere", "Around", "About", "Someplace", "Otherwhere"],

  "poem": ["#number.capitalize# #object.s# #pastTenseDirectionalVerb# in a #color# #natureHabitat#,\nAnd sorry I could not #travelVerb# #quantifier# \nAnd be one #travelVerb-er#, #timeFrame# I #stillVerb# \nAnd looked #direction# #smallerNumber# as far as I could \nTo where it #adjective# in the #natureNoun#;\nThen #choiceVerb# the other, as just as #niceAdjective# \nAnd having #uncertaintyAdverb# the #comparisonAdjective# claim, \nBecause it was #habitatTrait# and wanted wear; \nThough as for that the #object# there \nHad worn them #adverb# about the same,\nAnd #quantifier# that #timeOfDay# #equallySynonym# lay \nIn #habitatObject# no step had #troddenSynonym# black. \nOh, I #keptSynonym# the first for #anotherSynonym# day! \nYet #knowingSynonym# how way #leadsSynonym# on to way, \nI #doubtedSynonym# if I should ever come back.\nI shall be #tellingSynonym# this with a sigh \n#place# ages and ages hence: \n#number.capitalize# #object.s# #pastTenseDirectionalVerb# in a #natureHabitat#, and I—\nI took the one less traveled by, \nAnd that has made all the difference."]
}

  rule2 = {
  "female_name": ["Laine", "Yevette", "Joi", "Ginny", "Mable", "Britney", "Lelia", "Beulah", "Karla", "Analisa", "Eugenie"],
  "male_name": ["Elbert", "Omar", "Johnny", "Jere", "Rudy", "Bill", "Rubin", "Miquel", "Joel", "Jerome", "Jack", "Brody"],
  "setCharacter": ["[#setIdentity#][#setStages#]"],
  "setIdentity": [
    "[character: #female_name#][they: she][them: her][their: her][themselves: herself]", 
    "[character: #male_name#][they: he][them: him][their: his][themselves: himself]"
    ],
  "setStages": [
    "[stage: #trust_vs_mistrust#][age: #age_for_1#][event: #feeding#][resolution: #hope#]", 
    "[stage: #autonomy_vs_doubt#][age: #age_for_2#][event: #toilet_training#][resolution: #will#]", 
    "[stage: #initiative_vs_guilt#][age: #age_for_3#][event: #independence#][resolution: #purpose#]", 
    "[stage: #industry_vs_inferiority#][age: #age_for_4#][event: #school#][resolution: #competence#]", 
    "[stage: #identity_vs_role_confusion#][age: #age_for_5#][event: #peer_relationships#][resolution: #fidelity#]", 
    "[stage: #intimacy_vs_isolation#][age: #age_for_6#][event: #love_relationships#][resolution: #intimacy#]", 
    "[stage: #generativity_vs_stagnation#][age: #age_for_7#][event: #parenting_mentoring#][resolution: #generativity#]",
    "[stage: #ego_integrity_vs_despair#][age: #age_for_8#][event: #reflection_and_acceptance_of_life#][resolution: #wisdom#]"
    ],
  "trust_vs_mistrust": ["#trust#", "#mistrust#"],
  "autonomy_vs_doubt": ["#autonomy#", "#doubt#"],
  "initiative_vs_guilt": ["#initiative#", "#guilt#"],
  "industry_vs_inferiority": ["#industry#", "#inferiority#"],
  "identity_vs_role_confusion": ["#identity#", "#role_confusion#"],
  "intimacy_vs_isolation": ["#intimacy#", "#isolation#"],
  "generativity_vs_stagnation": ["#generativity#", "#stagnation#"],
  "ego_integrity_vs_despair": ["#ego_integrity#", "#despair#"],

  "age_for_1": ["12 month", "13 months", "14 months", "15 months", "16 months", "17 months", "18 months"],
  "age_for_2": ["18 months", "1", "2", "3"],
  "age_for_3": ["3", "4", "5", "6"],
  "age_for_4": ["6", "7", "8", "9", "10", "11", "12"],
  "age_for_5": ["13", "14", "15", "16", "17", "18", "19", "20", "21"],
  "age_for_6": ["21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39"],
  "age_for_7": ["40", "41", "42", "43", "44", "45", "50", "51", "52", "53", "54", "55", "60", "61", "62", "63", "64", "65"],
  "age_for_8": ["65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80"],

  "trust": ["#character#'s mother left #them# with the father for five minutes to do laundry, and #they# were calm throughout the absence.", "With the help of #their# father, #character# successfully played a block game.", "Even when #character# was hungry, #they# did not cry or express anger; instead #they# were able to wait for #their# mother to feed #them#."],
  "mistrust": ["#character#'s mother left #them# with the father for five minutes to do laundry, and #they# showed anxiety and frustration throughout the absence.", "Ignored by #their# mother, #character# could not focus on playing blocks, constantly diverting #their# attention to around #them#.", "When #character# was hungry, #they# expressed distress by repeatedly crying or yelling.", "#character# started crying if not held by #their# mother."],
  "feeding": ["#character#'s mother fed #them# #food# for the first time","#character# was given #food# for the first time.", "It was the first time #character# held a spoon"],
  "hope": ["#character# learned to trust #their# parents.", "#character# became a more hopeful, calm child as the parents were educated on how to raise #them#.", "#character# no longer showed frustration or distress even in the absence of #their# parent."],

  "autonomy": ["At meal time, #character# independently used the spoon without #their# parent's help.", "#character# started walking without #their# parent's help.", "#character# started climbing everywhere, exploring the house."],
  "doubt": ["After being scolded for opening the knife drawer by accident, #character# started crying uncontrollably.", "While trying to walk, #character# fell on #their# bottom, and #character# started crying."],

  "initiative": ["#character# and #their# mother were baking together, and #character# decided to make #their# own version of a cookie.", "#character# learned to bike for the first time with the help of #their# father."],
  "guilt": ["#character# and #their# mother were baking together, and #character# decided to make #their# own version of a cookie, but accidently burnt the cookie, which led #character# to feel sad.", "#character# learned to bike for the first time with the help of #their# father, and fell multiple times, which made #character# more timid."],

  "industry": ["#character# practiced spelling with #their# parents at home, and aced the spelling bee at school, leading #them# to feel proud about themselves.", "#character# got a compliment from a teacher at school.", "#character#'s friends asked #them# for help on a math puzzle, and #they# were able to help the friend."],
  "inferiority": ["#character# practiced spelling with #their# parents at home, but got a low score on a spelling quiz for a class, which upset the parents.", "#character# was scolded by a teacher at school in front of the whole class.", "#character#'s friends asked #them# for help on a math puzzle, but #they# were not able to help the friend."],

  "identity": ["#character# found what #they# wants to study in college.", "#character# has a sense of who #they# want to become, and have stable family to support that goal."],
  "role_confusion": ["#character# does not have a clue of what #they# want to become in the future.", "#character# is coping with #their# romantic relationship and school work, as well as conflict at home."],

  "intimacy": ["#character# is secure in #their# relationship with a romantic partner.", "#character# knows that #they# are loved for who #they# are/is, and is not afraid to express #themselves#."],
  "isolation": ["#character# is insecure in #their# relationship with a romantic partner, and is constantly under the fear that #their# partner will abandon them.", "#character# feels like #they# need to conceal #their# true feelings in order to be loved or appreciated."],

  "generativity": ["#character# feels fulfillment in #character#'s contribution to #their# children's lives.", "#character# feels like #they# are/is a competent at #their# work field."],
  "stagnation": ["#character# has doubts about #their# contribution to their work field.", "#character# feels like a bad parent."],

  "ego_integrity": ["#character# feels good about the choices #they# made in their life."],
  "despair": ["#character# feels like #their# life was a waste."],

  "story": ["#character# is #age#. #stage# #grow_up#"],
  "grow_up": ["[#setStages#] #character# is now #age#. #stage# #grow_up#", "[#setStages#] #character# is now #age#. #stage#"],
  "origin": ["#[#setCharacter#]story#"]
  }

  rule3 = {
  'origin':['#[#setRoutine#]content#'],
  'setRoutine': ['[day: weekday][awakeTime: 7, 8, 9][afterAwake: go to #affair# after having #meal# for breakfast, go to #affair#][lunch: I have lunch in #cafeteria# and then #afternoon#]', '[day: weekend][awakeTime: 10, 11, 12][afterAwake: have some #drinks#][lunch: I have #meal# for brunch and then go to #activity#]'],
  'content': '#introduction# #routine#',
  'introduction': ["#greeting.capitalize#, I am #name#, a #year# #major#. I live in #dorm#.", "#greeting.capitalize#, I am #name#, a #year# #major# and #minor#. I live in #dorm#."],
  'greeting': ["Hi there", "Hello", "Hi"],
  'name':  ["Nicole", "Maanya", "Yemi", "Sue"],
  'year': ["junior", "senior"],
  'major': ["CS major", "Linguistics major",],
  'minor': ["Digital Arts and Humanities minor", "Chinese minor"],
  'dorm': ["Cassat", "Nourse", "Burton", "James", "Myers", "Watson", "Goodhue"],
  'meal': ["cereal", "sandwich", "salad", "pizza", "ramen", "curry"],
  'drinks': ["americano", "cappuccino", "latte", "milk", "coke", "tea"],
  'afternoon': ["take a nap", "work in the #location#", "work in #coffee#"],
  'affair': ["work", "class", "office hour"],
  'activity': ["meet my friends in #location#", "meet with my friends in #coffee#", "grab a coffee in #coffee#"],
  'location':["library", "Weitz"],
  'coffee': ["Blue Monday", "Little Joy", "Hideaways"],
  'cafeteria': ["Burton", "LDC", "Sayles"],
  'reasonForCafeteria': ["it is closer to my dorm", "it has better food", "it has more choices", "most of my friends eat there"],
  'clubEvent': ["dance with WHOA", "practice with the choir", "play badminton with other club members"],
  'people': ["floormates", "friends", "roomate"],
  'nightEvent': ["chatting", "playing cards", "watching some Youtube videos"],
  'bedTime': ["10", "11", "midnight"],
  'routine': "A usual#day# looks like this for me: I wake up at#awakeTime# and#afterAwake#. After that,#lunch#. As for dinner, I ususally go to #cafeteria#, since #reasonForCafeteria#. After dinner, I #clubEvent#. I like #nightEvent# with my #people# before bed. And I usually go to sleep at #bedTime#."
  }

  rule4 = {"origin": ["#[character:#name_choice.capitalize#]story#"], 
  "story": ["[relative: #relation#][relative_name: #name_choice#] My #relative#'s family name being #relative_name#, and my #religion# name #name_choice#, my #adjective# tongue could make of both names nothing longer or more explicit than #character#. So, I called myself #character#, and came to be called #character#. #second_para#"], 
  "relation": ["father", "mother", "cousin", "uncle", "aunt"], 
  "religion": ["#religious#", "original", "preferred"], 
  "religious": ["Christian", "Hindu", "Jewish"], 
  "adjective": ["stupid", "infant", "", "untrained"], 
  "name_choice": ["Tom", "#name_variations#", "Dot", "Bob", "Ben", "Carl", "Rae", "Ed", "Trey", "Nick", "Oli", "Tim", "Henry", "Alex", "Perl", "Carly", "Sam", "Ned"], 
  "name_variations": ["Pip", "Pop", "Poe", "Pi", "Pep"], 
  "second_para": ["I give #relative_name# as my #relative#'s family name, and my sister - Mrs. #name_choice# #last_name#, who married the blacksmith. As I never saw my parents, and never saw any likeness of either of them (for #reason_for_not_seeing_relative#), my first fancies regarding what they were like, were unreasonably derived from their [object_memory: #objects_memory#] #object_memory#. The shape of the letters on my #relative#'s #object_memory#, gave me an odd idea that they were #descriptive.a#, #descriptive#, #descriptive# type of person, with #hair# hair. #third_para#"], 
  "last_name": ["Smith", "Gregory", "Luna", "Peep", "#color.capitalize#"], "color":["white", "brown", "black", "green"], 
  "reason_for_not_seeing_relative": ["their days were long before the days of photographs", "they were never around", "they were always working", "they were #mean_adjective#"], 
  "mean_adjective": ["rude", "mean-spirited", "disloyal", "discouraging", "impudent"], 
  "objects_memory": ["tombstones", "diaries", "letters", "epitaphs"], "descriptive": ["#appearance#", "#mind#"], "appearance":["#weight#", "#height#", "#face#"], 
  "weight": ["fat", "stout", "thin", "skinny", "lanky"], "height": ["tall", "short", "giant", "tiny"], 
  "face": ["beautiful", "wonderful", "attractive", "mesmerizing"], "mind": ["smart", "intelligent", "thoughtful", "enlightened"], 
  "hair": ["#length##style#"], "length": ["long", "short"], "style": ["curly", "frizzy", "messy", "sleek"], 
  "third_para": ["When my #relative# died, [number: #numbers#] #number# little stone lozenges, each about a foot and a half long, were arranged in a neat row beside the grave, and were sacred to the memory of #number# little #sibling.s# of mine - who gave up #making_money#, exceedingly early in that universal struggle. #fourth_para#"], 
  "numbers": ["5","6","7","8","20","10"], 
  "sibling": ["brother", "sister", "niece", "nephew"],
  "making_money": ["trying to earn a living", "making #money#", "working to make some #money#"], 
  "money": ["money", "pennies", "dough", "bucks", "cash"], 
  "fourth_para": ["Ours was the marsh country, down by the [place_choice: #place#] #place_choice#, within, as the #place_choice# wound, #number# miles of the #place_choice#. My first most vivid and broad impression of the identity of things, seems to me to have been gained on a memorable raw #time_of_day#. At such a time I found out for certain, that this #face# place overgrown with nettles was the churchyard; and that #relative_name#, late of this parish was dead and buried; and that #name_choice#, #name_choice#, #name_choice#, #name_choice#, and #name_choice#, #adjective# children of the aforesaid, were also dead and buried; and that the dark flat wilderness beyond the churchyard, intersected with dykes and mounds and gates, with scattered cattle feeding on it, was the #marsh.s#; and that the low leaden line beyond, was the #place_choice#; and that the distant lair from which the wind was rushing, was the sea; and that the #height# bundle of #reaction.s# growing afraid of it all and beginning to #cry#, was #character#."], 
  "place": ["#water_body#", "docks", "park", "prarie"], 
  "water_body": ["sea", "river", "lake"], 
  "time_of_day": ["morning", "afternoon", "evening", "night", "dawn", "twilight"], 
  "marsh": ["marsh", "swamp", "wetland", "bog"], 
  "reaction": ["tear", "shiver", "quiver", "tremble"], 
  "cry": ["cry", "sob", "wail"]
  }

  rules = [rule1, rule2, rule3, rule4]
  for rule in rules:
    grammar = tracery.Grammar(rule)
    grammar.add_modifiers(base_english)
    print(grammar.flatten("#origin#"))
    print("\n")

if __name__ == "__main__":
  component2()