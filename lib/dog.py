#!/usr/bin/env python3

class Dog:
    def __init__(self, speech="Woof!"):
        self.speech = speech

    def bark(self):
        print(self.speech)

    def sit(self):
        print("The dog is sitting.")
