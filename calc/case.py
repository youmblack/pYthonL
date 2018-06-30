#!/usr/bin/env python
# coding=utf-8

class Animal:

    def __init__(self):
        pass
    def leg(self):
        pass
    def eat(self):
        pass

class Dog(Animal):

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.bark = []
    
    def get_bark(self, bark):
        self.bark.append(bark) 




