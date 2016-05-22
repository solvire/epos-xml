===============================
epos-xml
===============================

.. image:: https://img.shields.io/pypi/v/epos-xml.svg
        :target: https://pypi.python.org/pypi/epos-xml

.. image:: https://img.shields.io/travis/solvire/epos-xml.svg
        :target: https://travis-ci.org/solvire/epos-xml

.. image:: https://readthedocs.org/projects/epos-xml/badge/?version=latest
        :target: https://readthedocs.org/projects/epos-xml/?badge=latest
        :alt: Documentation Status


Epson ePOS-Print XML Wrapper

* Free software: ISC license
* Documentation: https://epos-xml.readthedocs.org.

Features
--------

Epson ePOS-Print XML Wrapper
============================

A small library for generating the XML required to communicate with ePOS
enabled Epson POS printing devices.

Epson ePOS-Print API
====================

Epson provides an API for communicating with the POS priters via
HTTP/HTTPS from any TPC capable device. This includes browsers, mobile
devices, embedded systems and local servers.

For more information regarding documentation from Epson please see this
link:
https://c4b.epson-biz.com/modules/community/index.php?content\_id=3

Download information regarding the

Epson ePOS-Print XML
--------------------

The API allows for the communication with the device via SOAP/XML. There
are detailed instructions concerning the XML Schema and the format of
the data. This utility was initially designed based off the
documentation provided in the users manual. If the device/firmware/API
have changed since this publication the XML produced may not work.

ePOS-Print XML User’s Manual - M00048210 Rev. K

Device Testing and Communication
--------------------------------

Communication test were only performed on a TM-88V with ethernet module
UB-E04 firmware 4.0 software version 1.02. If you are using hardware or
firmware versions other than this your results may vary.

Library
=======

Installation
------------

``pip install epos-xml``

The main entry point to the library is the ``epos`` module.

.. code:: python


    from datetime import datetime
    from epos-xml import epos, elements


    doc = epos.ePOSDocument()

    doc.append_row(elements.Text('A Receipt'))
    doc.append_row(elements.Text("\n"))
    doc.append_row(elements.Text("Test Business Name")
    doc.append_row(elements.Text("Date " + str(datetime.now())))
    doc.append_row(elements.Text("\n"))
    doc.append_row(elements.Symbol('http://dtac.io')
    doc.append_row(elements.Feed())
    doc.append_row(elements.Cut())


    print doc.xml()

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
