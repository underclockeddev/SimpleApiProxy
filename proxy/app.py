import requests, time, os
from flask_cors import CORS
from flask import Flask, request, Response
from flask_restful import Api, Resource

attempts = 0

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})


class SimpleApiProxy(Resource):

    def __init__(self):
        resp = requests.request(method='GET', url='http://management/config', data=request.get_data())
        configVals = resp.content.decode().split('\n')
        self.secondsBeforeRequest = int(configVals[0], 0)
        self.destinationUrl = configVals[1]
        self.failedAttemptsBeforeSuccess = int(configVals[2], 0)
        app.logger.info(configVals[0])
        app.logger.info(configVals[1])
        app.logger.info(configVals[2])
    def get(self):
        global attempts
        attempts += 1

        app.logger.info("attempt: " + str(attempts) + ", waiting " + str(self.secondsBeforeRequest) + " seconds")
        time.sleep(self.secondsBeforeRequest)

        if (attempts < self.failedAttemptsBeforeSuccess):
            app.logger.info("failed attempt #" + str(attempts) + " of " + str(self.failedAttemptsBeforeSuccess))
            return "Bad request", 400

        app.logger.info("routing GET to " + self.destinationUrl)
        resp = requests.request(
        method=request.method,
        url=self.destinationUrl,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items()
                if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        app.logger.info(response)

        attempts = 0 # reset
        return response

    def post(self):
        global attempts
        attempts += 1

        app.logger.info("attempt: " + str(attempts) + ", waiting " + str(self.secondsBeforeRequest) + " seconds")
        time.sleep(self.secondsBeforeRequest)

        if (attempts < self.failedAttemptsBeforeSuccess):
            app.logger.info("failed attempt #" + str(attempts) + " of " + str(self.failedAttemptsBeforeSuccess))
            return "Bad request", 400

        app.logger.info("routing POST to " + self.destinationUrl)
        resp = requests.request(
        method=request.method,
        url=self.destinationUrl,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items()
                if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        app.logger.info(response)
        return response

api.add_resource(SimpleApiProxy, "/orbitalmock")
app.run(host='0.0.0.0', port=5000)