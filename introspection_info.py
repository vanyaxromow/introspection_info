from inspect import getmodule
import sys


class SomeClass:
    def __init__(self):
        self.num = 42


some_obj = SomeClass()


def introspection_info(obj):
    lst = [type, id, dir, getmodule]
    lst_2 = ['type', 'id', 'attributes, methods', 'module']
    dict_ = {}
    for i, val in enumerate(lst):
        dict_[lst_2[i]] = val(obj)
    return dict_


number_info = introspection_info(some_obj)
print(number_info)
