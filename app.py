from flask import Flask ,request , render_template ,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#We are basically telling python that we are building a new web application object by using the Flask blueprint
#__name__ basically is an in-built tool that tells Python that the web application/class is being used right here in this file 
app=Flask(__name__)

#telling app that we are using sqlite for our database 
#The ADDRESS to store the database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///capsule_v2.db'
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
    unlock_date=db.Column(db.DateTime,nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.now)

    


    def __repr__(self):
        return f'<Capsule {self.id}>'



@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        title_input = request.form['title']
        message_input = request.form['message']
        date_input= request.form['unlock_date']

        unlock_date_obj = datetime.strptime(date_input, '%Y-%m-%d')

        new_capsule = Capsule(
            title=title_input,
            message=message_input,
            unlock_date=unlock_date_obj
        )
        # 4. Save to Database
        db.session.add(new_capsule) # Stage the change
        db.session.commit()         # Save permanently

        #Refresh the page to clear the form 
        return redirect('/')

    
    # 1. Get all capsules sorted by newest first
    capsules = Capsule.query.order_by(Capsule.created_at.desc()).all()
    
    # 2. Get current time for the "Lock/Unlock" logic
    
    return render_template('index.html', capsules=capsules, now=datetime.now())


@app.route('/delete/<int:id>')
def delete(id):
    capsule= Capsule.query.get(id)
    db.session.delete(capsule)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)