from ast import Delete
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from db import db
from resources.store import Store, StoreList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 
app.secret_key = 'hello' 
api = Api(app)

@app.before_first_request #creates tables in the database for us without having a separate create_tables.py file
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>') #get, post
api.add_resource(ItemList, '/items') #get, post
api.add_resource(UserRegister, '/register') 


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True) #better way to troubleshoot problems
