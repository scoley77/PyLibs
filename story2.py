print("Ok! Let's get going!")

noun1 = input('a noun:').strip()
adj1 = input('an adjective:').strip()
noun2 = input('a noun:').strip()
noun3 = input('a noun:').strip()
house = input('part of a house:').strip()
person1 = input('type of person:').strip()
adj2 = input('an adjective:').strip()
animal1 = input('an animal:').strip()
adj3 = input('an adjective:').strip()
person2 = input('type of person:').strip()
adj4 = input('an adjective:').strip()
animal2 = input('an animal:').strip()
face = input('a facial expression:').strip() + "ed"
greeting = input('a greeting:').strip()

print(f'Once upon a {noun1}, there was a/an {adj1} {noun2}, who lived in a {noun3}. As she sat at her {house}, she dreamed that a {person1} would come riding a/an {adj2} {animal1} to save her from her {adj3} life.')
print(f'One day, she saw him. A {person2} on a {adj4} {animal2}. It wasn\'t quite what she had imagined, but then he {face} and said,"{greeting}."')