class MandatoryFieldCannotBeEmptyException(Exception):
    def __init__(self):
        super().__init__()


class InvalidProjectIDException(Exception):
    def __init__(self):
        super().__init__()


class KeyInRulesNotPresentInRequest(Exception):
    def __init__(self, message):
        super().__init__(message)


class RulesListEmptyException(Exception):
    def __init__(self):
        super().__init__()


class InvalidFeatureTableNameException(Exception):
    def __init__(self):
        super().__init__()
