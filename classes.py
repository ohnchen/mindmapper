#!/usr/bin/env python

class Topic():
    def __init__(self, name, color="black"):
        self.name = name
        self.color = color
    
    def __repr__(self):
        return f'Topic: \"{self.name.title()}\" in {self.color}'

class Subtopic():
    def __init__(self, name, color="black"):
        self.name = name
        self.color = color    
    
    def __repr__(self):
        return f'Subtopic: \"{self.name.title()}\" in {self.color}'    

