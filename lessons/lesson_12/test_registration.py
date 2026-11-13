# import unittest
# from unittest import * # import all from this lib
from unittest import TestCase, main

from helpers.helpers import assert_logged
from lessons.lesson_12.api_register_service import register, REGISTERED_USERS, APIRegisterDuplicateException
from lessons.lesson_13.custom_logger import custom_logger


class TestRegistration(TestCase): # test suite
    """
    Test suite for registration feature
    """
    def test_registration_is_successful(self):
        """
        Test verifies user is registered with valid data successfully
        """
        test_username = "Christiano"
        test_password = "hjbshfESFbhj23"
        test_email = "christiano@gmail.com"
        test_phone_number = "1234567890"
        expected_status_code = 200
        expected_user = {"username": test_username, "email": test_email, "phone_number": test_phone_number}

        response_dict = register(username=test_username, password=test_password, email=test_email, phone_number=test_phone_number)

        if response_dict.get("status_cod") != expected_status_code:
            msg = f"Expected status code {expected_status_code}, got {response_dict.get('status_cod')}"
            custom_logger.error(msg)
            raise AssertionError(msg)

        if response_dict.get("user") != expected_user:
            msg = f"Expected user {expected_user}, got {response_dict.get('user')}"
            custom_logger.error(msg)
            raise AssertionError(msg)

        if expected_user not in REGISTERED_USERS:
            msg = f"Expected DB user {expected_user}, got {response_dict.get('user')}"
            custom_logger.error(msg)
            raise AssertionError(msg)


    def test_registration_invalid_email_without_at_sign(self):
        """
        Test verifies user is NOT registered with invalid email address
        """
        test_username = "Christiano"
        test_password = "hjbshfESFbhj23"
        test_email = "christianogmail.com"
        test_phone_number = "1234567890"
        expected_status_code = 400

        response_dict = register(username=test_username, password=test_password, email=test_email, phone_number=test_phone_number)

        assert_logged(condition=response_dict.get("status_code") == expected_status_code, msg=f"Expected status_code {expected_status_code}, got {response_dict.get('status_code')}")
        assert_logged(condition="user" not in response_dict.keys(), msg=f"Expected not to be present user field in response\n{response_dict}")
        assert_logged(condition="error_msg" in response_dict.keys(), msg=f"Expected to be present error message in response\n{response_dict}")
        assert_logged(condition={"username": test_username, "email": test_email, "phone_number": test_phone_number} not in REGISTERED_USERS)


    def test_register_duplicate_user_exception_is_raised(self):
        """
        Test verifies exception is raised while attemping to register a duplicate user
        """
        test_username = "Christiano1"
        test_password = "hjbshfESFbhj231"
        test_email = "christian@gmail.com"
        test_phone_number = "12345678901"
        expected_status_code = 200
        expected_user = {"username": test_username, "email": test_email, "phone_number": test_phone_number}

        response_dict = register(username=test_username, password=test_password, email=test_email, phone_number=test_phone_number)

        assert response_dict.get("status_code") == expected_status_code, f"Expected status_code {expected_status_code}, got {response_dict.get('status_code')}"
        assert response_dict.get("user") == expected_user, f"Expected user {expected_user}, got {response_dict.get('user')}"
        assert expected_user in REGISTERED_USERS, f"Expected DB user {expected_user}, got {response_dict.get('user')}"

        with self.assertRaises(APIRegisterDuplicateException): # якщо це виключення не впаде - то тест завалиться
            register(username=test_username, password=test_password, email=test_email, phone_number=test_phone_number)

        with self.assertLogs(custom_logger, level="INFO"):
            register(username=test_username, password=, email=test_email, phone_number=test_phone_number)


if __name__ == "__main__":
    main(verbosity=2)