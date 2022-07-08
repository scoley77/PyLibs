from random import randint

print("Welcome to PyLibs!")
print("To get started, enter a number from 1-4, or enter 5 for a random story!")
story_selection = input().strip()

def branch_off(selector):
  if selector == '1':
    import story1
  elif selector == '2':
    import story2
  elif selector == '3':
    import story3
  elif selector == '4':
    import story4
  else:
    print('Oops! That wasn\'t one of the options...')
    
if story_selection == '5':
  branch_off(str(randint(1,4)))
else:
  branch_off(story_selection)