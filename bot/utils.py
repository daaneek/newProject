import json
from  typing import Generator

class ListDictionari:
    ...




class FileDictionari:
    def __init__(self, dictionari: Generator, dict_name: str):
        self.name = dict_name
        self.__dict = self.yield_build(dictionari)
    
    @staticmethod
    def yield_build(dictionari):
        yield dictionari
    
    def get_dict(self):
        value = next(self.__dict)
        self.__dict = self.yield_build(value)
        return value

    @classmethod
    def from_open(cls, path_dictionari: str):
        with open(file=path_dictionari, mode="r") as file:
            return cls(json.loads(file), path_dictionari)