from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

# from properties.models import Company


def patient_required(function=None, redirect_field=REDIRECT_FIELD_NAME, home_url='record:home'):
    '''
    Decorator for views that check that the logged in user
    is a patient or redirects to login page.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and hasattr(u, 'patient'),
        login_url=home_url,
        redirect_field_name=redirect_field
    )

    if function:
        return actual_decorator(function)
    return actual_decorator

def staff_required(function=None, redirect_field=REDIRECT_FIELD_NAME, home_url='record:home'):
    '''
    Decorator for views that check that the logged in user
    is a staff or redirects to login page.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and hasattr(u, 'hospitalstaff'),
        login_url=home_url,
        redirect_field_name=redirect_field
    )

    if function:
        return actual_decorator(function)
    return actual_decorator