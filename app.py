from flask_restful import Api, Resource
import firebase_admin
from flask import Flask, request, jsonify, redirect, render_template
from firebase_admin import credentials, firestore, initialize_app
from firebase import firebase

app = Flask(__name__)
api = Api(app)
firebase = firebase.FirebaseApplication("https://login-auth-42458-default-rtdb.firebaseio.com/", None)

#Ignore the config dict its useless
config = {
    "apiKey": "AIzaSyCOyYtjVoddu_v0wuE90AlUO5ZYvIwe1iI",
    "authDomain": "login-auth-42458.firebaseapp.com",
    "projectId": "login-auth-42458",
    "storageBucket": "login-auth-42458.appspot.com",
    "messagingSenderId": "642686191238",
    "appId": "1:642686191238:web:74ba8c7a94671f0d447307",
    "measurementId": "G-9L1VJ04JS7"}
#------------------------------

# Initialize firestore DB
cred = credentials.Certificate(
    'login-auth-42458-firebase-adminsdk-fl3g5-db0164d6e9.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

#Statement below adds a data to the realtime database
'''
data = {
    'username': 'yashp',
    'password': 'ypathi234'
}
result1 = firebase.post('/login-auth-42458-default-rtdb/Credentials', data)
'''

#Uses firestore
@app.route('/', methods=['GET', 'POST'])
def loginauth():
    if request.method == 'POST':
        usern = request.form['uname']
        passwo = request.form['passw']
        print(usern)
        "\n"
        print(passwo)

        # login_ref = db.collection('Credentials').document('firstEntry')
        login_ref = db.collection('Credentials')
        login_ref.add({
            'username': usern,
            'password': passwo
        })
        return redirect('/')
    else:
        return render_template('login.html')


# RESTful API - uses the realtime database
class Get(Resource):
    def get(self):
        # args = post_put_args.parse_args()
        result = firebase.get('/login-auth-42458-default-rtdb/Credentials', '')
        print(result)


api.add_resource(Get, "/getUserInfo")

if __name__ == '__main__':
    app.run(Debug=True)
