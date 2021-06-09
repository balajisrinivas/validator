import exc


class Validator:
    def __init__(self, request, rules):
        self.request = request
        self.rules = rules

    def validate(self):

        result = True

        # Check whether the key present in rules is also present in request
        # If key not present raise an exception
        for key in self.rules.keys():
            if key not in self.request:
                raise exc.KeyInRulesNotPresentInRequest(f"Key present in rules {key} is not in request")

        # Directing to Rules Validation
        for key in self.rules.keys():
            if key in self.request:
                validate_input = self.request[key]
                rule_input = self.rules[key]

                # If there are multiple rules (more than one rule) to be validated
                if len(rule_input) > 1:
                    for each_rule in rule_input:
                        rule_obj = each_rule()
                        result = rule_obj.apply(validate_input)
                        if result is True:
                            pass

                # If there is only one rule to be validated
                elif len(rule_input) == 1:
                    rule_obj = rule_input[0]()
                    result = rule_obj.apply(validate_input)

                # If there are no rules provided in the list
                elif len(rule_input) == 0:
                    raise exc.RulesListEmptyException

        return result
