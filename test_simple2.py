#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/txkaur/Development/code/phase-3/python-p3-instance-methods/lib')

from person import Person
from dog import Dog

print("Testing Person...")
p = Person()
p.talk()
p.walk()

print("\nTesting Dog...")
d = Dog("Woof!")
d.bark()
d.sit()

print("\nAll tests passed!")

