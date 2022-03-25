from django.core.exceptions import ValidationError


def validator_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Name must contain only letters')


def validator_max_size(value):
    max_size = 10
    limit = max_size * 1024 * 1024
    if value.size > limit:
        raise ValidationError(f'File too large. Size should not exceed {max_size} MB.')