from functools import wraps


def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") != "admin":
            return "Unauthorized"
        return fn(*args, **kwargs)

    return wrapper


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"


print(show_secrets(role="author"))
