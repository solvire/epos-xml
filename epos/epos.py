# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import xml.etree.ElementTree as ET
# from django.utils.translation import ugettext as _

class ePOSDocument(object):
    """
    The main document for the ePOS XML printing
    """
    line_items = []

    def __init__(self):
        self.line_items = []

    def append_row(self, element):
        self.line_items.append(element)

    def xml(self):
        """
        Take the main document object and return an XML rendering
        """

        exml = ET.Element("epos-print", {"xmlns":"http://www.epson-pos.com/schemas/2011/03/epos-print"})
        for obj in self.line_items:
            o = ET.SubElement(exml, tag=obj.get_tag(), attrib=obj.get_attr())
            txt = obj.get_text()
            if txt is not None:
                o.text = obj.get_text()

        return ET.tostring(exml)
