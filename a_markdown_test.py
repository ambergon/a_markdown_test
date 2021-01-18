# coding:utf-8
import markdown
from markdown import Extension
from markdown.preprocessors import Preprocessor

import unittest

class MyExtension(Extension):
    def extendMarkdown(self, md ):
        # my_markdown = MyClass(md)
        # md.preprocessors['name'] = my_markdown

        md.preprocessors.register(MyClass(md.parser),'name',175)


        #md.parser.preprocessors.register(MyClass(md.parser)),name
        #md.inlinePattern
        #detail&summary
        #md.parser.blockprocessors.register(DetailBlock(md.parser),'box',175)

class MyClass(Preprocessor):
    def run( self , lines ):
        new_lines = []
        for line in lines:
            print(line)
            line = line + 'aa'
            new_lines.append(line)
        return new_lines

#class DetailBlock(BlockProcessor):
#    def test(self,parent,block):
#        return re.match(RE_FENCE_START,block)

#    def run(self,parent,blocks):
#        original_block = blocks[0]

#        pattern = re.compile(RE_FENCE_START)
#        match = pattern.search(blocks[0])
#        title = match.group("title")
#        cls = match.group("class")
#        cls_str=''
#        if cls != "" :
#            count = len(cls)
#            cls_str=cls_str + 'h'+str(count)

#        blocks[0] = re.sub(RE_FENCE_START,'',blocks[0])

#        for block_num,block in enumerate(blocks):
#            if re.search(RE_FENCE_END,block):
#                blocks[block_num] = re.sub(RE_FENCE_END,'',block)
#                e = etree.SubElement(parent,'details')

#                summary = markdown.util.etree.SubElement( e , "summary")
#                summary.set("class", cls_str )
#                summary.text = markdown.util.AtomicString(title)

#                #e.set('open','')
#                #e.set('style','display: inline-block; border: 1px solid red;')
#                self.parser.parseBlocks(e,blocks[0:block_num + 1])
#                for i in range(0,block_num + 1):
#                    blocks.pop(0)
#                return True
#        blocks[0] = original_block
#        return False

def makeExtension(*args, **kwargs):
    return MyExtension(*args, **kwargs)

class TextClass(unittest.TestCase):
    def test_extends(self):
        import markdown
        md = markdown.Markdown(extensions=['a_markdown_test'])

        text = '''aaa
bbb
ccc
ddd'''
        print(md.convert(text))

if __name__ == "__main__":
    unittest.main()
    
