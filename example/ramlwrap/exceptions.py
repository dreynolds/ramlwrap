

class FatalException(Exception):
    """
    Custom CBP Exception, allows custom status_code definition.
    """

    status_code = None  # Will default to 400 in constructor
    message = ""  # Error message is set in constructor
    errors = None
    public_message = "Something went wrong processing your request (see server logs)."

    def __init__(self, message, status_code=400, errors=None, public_message=None):
        if status_code:
            self.status_code = status_code
        else:
            self.status_code = FatalException.default_code

        if public_message:
            self.public_message = public_message

        self.errors = errors
        self.message = message

    def __str__(self):
        return repr(self.message)