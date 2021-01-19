# coding:utf-8
import markdown
from markdown import Extension
from markdown.preprocessors import Preprocessor
from markdown.inlinepatterns import InlineProcessor
from markdown.inlinepatterns import Pattern
from markdown.inlinepatterns import SimpleTagInlineProcessor
import xml.etree.ElementTree as etree

import unittest


def makeExtension(*args, **kwargs):
    return MyExtension(*args, **kwargs)

class MyExtension(Extension):
    def extendMarkdown(self, md ):
        self.RE = r'!!(.*?)!!'
        md.inlinePatterns.register(MyClass( self.RE ,md ),'name',175)

class MyClass(SimpleTagInlineProcessor):
    def handleMatch(self, m ,tag):
        return ""

class TextClass(unittest.TestCase):
    def test_extends(self):
        import markdown
        md = markdown.Markdown(extensions=['a_markdown_test'])
        text = '''aaa
bbb
--ccc--
ddd'''
        text = "!!aa!!"
        print(md.convert(text))

if __name__ == "__main__":
    unittest.main()
    
