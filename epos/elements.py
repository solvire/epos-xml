# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from abc import ABCMeta, abstractmethod

class ePOSElement:
    """
    Base class for the various elements in the ePOS object
    """
    __metaclass__ = ABCMeta

    text = None
    attr = {}
    # list of dicts
    local_attributes = {}
    required_attributes = []

    def __init__(self, text=None, attr=None):
        self.text = text
        if attr is not None:
            self.attr = attr

    @abstractmethod
    def get_tag(self):
        pass

    def get_attr(self):
        return self.clean_attributes()

    def clean_attributes(self):
        cleaned = {}

        for a in self.attr:
            if a in self.local_attributes:
                self.local_attributes[a] = self.attr[a]

        for k, v in self.local_attributes.iteritems():
            if v is not None:
                cleaned[k] = v

        return cleaned

    def get_text(self):
        return self.text

class Text(ePOSElement):
    """
    Text object
    """
    tag = 'text'

    def get_tag(self):
        return self.tag

    def get_text(self):
        return self.text + "\n"

class Feed(ePOSElement):
    """
    Line Feed Object
    """
    tag = 'feed'
    local_attributes = {
        "unit": None,
        "line": None,
        "linespc": None,
        "pos": None,
    }

    def get_tag(self):
        return self.tag

    def get_attr(self):
        return self.clean_attributes()


class Image(ePOSElement):
    """
    An Image object
    """
    tag = 'image'
    local_attributes = {
        "width": None,
        "height": None,
        "color": None,
        "align": None,
        "mode": None,
    }

    def get_tag(self):
        return self.tag

class Logo(ePOSElement):
    """
    Print a logo that was previously registered with the printer
    """
    tag = 'logo'
    local_attributes = {
        "key1": None,
        "key2": None,
        "align": None,
    }

    def get_tag(self):
        return self.tag

class Barcode(ePOSElement):
    """
    A barcode object
    """
    tag = 'barcode'
    required_attributes = ['type']

    local_attributes = {
        "type": None,
        "hri": None,
        "width": None,
        "height": None,
        "font": None,
        "align": None,
        "rotate": None,
    }

    def get_tag(self):
        return self.tag

class Symbol(ePOSElement):
    """
    A symbol from the ePOS sdk
    Usually a 2D barcode
    """
    tag = 'symbol'
    data = ""
    symbol_type = "pdf417_standard"

    def get_attr(self):
        return {
            "type": self.symbol_type,
            "level": "default",
            "width": "3",
            "height": "0",
            "size": "0"
        }

    def get_tag(self):
        return self.tag

class Hline(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class VlineBegin(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class VlineEnd(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class Page(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class Area(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class Direction(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class Position(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class Line(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class Rectangle(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class Cut(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class Pulse(ePOSElement):
    """
    Send a pulse signal to the printer
    Usually to kick the cash drawer
    """
    tag = "pulse"

    local_attributes = {
        "drawer": "drawer_1",
        "time": "pulse_100"
    }
    def get_tag(self):
        return self.tag

class Sound(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class Command(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class Layout(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class Recovery(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag

class Rest(ePOSElement):
    tag = None
    def get_tag(self):
        return self.tag
