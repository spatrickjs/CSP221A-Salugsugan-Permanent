from .exceptions import InsufficientBatteryError
from .robots import CleaningRobot, SecurityRobot

def fleet_report(robots):
    for robot in robots:
        try:
            robot.perform_task()
        except InsufficientBatteryError as error:
            print(f"[{robot.name} FAILED] {error}")

def run_task_safely(robot):
    try:
        # Perform task that could raise an InsuffiecientBatteryError
        robot.perform_task()
    except InsufficientBatteryError as e:
        print(f"[ALERT] {e}")
    else:
        print(f"[SUCCESS] {robot.name} completed the task successfully.")

    finally:
        print(f"[LOG] Task attempt for {robot.name} finished. Current battery: {robot.battery}%.")
    
