#!/usr/bin/env python3
from lib.person import Person
from lib.dog import Dog

print("Testing Person...")
p = Person()
p.talk()
p.walk()

print("\nTesting Dog...")
d = Dog("Woof!")
d.bark()
d.sit()

print("\nAll tests passed!")

