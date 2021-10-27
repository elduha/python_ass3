## 
Login to WEB server

#
Installation
Flask
Flask_sqlalchemy
JWT


#Usage
Install the libraries
Connect to DataBase(sqlite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

Get token
return jsonify({'token': token.decode('UTF-8')})


#Examples
After the conneting to web and after login we get the token
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidXNlcm5hbWUiLCJleHAiOjE2MzUzMzAzNTB9.BvkL1ASqZ38qVq5w8e2c1oqRGjUkgoyL7iNOwR1jEdU"


