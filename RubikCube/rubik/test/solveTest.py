from unittest import TestCase
from rubik.view.solve import solve
 

class SolveTest(TestCase):
        
# Happy path
#    Test that the stubbed solve returns the correct result
    '''
    def test100_solve_returnStubbedSolution(self):
        parms = {}
        parms['cube'] = 'rrrrrrrrrgggggggggbbbbbbbbboooooooooyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        #self.assertEqual('RBLUD', result.get('solution'))
    '''
    def test110_solve_returnEmptySolution(self):
        parms = {}
        parms['cube'] = 'rrrrrrrrrgggggggggbbbbbbbbboooooooooyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        
    def test120_solve_returnSolution(self):
        parms = {}
        parms['cube'] = 'ggbybgobwwbbyrroroyorbgogggyorgorwygbbowyyyrrwwbowwrwy'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)




