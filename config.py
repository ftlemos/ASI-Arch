"""
Robust Config stub - returns dummy values for any missing attribute
so Pipeline can import without crashing
"""
class ConfigMeta(type):
    _defaults = {
        "DATABASE": "http://localhost:8000",
        "DATABASE_URL": "http://localhost:8000",
        "SOURCE_FILE": "/tmp/source.py",
        "OUTPUT_DIR": "/tmp/output",
        "LOG_DIR": "/tmp/logs",
        "DATA_DIR": "/tmp/data",
        "OPENAI_API_KEY": "sk-test",
        "AZURE_OPENAI_API_KEY": "dummy",
        "AZURE_OPENAI_ENDPOINT": "https://dummy.openai.azure.com/",
        "OPENAI_API_VERSION": "2023-05-15",
        "GEMINI_API_KEY": "",
        "MODEL": "gemini-2.0-flash",
        "LLM_MODEL": "gemini-2.0-flash",
    }
    def __getattr__(cls, name):
        # Return default if known, else a generic dummy path/string
        if name in cls._defaults:
            return cls._defaults[name]
        # For file/dir paths, return /tmp/...
        if "FILE" in name or "DIR" in name or "PATH" in name:
            return f"/tmp/{name.lower()}"
        # For everything else, return dummy string
        return "dummy"

class Config(metaclass=ConfigMeta):
    pass

# Also support from config import Config and import config
print("Config stub loaded with auto-fallback")
