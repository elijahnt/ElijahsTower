import random
import time

def clear():
  print("\n" * 10)


def displayIntro():
  intro_options = ["1","2"]
  UserChoice=""
  while UserChoice not in intro_options:
    print('''Welcome to the Tower of Elijah, v.1
Humanity has been nearly destroyed by an attack
by the Demon Lucifer himself, but Humanity is still
fighting back. You have two choices so far on how
to start the story.

  1) Be a Demon Spawn from Hell itself to destroy Humanity.
  2) Be an Angelic Offspring to save Humanity.
  ''')

    UserChoice = str(input("Enter Option Number: "))
  print("You have selected choice " + UserChoice)
  if UserChoice == intro_options[0]:
    room1()
  elif UserChoice == intro_options[1]:
    room2()

def room1():
  clear()
  r1o = ["1","2"]
  c=""
  while c not in r1o:
    print('''>You are currently in Kyos, the Demon Capitol in the Overworld. You are
the son of Satan, yet a disappointment to him. You aren't as strong as the other
Demons, and he hates you for that. However, you still have his blood running
through your genes. You have a few choices with what to do from here.
You currently have two choices:

  1) Try to raid small homes or villages.
  2) Find a single human to torture for a while, testing your abilities.''')

    c = str(input("Enter Option Number: "))
  print("You have chosen " + c)
  if c = r1o[0]:
    raid()
  elif c = r1o[1]:
    torture()

def raid():
  raido = ["1","2","3"]
  clear()
  c=""
  while c not in raido:
    print('''>Warping into a nearby village, one of the Watchmen noticied you immediately.
and alerted their members. This is forcing you to go into a sneaky approach. Currently,
it is Daytime (High Enemy Awareness) and the Weather is Clear (High Enemy Visibility).
You can use three different spells:

 1) Invisibilty and take them out one by one.
 2) Change into human form and sneak in.
 3) Run away.''')

    c = str(input("Enter Option

def room2():
    clear()
    r2o = ["1","2"]
    c=""
    print('''> You are currently in Migard, the Human Sanctuary.
Your mother, Kyla, was one of the most powerful Angelic
beings of all time. Even Lucifer feared her at points, until her death
when she sacrificed herself to save humankind, and most importantly, you.
This blood runs through your veins, don't forget that. With these powers,
you have two choices:

  1) Find a local terrorizing demon.
  2) Help out civilians.''')

    c = str(input("Enter Option Number: "))
  print("You have chosen " + c)
  if c = r2o[0]:
    local()
  if c = r2o[1]:
    civi()

def 

displayIntro()
