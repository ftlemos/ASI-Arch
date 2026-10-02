# Stub for deleted ASI-Arch helpers
# Original functions just set global OpenAI config; now we use env vars

def set_default_openai_api(api_type: str = "chat_completions"):
    """No-op stub — kept for compatibility."""
    import os
    os.environ.setdefault("OPENAI_API_TYPE", api_type)

def set_default_openai_client(client=None):
    """No-op stub."""
    return client

def set_tracing_disabled(disabled: bool = True):
    """No-op stub."""
    import os
    os.environ["TRACING_DISABLED"] = str(disabled)
