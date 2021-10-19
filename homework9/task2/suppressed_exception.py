from contextlib import contextmanager


class Supressor:
    def __init__(self, error):
        self.error = error

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        return exc_type is not None and issubclass(exc_type, self.error)


@contextmanager
def my_context_manager(error):
    try:
        yield
    except error:
        return
