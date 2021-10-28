from flask import Flask, request
from requests.exceptions import Timeout
from flask_restful import Api, abort
import requests
import socket

app = Flask(__name__)
api = Api(app)

@app.route('/status')
def get_status():
    try:
        website = request.args.get('url')

        res = requests.get("https://www." + website, timeout=10) #switch from 10 to 0.000001 to test timeout

        ip = socket.gethostbyname(website)
        respose_time = res.elapsed.total_seconds()
        status_code = res.status_code
        
        ret = {"status_code" : status_code, "ip" : ip, "resposnse_time" : respose_time}

        allow = res.headers.get('allow')
        if allow:
            ret.update({"Allow" : allow})

        connection = res.headers.get('connection')
        if connection:
            ret.update({"Connection" : connection})

        date = res.headers.get('date')
        if date:
            ret.update({"Date" : date})

        expires = res.headers.get('expires')
        if expires:
            ret.update({"Expires" : expires})

        origin = res.headers.get('origin')
        if origin:
            ret.update({"Origin" : origin})

        server = res.headers.get('server')
        if server:
            ret.update({"Server" : server})
        
        return ret
    except Timeout:
        ######################## To fix: custom message not working
        abort(408, description="Request timeout! Could not establish connection within 10 seconds.")
    except:
        return {"message": "Connection error!"}


@app.route('/')
@app.route('/me')
def get_me():
    ip = request.remote_addr
    ret = {"IP" : ip}

    host = request.headers['Host']
    if host:
        ret.update({"Host" : host})

    agent = request.headers['User-Agent']
    if agent:
        ret.update({"Host" : agent})

    return ret

app.run(debug=False)