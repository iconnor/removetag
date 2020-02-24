from flask import Flask, request, jsonify, send_from_directory
from flask_restful import Resource, Api, reqparse
import requests

app = Flask(__name__, static_url_path='')
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('password', type=str, help='Docker hub password')
parser.add_argument('username', type=str, help='Docker hub username')
parser.add_argument('organization', type=str, help='Docker hub organization')
parser.add_argument('image', type=str, help='Docker hub image')
parser.add_argument('tag', type=str, help='Docker hub tag')


class Tags(Resource):
    def post(self):
        args = parser.parse_args()
        API_ENDPOINT = "https://hub.docker.com/v2"
        username = args['username']
        password = args['password']
        organization = args['organization']
        image = args['image']
        data = { "username": username, "password": password }
        r = requests.post(url = API_ENDPOINT + "/users/login/", data = data) 
        token = r.json()['token']
        print(f'Got a token back: {token}')
        data = request.get_json()
        print(f'Got a data: {data}')
        tag = data['pullrequest']['source']
        delete_url = f'{API_ENDPOINT}/repositories/{organization}/{image}/tags/{tag}/'
        print(f'Removing using {delete_url}')
        r2 = requests.delete(url = delete_url,
            headers = {"Authorization": f'JWT {token}'})
        return ({"code": r2.status_code})

api.add_resource(Tags, '/tags') # Route_1

@app.route('/')
def send_home():
    return send_from_directory('html','index.html')

if __name__ == '__main__':
     app.run(host='0.0.0.0')