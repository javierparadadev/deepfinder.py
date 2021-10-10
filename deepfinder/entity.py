import builtins

from deepfinder import deep_find


class DeepFinderList(list):
    def deep_find(self, path: str):
        return deep_find(self, path)


class DeepFinderDict(dict):
    def deep_find(self, path: str):
        return deep_find(self, path)


def nativify():
    builtins.list = DeepFinderList
    builtins.dict = DeepFinderDict
