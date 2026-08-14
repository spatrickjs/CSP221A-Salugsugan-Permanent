def log_action(func):
    def wrapper(self, *args, **kwargs):
        print(f"[LOG] Process: '{func.__name__}' for {self.name} started.")

        result = func(self, *args, **kwargs)

        print(f"[LOG] Process: '{func.__name__}' for {self.name} finished.")
        return result
    return wrapper