from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):


#F - Front closckwise
#f - Front counterclockwise
#R - Right clockwise
#r - Right counterclockwise
#B - Back clockwise
#b - Back counterclockwise
#L - Left clockwise
#l - Left counterclowise
#U - Up clockwise
#u - Up counterclockwise

    '''expect to get 'error:invalid direction'/'''
    def test910_missingDirection(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = ''
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid direction', result['status'])
    
    '''exepct to get no error'''
    def test110_noError(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        
    '''expect to get 'error:invalid direction'/'''
    def test120_noDirection(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = ''
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid direction', result['status'])
    
    '''expect to get 'error:invalid cube'/'''
    def test130_noCube(self):
        encodedCube = ''
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    '''expect to get 'error:extraneous key detected'/'''
    def test150_extraKeyCube(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwwq'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: extraneous key detected', result['status'])
        
        
        
        
        
        
        
        
        