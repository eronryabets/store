from django.http import HttpResponseForbidden


def user_profile_access_required(view_func):
    def wrapper(request, *args, **kwargs):
        # Получить идентификатор пользователя, который отправил запрос на редактирование профиля
        user_id = kwargs.get("pk")

        # Проверить, авторизован ли текущий пользователь, и имеет ли он право редактировать этот профиль
        if not request.user.is_authenticated or request.user.id != user_id:
            return HttpResponseForbidden("You do not have permission to edit this profile")

        return view_func(request, *args, **kwargs)

    return wrapper
