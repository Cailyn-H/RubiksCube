'''
Created on Jan 27, 2023

@author: cailynhyun
'''
import unittest 
import rubik.model.cube as cube


class CubeTest(unittest.TestCase):


    def test_rotate_010_F_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F')
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('ok', rotatedCube['status'])
    
    def test_rotate_015_f_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('f')
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('ok', rotatedCube['status'])
        
    def test_rotate_020_R_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('R') #R - Right clockwise 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('ok', rotatedCube['status'])
        
    def test_rotate_025_r_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('r') 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('ok', rotatedCube['status'])
    
    def test_rotate_030_B_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('B') 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('ok', rotatedCube['status'])
    
    def test_rotate_035_b_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('b') 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('ok', rotatedCube['status'])
    
    def test_rotate_040_L_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('L') 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('ok', rotatedCube['status'])
    
    def test_rotate_045_l_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('l') 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('ok', rotatedCube['status'])
    
    def test_rotate_050_U_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('U') 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('ok', rotatedCube['status'])
        
    def test_rotate_055_u_Rotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('u') 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('ok', rotatedCube['status'])
    
    def test_rotate_100_missingDirection(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate(None) 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('error: invalid direction', rotatedCube['status'])
    
    def test_rotate_110_emptyDirection(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate("") 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('error: invalid direction', rotatedCube['status'])
        
    def test_rotate_120_multipleRotation(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('uLBf') 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('ok', rotatedCube['status'])
    
    def test_rotate_130_missingCube(self):
        theCube = cube.Cube(None)
        rotatedCube = theCube.rotate('F') 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('error: invalid cube', rotatedCube['status'])
    
    def test_rotate_140_emptyCube(self):
        cubeToRotate=''
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F') 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('error: invalid cube', rotatedCube['status'])
    
    def test150_extraKeyCube(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrroooooooookggkgggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F') 
        self.assertEqual(rotatedCube['cube'], theCube.get())
        self.assertEqual('error: extraneous key detected', rotatedCube['status'])
        
    def test_rotate_910_invalidDirection(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('K') 
        self.assertEqual('error: invalid direction', rotatedCube['status'])
    
    def test_rotate_920_invalidCube(self):
        cubeToRotate='bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwwwqqqqqqqqq'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F') 
        self.assertEqual('error: invalid cube', rotatedCube['status'])
        
        
        
        
        