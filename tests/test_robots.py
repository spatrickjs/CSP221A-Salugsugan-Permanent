import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from project.main import CleaningRobot, SecurityRobot, InsufficientBatteryError

class TestRobots(unittest.TestCase):
    def test_battery_limits(self):
        # Test battery if values are above 100 and below 0.
        robot = CleaningRobot("TestRobot", battery = 150)
        self.assertEqual(robot.battery, 100)

    def test_battery_consumption(self):
        # Test battery consumtipon after performing task.
        robot = CleaningRobot("TestRobot", battery = 100)
        robot.perform_task() # Cleaning battery cost is 15
        self.assertEqual(robot.battery, 85)

    def test_insufficient_battery(self):
        # Test if InsufficientBatteryError is raised if battery is below the required amount for the task.
        security = SecurityRobot("SecurityBot", battery = 10, patrol_zone = "Zone  1")
        with self.assertRaises(InsufficientBatteryError):
            security.perform_task()

if __name__ == '__main__':
    unittest.main()
