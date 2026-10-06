from hawkBackend.domain.validations import ValidationProtocol


class FieldValidator:
    def __init__(self, rules: list[ValidationProtocol]) -> None:
        self.rules = rules

    def validate(self, value: str, short_circuit: bool = True) -> list[str]:
        errors: list[str] = []
        for rule in self.rules:
            error = rule.validate(value)
            if error:
                errors.append(error)
                if short_circuit:
                    break
        return errors
