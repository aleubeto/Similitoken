class LexicUnit:
    """
    The :class:`LexicUnit` encapsulates a single lexer token and its location
    in the source code.

    range: (tuple) token location
    kind: (string) token kind
    value: (string) token value; None or a kind-specific class
    """

    def __init__(self, range, kind, value=None):
        self.range, self.kind, self.value = range, kind, value
