import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_print(self):
        node = HTMLNode("a", "hello world", None, {"href": "https://www.google.com"})
        print(node)

    # def test_props(self):
    #     node = HTMLNode("a", "hello world", None, {"href": "https://www.google.com"})
    #     node.props_to_html()
        
