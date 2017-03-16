import json

from entity.enum.user_attribute import *


class UserProfile(object):
    def __init__(self, profiling):
        """
        :type profiling: entity.user_profile.UserAttributes
        """
        self.__profiling = profiling

    @property
    def profiling(self):
        return self.__profiling

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :rtype: entity.user_profile.UserProfile
        """
        return UserProfile(UserAttributes.from_json(json_object["profiling"]))

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.user_profile.UserProfile
        """
        return UserProfile.from_json(json.loads(json_string))


class UserAttributes(object):
    def __init__(self, gender=None, age_group=None, relationship=None, education_level=None, income=None,
                 occupation=None):
        """
        :type gender: str | None
        :type age_group: str | None
        :type relationship: str | None
        :type education_level: str | None
        :type income: str | None
        :type occupation: str | None
        """
        self.__gender = gender
        self.__age_group = age_group
        self.__relationship = relationship
        self.__education_level = education_level
        self.__income = income
        self.__occupation = occupation

    @property
    def gender(self):
        return self.__gender

    @property
    def age_group(self):
        return self.__age_group

    @property
    def relationship(self):
        return self.__relationship

    @property
    def education_level(self):
        return self.__education_level

    @property
    def income(self):
        return self.__income

    @property
    def occupation(self):
        return self.__occupation

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :rtype: entity.user_profile.UserAttributes
        """
        return UserAttributes(json_object.get(GENDER),
                              json_object.get(AGE_GROUP),
                              json_object.get(RELATIONSHIP),
                              json_object.get(EDUCATION_LEVEL),
                              json_object.get(INCOME),
                              json_object.get(OCCUPATION))

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.user_profile.UserAttributes
        """
        return UserAttributes.from_json(json.loads(json_string))
