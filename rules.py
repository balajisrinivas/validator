import exc


class Rule:
    def __init__(self):
        self.error_message = "error"
        self.class_name = type(self).__name__

    def set_error(self, message):
        self.error_message = message

    def get_error(self):
        return self.error_message


class Required(Rule):

    def __init__(self):
        Rule.__init__(self)

    def apply(self, arg):
        if arg is None or (hasattr(arg, "__len__") and len(arg) == 0):
            self.set_error("Field was empty")
            raise exc.MandatoryFieldCannotBeEmptyException
        return True


class ProjectIDExistsRule(Rule):

    def __init__(self):
        Rule.__init__(self)

    def apply(self, arg):
        # This function checks if the projectID is present in the project table
        # This is now just a dummy function and it needs to be developed
        # arg.get_repo
        # find_by_key
        key_present_in_project_table = True
        if key_present_in_project_table is False:
            raise exc.InvalidProjectIDException
        return True


class FeatureTableExistsRule(Rule):

    def __init__(self):
        Rule.__init__(self)

    def apply(self, arg):
        # This function checks if the feature table is present in the metadata
        # This is now just a dummy function and it needs to be developed
        # arg.get_repo
        # find_by_key
        is_feature_table_name_exists = False
        if is_feature_table_name_exists is False:
            raise exc.InvalidFeatureTableNameException
        return True
