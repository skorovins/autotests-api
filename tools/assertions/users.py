import allure

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from clients.users.users_schema import UserSchema
from tools.assertions.base import assert_equal


@allure.step("Check create user response")
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


@allure.step("Check user")
def assert_user(actual_user: UserSchema, expected_user: UserSchema):
    """
    Проверяет корректность данных пользователя.
    :param actual_user: Фактические данные пользователя.
    :param expected_user: Ожидаемые данные пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual_user.id, expected_user.id, "id")
    assert_equal(actual_user.email, expected_user.email, "email")
    assert_equal(actual_user.last_name, expected_user.last_name, "last_name")
    assert_equal(actual_user.first_name, expected_user.first_name, "first_name")
    assert_equal(actual_user.middle_name, expected_user.middle_name, "middle_name")


@allure.step("Check get user response")
def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на получение пользователя соответствует ответу на его создание.

    :param get_user_response: Ответ API при запросе данных пользователя.
    :param create_user_response: Ответ API при создании пользователя.
    :raises AssertionError: Если данные пользователя не совпадают.
    """
    assert_user(get_user_response.user, create_user_response.user)