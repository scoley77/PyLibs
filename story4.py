print("Let's do this!")

name = input('a name:').strip()
verb1 = input('a verb:').strip()
feeling1 = input('an emotion:').strip()
sense = input('one of the 5 senses:').strip()
adj1 = input('an adjective:').strip()
adj2 = input('an adjective:').strip()
person1 = input('a type of person:').strip()
place = input('a place:')
body = input('a body part:').strip()
verb2 = input('a verb:').strip()
feeling2 = input('an emotion:').strip()
feeling3 = input('an emotion:').strip()
person2 = input('a type of person:').strip()
adj3 = input('an adjective:').strip()
noun = input('a noun:').strip()
farewell = input('a farewell:').strip()
name2 = input('a name:').strip()

print(f'Dear {name},')
print(f'I can no longer {verb1} my feelings of {feeling1}. Every time I {sense} you, I am struck by how {adj1} you are. You are the most {adj2} {person1} on the {place}! I had to tell you how I feel, for fear my {body} will {verb2} from {feeling2}. If you share my feelings, you will make me the {feeling3}est {person2} ever! If not, I sincerely hope you will think of my {adj3} {noun} and reconsider.')
print(farewell + ',')
print(name2)