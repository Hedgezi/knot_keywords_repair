import unittest
from main import *

class KeywordVariationsTest(unittest.TestCase):
    def test_index_terms_dash(self):
        keywords = extractKeywordsAsList("test_samples/keyword_variations/Index_Terms_dash.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["Value Stream Mapping (VSM)", "Lean Production", "Takt time", "Production-Lead Time", "Current State Map" ,"Future State Map"])  

    def test_Key_terms_dash(self):
        keywords = extractKeywordsAsList("test_samples/keyword_variations/Key_terms_dash.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["power factor", "power factor correction", "total harmonic distortion", "interleaved boost converter", "single stage converter", "pulse width modulation"])  

    def test_Key_word_dash(self):
        keywords = extractKeywordsAsList("test_samples/keyword_variations/Key_word_dash.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["Accuracy", "linearity", "potentiometric titration", "stability", "total alkalinity", "water"])  
    
    def test_Key_words_colon(self):
        keywords = extractKeywordsAsList("test_samples/keyword_variations/Key_words_colon.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["argumentation", "Science", "didactic sequence", "Living Machine", "dynamic model v"])  

    def test_Key_Words(self):
        keywords = extractKeywordsAsList("test_samples/keyword_variations/Key_Words.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["Cerebrovascular disease", "Moyamoya", "intracerebral hemorrhage", "Progressive Intracranial Occlusive Arteropathy", "Colombia"])  
    
    def test_KEY_WORDS(self):
        keywords = extractKeywordsAsList("test_samples/keyword_variations/KEY_WORDS.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["Demand technological", "productive sector"])  

    def test_Key_dash_Words_colon(self):
        keywords = extractKeywordsAsList("test_samples/keyword_variations/Key-Words_colon.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["-PWM", "Solar management unit", "Switching devices", "Solar energy", "Inverter", "Load", "Relay", "Battery"])  

    def test_Keyword_colon(self):
        keywords = extractKeywordsAsList("test_samples/keyword_variations/Keyword_colon.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["Reading Comprehension", "Classroom Action Research", "Directed Reading Thinking Activity (DRTA) Strategy"])  

    def test_Keyword_dash(self):
        keywords = extractKeywordsAsList("test_samples/keyword_variations/Keyword_dash.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["Fault Tolerance", "Mobile Computing Systems", "Coordinated Checkpointing", "Rollback Recovery", "Distributed Systems"])  

    def test_Keyword_space_colon(self):
        keywords = extractKeywordsAsList("test_samples/keyword_variations/Keyword_space_colon.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["Vocabulary", "Anagram Plus Flashcard"])  

    def test_Keyword(self):
        keywords = extractKeywordsAsList("test_samples/keyword_variations/Keyword.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["Dietary patterns", "Factor analysis", "Indonesia", "Jakarta", "Oral cancer"])  

    def test_KJWVORDS_colon(self):
        keywords = extractKeywordsAsList("test_samples/keyword_variations/KJWVORDS_colon.tei.xml", PREFIX)
        allproblems = checkForProblems(keywords)
        repaired = repairPossibleProblems(keywords, allproblems)
        self.assertEqual(repaired, ["Cape Tribulation", "fringing reef", "siltation", "sea-level high"])  


    
        

    
    
    



    

    

    

    

    




if __name__ == '__main__':
    unittest.main()