import unittest
import robot
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stderr, redirect_stdout

class TestRobot(unittest.TestCase):
    @patch("sys.stdin" , StringIO("HAL\nofF"))
    def test_inList1(self):
        result = robot.get_robot_name()
        self.assertEqual(result, 'HAL')
    

    @patch("sys.stdin", StringIO("off\n"))
    def test_off_command(self):
        with patch(('sys.stdout'), new = StringIO()) as fake:
            robot.get_command_input('HAL' , 'OFF', 0 ,0 , "anything" , 0)
            self.assertEqual("HAL: What must I do next? HAL: Shutting down..\n", fake.getvalue())

    @patch("sys.stdin", StringIO("help\n"))
    def test_help_command(self):
        with patch(('sys.stdout'), new = StringIO()) as fake:
            robot.get_command_input('HAL' , 'HELP', 0 ,0 , "" , 0)
            self.assertEqual("HAL: What must I do next? I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands\nFORWARD - move forward\nBACK - move backwards\nRIGHT - move right\nLEFT - move left\nSPRINT - burst of speed\n", fake.getvalue())

    @patch("sys.stdin", StringIO("forward 4\n"))
    def test_forward_command(self):
        with patch(('sys.stdout'), new = StringIO()) as fake:
            robot.get_command_input('HAL' , 'FORWARD', 0 , 0 , "" , 0)
            self.assertEqual("HAL: What must I do next?  > HAL moved forward by 4 steps.\n > HAL now at position (0,4).\n" , fake.getvalue())


    @patch("sys.stdin", StringIO("back 4\n"))
    def test_back_command(self):
        with patch(('sys.stdout'), new = StringIO()) as fake:
            robot.get_command_input('HAL' , 'BACK', 0 , 0 , "" , 0)
            self.assertEqual("HAL: What must I do next?  > HAL moved back by 4 steps.\n > HAL now at position (0,-4).\n" , fake.getvalue())

    @patch("sys.stdin", StringIO("FLY\n"))
    def test_invalid_command(self):
        with patch(('sys.stdout'), new = StringIO()) as fake:
            robot.get_command_input('HAL' , 'FLY', 0 , 0 , "" , 0)
            self.assertEqual("HAL: What must I do next? HAL: Sorry, I did not understand 'FLY'.\n" , fake.getvalue())

    @patch("sys.stdin", StringIO("sprint 4\n"))
    def test_sprint_command(self):
        with patch(('sys.stdout'), new = StringIO()) as fake:
            robot.get_command_input('HAL' , 'SPRINT', 0 , 0 , "" , 0)
            self.assertEqual("HAL: What must I do next?  > HAL moved forward by 4 steps.\n > HAL moved forward by 3 steps.\n > HAL moved forward by 2 steps.\n > HAL moved forward by 1 steps.\n > HAL now at position (0,10).\n" , fake.getvalue())       
    
    @patch("sys.stdin", StringIO("sprinT 240\n"))
    def test_OutOfBounds(self):
        with patch(('sys.stdout'), new = StringIO()) as fake:
            robot.get_command_input('HAL' , ['SPRINT',' FORWARD'], 0 , 0 , "" , 0)
            self.assertEqual("HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.\n > HAL now at position (0,0).\n" , fake.getvalue())

    @patch("sys.stdin", StringIO("left\n"))
    def test_right_command(self):
        with patch(('sys.stdout'), new = StringIO()) as fake:
            robot.get_command_input('HAL' , 'LEFT', 0 , 0 , "" , 0)
            self.assertEqual("HAL: What must I do next?  > HAL turned left.\n > HAL now at position (0,0).\n" , fake.getvalue())

    @patch("sys.stdin", StringIO("right\n"))
    def test_left_command(self):
        with patch(('sys.stdout'), new = StringIO()) as fake:
            robot.get_command_input('HAL' , 'RIGHT', 0 , 0 , "" , 0)
            self.assertEqual("HAL: What must I do next?  > HAL turned right.\n > HAL now at position (0,0).\n" , fake.getvalue())            

   
     
     

