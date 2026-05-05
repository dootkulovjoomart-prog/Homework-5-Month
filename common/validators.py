from rest_framework.exceptions import ValidationError
from datetime import date   

def validate_age_from_token(request):
    user=request.user

    if not user.is_authenticated:
        raise ValidationError('Unauthanticade')
    if not user.birthdate:
        raise ValidationError('send birthdate')
    today = date.today()
    age = today.year - user.birthdate.year - (
        (today.month, today.day) < (user.birthdate.month, user.birthdate.day)
    )

    if age < 18:
        raise ValidationError('not 18 year')
    
    return True