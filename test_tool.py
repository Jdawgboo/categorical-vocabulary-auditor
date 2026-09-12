import unittest
from tool import audit
class Tests(unittest.TestCase):
 def test_vocab(self): self.assertEqual(audit(['a','x'],{'a','b'}),{'unexpected':['x'],'unused_allowed':['b']})
if __name__=='__main__': unittest.main()
