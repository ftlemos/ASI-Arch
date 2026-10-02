"""
Minimal agents stub compatible with ASI-Arch
Replaces the private 'agents' package that isn't in the repo
"""
def function_tool(func=None, **kwargs):
    """Decorator that ASI-Arch uses to register tools - in mock mode just returns func"""
    if func is None:
        def decorator(f):
            f._is_function_tool = True
            return f
        return decorator
    func._is_function_tool = True
    return func

class Agent:
    def __init__(self, *args, **kwargs):
        pass
    def run(self, *args, **kwargs):
        return {"mock": True}

class Runner:
    @staticmethod
    def run(*args, **kwargs):
        return {"mock": True}

# For any other imports like from agents import xxx
def __getattr__(name):
    # Return dummy for anything else
    return function_tool

print("agents stub loaded with function_tool")
