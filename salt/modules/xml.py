"""
XML file manager

.. versionadded:: 3000
"""

import logging
import defusedxml.ElementTree

log = logging.getLogger(__name__)


# Define the module's virtual name
__virtualname__ = "xml"


def __virtual__():
    """
    Only load the module if all modules are imported correctly.
    """
    return __virtualname__


def get_value(file, element):
    """
    Returns the value of the matched xpath element

    CLI Example:

    .. code-block:: bash

        salt '*' xml.get_value /tmp/test.xml ".//element"
    """
    try:
        root = defusedxml.ElementTree.parse(file)
        element = root.find(element)
        return element.text
    except AttributeError:
        log.error("Unable to find element matching %s", element)
        return False


def set_value(file, element, value):
    """
    Sets the value of the matched xpath element

    CLI Example:

    .. code-block:: bash

        salt '*' xml.set_value /tmp/test.xml ".//element" "new value"
    """
    try:
        root = defusedxml.ElementTree.parse(file)
        relement = root.find(element)
    except AttributeError:
        log.error("Unable to find element matching %s", element)
        return False
    relement.text = str(value)
    root.write(file)
    return True


def get_attribute(file, element):
    """
    Return the attributes of the matched xpath element.

    CLI Example:

    .. code-block:: bash

        salt '*' xml.get_attribute /tmp/test.xml ".//element[@id='3']"
    """
    try:
        root = defusedxml.ElementTree.parse(file)
        element = root.find(element)
        return element.attrib
    except AttributeError:
        log.error("Unable to find element matching %s", element)
        return False


def set_attribute(file, element, key, value):
    """
    Set the requested attribute key and value for matched xpath element.

    CLI Example:

    .. code-block:: bash

        salt '*' xml.set_attribute /tmp/test.xml ".//element[@id='3']" editedby "gal"
    """
    try:
        root = defusedxml.ElementTree.parse(file)
        element = root.find(element)
    except AttributeError:
        log.error("Unable to find element matching %s", element)
        return False
    element.set(key, str(value))
    root.write(file)
    return True
