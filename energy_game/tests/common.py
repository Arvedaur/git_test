BASE_URL = "http://127.0.0.1:8000"

def assert_true(cond, msg):
    if not cond:
        raise AssertionError(msg)
