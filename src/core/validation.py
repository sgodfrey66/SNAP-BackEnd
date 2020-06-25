import rules
from core.exceptions import ApplicationValidationError


def validate_fields_with_rules(user, data, error_message='Not found', **kwargs):
    for field, rule_name in kwargs.items():
        assert rules.rule_exists(rule_name)
        if field in data and not rules.test_rule(rule_name, user, data[field]):
            raise ApplicationValidationError(field, [error_message])
