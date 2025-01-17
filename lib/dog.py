#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    APPROVED_BREEDS = ["Labrador", "Golden Retriever", "Bulldog", "Poodle", "German Shepherd"]

    def __init__(self,name,breed):
        self.name= name
        self.breed= breed
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if isinstance(value, str) and 1<= len(value) <=25:
            self._name= value
        else:
            print("Name must be a string between 1 and 25 characters.")
    
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self,value):
        if value in Dog.APPROVED_BREEDS:
            self._breed= value
        else:
            print("Breed must be in the list of approved breeds.")