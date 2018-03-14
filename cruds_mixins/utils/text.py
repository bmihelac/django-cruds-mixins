from django.utils.translation import ugettext_lazy as _


def create_model_title(model):
    return _('New %(model_name)s') % {
        'model_name': model._meta.verbose_name.capitalize()
    }


def edit_model_title(model):
    return _('Edit %(model_name)s') % {
        'model_name': model._meta.verbose_name.capitalize()
    }
