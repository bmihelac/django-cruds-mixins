from cruds import utils as cruds_utils


class PermissionClass(object):

    def can_list(self, user, model, view=None):
        raise NotImplementedError

    def can_create(self, user, model, view=None):
        raise NotImplementedError

    def can_update(self, user, model, instance, view=None):
        raise NotImplementedError

    def can_detail(self, user, model, instance, view=None):
        raise NotImplementedError

    def can_delete(self, user, model, instance, view=None):
        raise NotImplementedError


class AllowAny(PermissionClass):
    """Allows all actions to anyone.
    """

    def can_list(self, user, model, view=None):
        return True

    def can_create(self, user, model, view=None):
        return True

    def can_update(self, user, model, instance, view=None):
        return True

    def can_detail(self, user, model, instance, view=None):
        return True

    def can_delete(self, user, model, instance, view=None):
        return True


class AllowNoone(PermissionClass):
    """Allows all actions to anyone.
    """

    def can_list(self, user, model, view=None):
        return False

    def can_create(self, user, model, view=None):
        return False

    def can_update(self, user, model, instance, view=None):
        return False

    def can_detail(self, user, model, instance, view=None):
        return False

    def can_delete(self, user, model, instance, view=None):
        return False


class IsStaffOrReadOnly(PermissionClass):
    """Anyone has read only access, staff can change.
    """

    def can_list(self, user, model, view=None):
        return True

    def can_create(self, user, model, view=None):
        return user.is_staff

    def can_update(self, user, model, instance, view=None):
        return user.is_staff

    def can_detail(self, user, model, instance, view=None):
        return True

    def can_delete(self, user, model, instance, view=None):
        return user.is_staff


class RulesPermissions(PermissionClass):

    def can_list(self, user, model, view=None):
        return user.has_perm(
            cruds_utils.crud_permission_name(model, cruds_utils.ACTION_LIST),
        )

    def can_create(self, user, model, view=None):
        return user.has_perm(
            cruds_utils.crud_permission_name(model, cruds_utils.ACTION_CREATE),
        )

    def can_update(self, user, model, instance, view=None):
        return user.has_perm(
            cruds_utils.crud_permission_name(
                model,
                cruds_utils.ACTION_CREATE,
                instance
            ),
            instance,
        )

    def can_detail(self, user, model, instance, view=None):
        return user.has_perm(
            cruds_utils.crud_permission_name(
                model,
                cruds_utils.ACTION_DETAIL,
                instance
            ),
            instance,
        )

    def can_delete(self, user, model, instance, view=None):
        return user.has_perm(
            cruds_utils.crud_permission_name(
                model,
                cruds_utils.ACTION_DELETE,
                instance
            ),
            instance,
        )
