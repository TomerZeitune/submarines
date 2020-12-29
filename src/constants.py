class MessageType:
    BEGIN_SESSION = 0
    YES = 1
    NO = 2
    CONTINUE_SESSION = 3
    ATTACK_SUBMARINE = 4
    ERROR = 5
    DISCONNECT = 6
    READY = 7
    SUBMARINE_SINK = 8
    KEEP_ALIVE = 9


MESSAGE_FIELDS_COUNTS = {
    MessageType.BEGIN_SESSION: 3,
    MessageType.YES: 0,
    MessageType.NO: 0,
    MessageType.CONTINUE_SESSION: 2,
    MessageType.ATTACK_SUBMARINE: 2,
    MessageType.ERROR: 1,
    MessageType.DISCONNECT: 0,
    MessageType.READY: 0,
    MessageType.SUBMARINE_SINK: 3,
    MessageType.KEEP_ALIVE: 0,
}
