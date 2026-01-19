from flask import Flask ,request , render_template ,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#We are basically telling python that we are building a new web application object by using the Flask blueprint
#__name__ basically is an in-built tool that tells Python that the web application/class is being used right here in this file 
app=Flask(__name__)

#telling app that we are using sqlite for our database 
#The ADDRESS to store the database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///capsule.db'
#turning auto tracking off which allows us to access every change in the memory of the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialising the database
#The DELIVERY of the database
db=SQLAlchemy(app)

class Capsule(db.Model):
    # Primary Key: The unique ID for every message (1, 2, 3...)
    id= db.Column(db.Integer, primary_key=True)

    #The data columns 
    title= db.Column(db.String(100),nullable=False)
    message= db.Column(db.Text , nullable=False)

    #The logic columns 
    unlock_data=db.Column(db.DateTime,nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.now)


    def __repr__(self):
        return f'<Capsule {self.id}>'



@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        title_input = request.form['title']
        message_input = request.form['message']
        date_input= request.form['unlock_date']

        unlock_date_obj = 

if __name__ == '__main__':
    app.run(debug=True)