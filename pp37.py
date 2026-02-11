import random
characters=['😸','🐶','🎅','🕵️‍♀️','🧛‍','🐿']
places=['🏰','🏍','🌌','🏝','🛸']
actions=['fought','found','rescued','hid from','talked to']
objects=['a treasure','a dragon egg','a magic wand','a spaceship','a golden banana']
def generate_story():
    character=random.choice(characters)
    place=random.choice(places)
    action=random.choice(actions)
    obj=random.choice(objects)
    story=f"One day, {character}  went to  {place}  and  {action} {obj}!"
    return story
for i in range(5):
    print(generate_story())
