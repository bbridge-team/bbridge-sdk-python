import sys

import time
from pymongo import MongoClient

from bbridge_sdk import BBridgeClient
from bbridge_sdk.entity.enum import EN, GENDER, AGE_GROUP, RELATIONSHIP, EDUCATION_LEVEL, INCOME, OCCUPATION, EI, TF, \
    SI, JP
from bbridge_sdk.entity.enum.data_source import TWITTER
from bbridge_sdk.entity.request import User
from bbridge_sdk.entity.request.user_id import UserID
from bbridge_sdk.entity.response import UserProfile

from bbridge_sdk.entity.response.data_id_result import DataIdResult

apiUserName, apiUserPassword, databaseURL, databaseName, usersTableName, outputDdatabaseName,\
resultsTableName, requestedCollectionName, crawledCollectionName, profiledCollectionName = sys.argv

usersCollection = MongoClient(databaseURL)[databaseName][usersTableName]
crawlingAttemptedUsersCollection = MongoClient(databaseURL)[outputDdatabaseName][requestedCollectionName]
crawledUsersCollection = MongoClient(databaseURL)[outputDdatabaseName][crawledCollectionName]
profiledUsersCollection = MongoClient(databaseURL)[outputDdatabaseName][profiledCollectionName]
outputCollection = MongoClient(databaseURL)[outputDdatabaseName][resultsTableName]

profilingExceptions = dict()
maxNumProfilingAttempts = 5

downloadExceptions = dict()
maxNumDataDownloadAttempts = 5

client = BBridgeClient.Builder(apiUserName, apiUserPassword).build()

continueFlag = True

while(continueFlag):
    continueFlag = False

    for user in usersCollection.find():

        user_id_str = str(user['_id'])

        requested = crawlingAttemptedUsersCollection.find_one({'_id':user_id_str})

        if requested is None:
            continueFlag = True

            userId = UserID(TWITTER, user['_id'])
            request_id = client.crawler_retrieval(userId, 100, "TEST").body.request_id

            request = {
                "_id": user_id_str,
                "request_id": request_id}

            crawlingAttemptedUsersCollection.insert(request)
        else:
            crawled = crawledUsersCollection.find_one({'_id':user_id_str})

            if crawled is None:
                continueFlag = True

                request_id = requested['request_id']
                try:
                    data_id = client.response(request_id, DataIdResult)

                    request_id = client.crawler_download(DataIdResult(data_id.body.value)).body.request_id
                    time.sleep(1)
                    result = client.response(request_id)

                    try:
                        texts = []
                        image_urls = []

                        for post in result.body['osn_user_data']['posts']:
                            if post['text'] is not None:
                                texts.append(post['text'])

                            if post['imageUrl'] is not None:
                                image_urls.append(post['imageUrl'])

                        crawled_data = {
                            "_id": user_id_str,
                            "texts":texts,
                            "image_urls":image_urls}

                        crawledUsersCollection.insert(crawled_data)

                        print("Crawled user id: " + user_id_str)

                    except:
                        print("Post extraction exception, user id: " + user_id_str)
                except:
                    if user_id_str in downloadExceptions:
                            downloadExceptions[user_id_str] = downloadExceptions[user_id_str] + 1

                            if downloadExceptions[user_id_str] > maxNumDataDownloadAttempts:
                                print("Rescheduling crawling of user id: " + user_id_str)
                                crawlingAttemptedUsersCollection.remove(user_id_str)
                                del downloadExceptions[user_id_str]
                            else:
                                print(str(downloadExceptions[user_id_str]) + " download exception, user id: " + user_id_str)
                    else:
                        downloadExceptions[user_id_str] = 0
            else:
                profiled = profiledUsersCollection.find_one({'_id':user_id_str})

                if profiled is None:
                    continueFlag = True

                    user = User(crawled["texts"], crawled["image_urls"])
                    request_id = client.individual_user_profiling(user, EN, [GENDER, AGE_GROUP, RELATIONSHIP,
                                                                         EDUCATION_LEVEL, INCOME, OCCUPATION,
                                                                         EI, SI, TF, JP]).body.request_id
                    request = {
                        "_id": user_id_str,
                        "request_id":request_id}

                    profiledUsersCollection.insert(request)
                else:
                    try:
                        request_id = profiled['request_id']
                        profile = client.response(request_id, UserProfile)

                        user_profile = {
                            "_id": user_id_str,
                            "gender":{"label": profile.body.profiling.gender.label, "confidence": profile.body.profiling.gender.confidence},
                            "age_group":{"label": profile.body.profiling.age_group.label, "confidence": profile.body.profiling.age_group.confidence},
                            "relationship":{"label": profile.body.profiling.relationship.label, "confidence": profile.body.profiling.relationship.confidence},
                            "education_level":{"label": profile.body.profiling.education_level.label, "confidence": profile.body.profiling.education_level.confidence},
                            "income":{"label": profile.body.profiling.income.label, "confidence": profile.body.profiling.income.confidence},
                            "occupation":{"label": profile.body.profiling.occupation.label, "confidence": profile.body.profiling.occupation.confidence},
                            "MBTI_ei":{"label": profile.body.profiling.ei.label, "confidence": profile.body.profiling.ei.confidence},
                            "MBTI_si":{"label": profile.body.profiling.si.label, "confidence": profile.body.profiling.si.confidence},
                            "MBTI_tf":{"label": profile.body.profiling.tf.label, "confidence": profile.body.profiling.tf.confidence},
                            "MBTI_jp":{"label": profile.body.profiling.jp.label, "confidence": profile.body.profiling.jp.confidence},
                        }

                        outputCollection.insert(user_profile)

                        print("Profiled user id: " + user_id_str)
                    except:
                        if user_id_str in profilingExceptions:
                            profilingExceptions[user_id_str] = profilingExceptions[user_id_str] + 1

                            if profilingExceptions[user_id_str] > maxNumProfilingAttempts:
                                print("Rescheduling profiling of user id: " + user_id_str)
                                profiledUsersCollection.remove(user_id_str)
                                del profilingExceptions[user_id_str]
                            else:
                                print(str(profilingExceptions[user_id_str]) + " profiling exception, user id: " + user_id_str)
                        else:
                            profilingExceptions[user_id_str] = 0

