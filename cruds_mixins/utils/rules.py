import rules

from cruds import utils as cruds_utils


ACTIONS = {
    'list_predicate': cruds_utils.ACTION_LIST,
    'create_predicate': cruds_utils.ACTION_CREATE,
    'update_predicate': cruds_utils.ACTION_UPDATE,
    'detail_predicate': cruds_utils.ACTION_DETAIL,
    'delete_predicate': cruds_utils.ACTION_DELETE,
}


def add_crud_perms(model, **kwargs):
    """Adds perms to crud actions.
    """
    for name, predicate in kwargs.items():
        action = ACTIONS.get(name, name)
        perm_name = cruds_utils.crud_permission_name(model, action)
        rules.add_perm(perm_name, predicate)
