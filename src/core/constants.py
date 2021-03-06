class MessageType:
    BEGIN_SESSION = 0
    YES = 1
    NO = 2
    CONTINUE_SESSION = 3
    ATTACK_SUBMARINE = 4
    ERROR = 5
    DISCONNECT = 6
    READY = 7
    SUBMARINE_SANK = 8
    KEEP_ALIVE = 9


MESSAGE_FIELDS_COUNTS = {
    MessageType.BEGIN_SESSION: 2,
    MessageType.YES: 0,
    MessageType.NO: 0,
    MessageType.CONTINUE_SESSION: 2,
    MessageType.ATTACK_SUBMARINE: 2,
    MessageType.ERROR: 1,
    MessageType.DISCONNECT: 0,
    MessageType.READY: 0,
    MessageType.SUBMARINE_SANK: 3,
    MessageType.KEEP_ALIVE: 0,
}

SEA = 0
SUB = 1
HIT = 2
FIELD_SIZE = 2
MAX_CONNECT_REQUEST = 5
