# coding:utf-8
import markdown
import a_markdown_test 
import unittest
class TextClass(unittest.TestCase):
    def test_extends(self):
        import markdown
        md = markdown.Markdown(extensions=['a_markdown_test'])

        #日本語を単独で使えるようにしたい 
        text = '''{{{##title
hoge
}}}'''
        print(md.convert(text))

if __name__ == "__main__":
    unittest.main()
