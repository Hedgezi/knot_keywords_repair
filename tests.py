import unittest
from main import *

class KeywordsWordTest(unittest.TestCase):
    def testA(self):
        keywords = extractKeywordsAsList("examples/1.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["Radiology"])
    def testB(self):
        keywords = extractKeywordsAsList("examples/2.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["body orientation", "camouflage"])
    def testC(self):
        keywords = extractKeywordsAsList("examples/3.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["body orientation", "camouflage"])
    def testD(self):
        keywords = extractKeywordsAsList("examples/4.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["Generalized hypergeometric series", "Quadratic transformation", "Summation theorems"])

class ColonTest(unittest.TestCase):
    def testA(self):
        keywords = extractKeywordsAsList("examples/5.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["body orientation", "camouflage"])

if __name__ == '__main__':
    unittest.main()