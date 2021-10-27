app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db= SQLAlchemy(app)



def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return '<h1>Hello, token is missing </h1>', 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return '<h1>Hello, Could not verify the token</h1>', 403

        return f(*args, **kwargs)

    return decorated


@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({'user': auth.username, 'exp': datetime.utcnow() + timedelta(minutes=30)},
                           app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


@app.route('/')
def index():
    if request.authorization and request.authorization.username == 'username' and request.authorization.password == 'password':
        return '<h1>You are logged in</h1>'

    return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})


@app.route('/protected')
@auth_required
def protected():
    return '<h1>You are on the token page!</h1>'


@app.route('/otherpage')
@auth_required
def other_page():
    return '<h1>You are on the other page!</h1>'


if __name__ == '__main__':
    app.run(debug=True)