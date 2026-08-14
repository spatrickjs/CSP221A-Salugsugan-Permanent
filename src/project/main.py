from abc import ABC, abstractmethod

def log_action(func):
    def wrapper(self, *args, **kwargs):
        print(f"[LOG] Process: '{func.__name__}' for {self.name} started.")

        result = func(self, *args, **kwargs)

        print(f"[LOG] Process: '{func.__name__}' for {self.name} finished.")
        return result
    return wrapper

class InsufficientBatteryError(Exception):
    def  __init__(self, robot_name: str, required: int, available: int):
        self.robot_name = robot_name
        self.required = required
        self.available = available

        message = f"Error: '{self.robot_name}' needs {self.required}% battery, but only has {self.available}%."

        super().__init__(message)
    pass

class Robot(ABC):
    manufacturer = "Robots"
    population  = 0

    repair_history = []

    def __init__(self, name: str, battery: int = 100):
        self.name = name
        self._battery = 0
        self.battery = battery

        Robot.population += 1

    @classmethod
    def from_dict(cls, config: dict):
        return cls(**config)

    @property
    def battery(self) -> int:
        return self._battery
    
    @battery.setter
    def battery(self, value: int):
        if value < 0:
            self._battery = 0
        elif value > 100:
            self._battery = 100
        else:
            self._battery = value

    def __str__(self) -> str:
        return f"{self.name} ({self.battery}%battery)"
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', battery={self.battery})"

    @abstractmethod
    def perform_task(self):
        pass

class CleaningRobot(Robot):
    def __init__(self, name: str, battery: int = 100, dust_capacity: int = 5):
        super().__init__(name, battery)
        self.dust_capacity = dust_capacity
        self.task_cost = 15  # Cleaning battery cost

    @log_action
    def perform_task(self):
        if self.battery < self.task_cost:
            raise InsufficientBatteryError(self.name, self.task_cost, self.battery)

        self.battery -= self.task_cost
        print(f"{self.name} is cleaning. (Dust capacity: {self.dust_capacity})")

class SecurityRobot(Robot):
    def __init__(self, name: str, battery: int = 100, patrol_zone: str = "Zone 1"):
        super().__init__(name, battery)
        self.patrol_zone = patrol_zone
        self.task_cost = 30 # Patrol battery cost

    @log_action
    def perform_task(self):
        if self.battery < self.task_cost:
            raise InsufficientBatteryError(self.name, self.task_cost, self.battery)

        self.battery -= self.task_cost
        print(f"{self.name} is patrolling {self.patrol_zone}ft.")

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
    
