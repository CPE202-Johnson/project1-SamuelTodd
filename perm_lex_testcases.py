import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        # test for an empty string
        self.assertEqual(perm_lex.perm_gen_lex(''), [])

        # test for a single character string
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])

        # default test for a two character string
        self.assertEqual(perm_lex.perm_gen_lex('ab'), ['ab','ba'])

        # test for a three letter string
        self.assertEqual(perm_lex.perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

if __name__ == "__main__":
        unittest.main()
