class InsufficientBatteryError(Exception):
    def  __init__(self, robot_name: str, required: int, available: int):
        self.robot_name = robot_name
        self.required = required
        self.available = available

        message = f"Error: '{self.robot_name}' needs {self.required}% battery, but only has {self.available}%."

        super().__init__(message)