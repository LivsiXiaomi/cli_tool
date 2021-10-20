from enum import Enum


class Commands(Enum):
    CREATE = "CREATE"
    DELETE = "DELETE"
    MOVE = "MOVE"
    LIST = "LIST"


ERROR_MESSAGE_TEMPLATE = "Could not {} directory: wrong number of args."
