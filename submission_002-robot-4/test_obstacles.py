import unittest
import world.obstacles

class TestObstacles(unittest.TestCase):
    '''Test if get obstacles returns a list'''
    def test_get_obstacles(self):
        result = world.obstacles.get_obstacles()
        self.assertTrue(type(result),list)
    
    '''Test if is_position blocked returns false when position not blocked.''' 
    def test_isposition_blocked(self):
        result = world.obstacles.is_position_blocked(3,8)
        self.assertEquals(result, False)

    '''Test if is_path blocked returns false when position not blocked.'''
    def test_is_path_blocked(self):
        result = world.obstacles.is_path_blocked(4,7,7,9)
        self.assertEquals(result, False)
