from .bbridge_entity import BBridgeEntity
from ..enum import *


class UserProfile(BBridgeEntity):
    def __init__(self, profiling):
        """
        :type profiling: bbridge_sdk.entity.response.user_profile.UserAttributes
        """
        self.__profiling = profiling

    @classmethod
    def from_json(cls, json_object):
        return UserProfile(UserAttributes.from_json(json_object["profiling"]))

    @property
    def profiling(self):
        return self.__profiling


class UserAttributes(BBridgeEntity):
    def __init__(self, gender=None, age_group=None, relationship=None, education_level=None, income=None,
                 occupation=None, ei=None, si=None, tf=None, jp=None):
        """
        :type gender: bbridge_sdk.entity.response.user_profile.UserAttributeEstimation | None
        :type age_group: bbridge_sdk.entity.response.user_profile.UserAttributeEstimation | None
        :type relationship: bbridge_sdk.entity.response.user_profile.UserAttributeEstimation | None
        :type education_level: bbridge_sdk.entity.response.user_profile.UserAttributeEstimation | None
        :type income: bbridge_sdk.entity.response.user_profile.UserAttributeEstimation | None
        :type occupation: bbridge_sdk.entity.response.user_profile.UserAttributeEstimation | None
        :type ei: bbridge_sdk.entity.response.user_profile.UserAttributeEstimation | None
        :type si: bbridge_sdk.entity.response.user_profile.UserAttributeEstimation | None
        :type tf: bbridge_sdk.entity.response.user_profile.UserAttributeEstimation | None
        :type jp: bbridge_sdk.entity.response.user_profile.UserAttributeEstimation | None
        """
        self.__gender = gender
        self.__age_group = age_group
        self.__relationship = relationship
        self.__education_level = education_level
        self.__income = income
        self.__occupation = occupation
        self.__ei = ei
        self.__si = si
        self.__tf = tf
        self.__jp = jp

    @classmethod
    def from_json(cls, json_object):
        return UserAttributes(UserAttributeEstimation.from_json(json_object.get(GENDER)),
                              UserAttributeEstimation.from_json(json_object.get(AGE_GROUP)),
                              UserAttributeEstimation.from_json(json_object.get(RELATIONSHIP)),
                              UserAttributeEstimation.from_json(json_object.get(EDUCATION_LEVEL)),
                              UserAttributeEstimation.from_json(json_object.get(INCOME)),
                              UserAttributeEstimation.from_json(json_object.get(OCCUPATION)),
                              UserAttributeEstimation.from_json(json_object.get(EI)),
                              UserAttributeEstimation.from_json(json_object.get(SI)),
                              UserAttributeEstimation.from_json(json_object.get(TF)),
                              UserAttributeEstimation.from_json(json_object.get(JP)))

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

    @property
    def ei(self):
        return self.__ei

    @property
    def si(self):
        return self.__si

    @property
    def tf(self):
        return self.__tf

    @property
    def jp(self):
        return self.__jp


class UserAttributeEstimation(BBridgeEntity):
    def __init__(self, label, confidence):
        """
        :type label: str
        :type confidence: double
        """
        self.__label = label
        self.__confidence = confidence

    @classmethod
    def from_json(cls, json_object):

        if json_object is None:
            return None

        return UserAttributeEstimation(json_object["label"], json_object["confidence"])

    @property
    def label(self):
        return self.__label

    @property
    def confidence(self):
        return self.__confidence
