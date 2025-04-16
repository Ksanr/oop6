# -*- coding: utf-8 -*-

__author__ = 'sobolevn'

from utils import get_input_function


class Storage(object):  # storage = Storge()
    obj = None

    items = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj


class BaseItem(object):
    def __init__(self, heading, done=False):
        self.heading = heading
        self.done = done

    def __repr__(self):
        return self.__class__

    @classmethod
    def construct(cls):
        raise NotImplemented()

    def __str__(self):
        return f'{self.heading} for {('-', '+')[self.done]}'

    def to_done(self):
        self.done = True

    def to_undone(self):
        self.done = False


class ToDoItem(BaseItem):
    def __str__(self):
        return f'ToDo: {self.heading}. Done: {('-', '+')[self.done]}'

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        return ToDoItem(heading)

class ToBuyItem(BaseItem):
    def __init__(self, heading, price):
        super(ToBuyItem, self).__init__(heading)
        self.price = price

    def __str__(self):
        return f'ToBuy: {self.heading} for {self.price}. Done: {('-', '+')[self.done]}'

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        price = input_function('Input price: ')
        return ToBuyItem(heading, price)

class ToReadItem(BaseItem):
    def __init__(self, heading, url):
        super(ToReadItem, self).__init__(heading)
        self.url = url

    def __str__(self):
        return f'ToRead: {self.heading} {self.url}. Done: {('-', '+')[self.done]}'

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        url = input_function('Input url: ')
        return ToReadItem(heading, url)


