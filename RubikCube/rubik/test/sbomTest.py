'''
Created on Jan 17, 2023

@author: cailynhyun
'''
import unittest
import app


class SbomTest(unittest.TestCase):


    def test_sbom_100_ShouldReturnAuthorName(self):
        myName = 'yzh0068'
        result = app._getAuthor('../../')
        resultingAuthorName = result['author']
        self.assertEqual(resultingAuthorName, myName)