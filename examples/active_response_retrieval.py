import time


def active_response_retrieval(client, request_id):
    number_of_attempts = 0

    while True:
        number_of_attempts = number_of_attempts + 1
        time.sleep(1)
        response = client.response(request_id)
        print("After " + str(number_of_attempts) + " second(s): " + str(response.body))

        if response.body is not None:
            break
