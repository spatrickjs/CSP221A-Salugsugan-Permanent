import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from project.main import CleaningRobot, SecurityRobot, InsufficientBatteryError, fleet_report, run_task_safely

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

    # Test fleet_report and run_task_safely functions
    def test_fleet_report_execution(self):
        robots = [
            CleaningRobot("Cleaner1", battery = 100),
            SecurityRobot("Security1", battery = 100)
        ]

        fleet_report(robots)

    def test_run_task_safely_success(self):
        robot = CleaningRobot("Cleaner1", battery = 100)
        run_task_safely(robot)

    def test_run_task_safely_insufficient_batter(self):
        # Test if function handles insufficient battery correctly
        robot = CleaningRobot("Cleaner2", battery = 10)
        run_task_safely(robot)

    #test constructor
    def test_alternative_constructor(self):
        cleaner_config = {"name": "AutoClean", "battery": 75, "dust_capacity": 10}

        new_robot = CleaningRobot.from_dict(cleaner_config)

        self.assertEqual(new_robot.name, "AutoClean")
        self.assertEqual(new_robot.battery, 75)
        self.assertEqual(new_robot.dust_capacity, 10)
        self.assertIsInstance(new_robot, CleaningRobot)

    #test trap
    def test_mutable_attribute_trap(self):
        bot1 = CleaningRobot("TrapRobot1")
        bot2 = SecurityRobot("TrapRobot2")

        bot1.repair_history.append("Repaired hardware")

        self.assertEqual(len(bot2.repair_history),  1)
        self.assertIn("Repaired hardware", bot2.repair_history)
        self.assertIs(bot1.repair_history, bot2.repair_history)

if __name__ == '__main__':
    unittest.main()
