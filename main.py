from flask import Flask, render_template, request
from flask_mail import Mail, Message

app=Flask(__name__)
app.secret_key="123"

@app.route("/",methods=["GET","POST"])
def mail():
    if request.method == "POST":
        fmail=request.form.get('email')
        password=request.form.get('password')
        temail = request.form.get('temail')
        message = request.form.get('message')
        body = request.form.get('body')
        destination=request.form.get('destination')
        date=request.form.get('date')
        ticket_id = request.form.get('ticket_id')
        name = request.form.get('name')

        
        app.config['MAIL_SERVER']='smtp.gmail.com'
        app.config['MAIL_PORT']=465
        app.config['MAIL_USERNAME']=fmail
        app.config['MAIL_PASSWORD']=password
        app.config['MAIL_USE_TLS']=False
        app.config['MAIL_USE_SSL'] =True
        mail = Mail(app)

        msg=Message('Ticket details',sender=fmail,recipients=[temail])
        msg.html=render_template('sendticket.html',ticket_id=ticket_id,fmail=fmail,name=name,date=date)
        mail.send(msg)

        return ("mail sent")





    return render_template("mail.html")

if __name__=="__main__":
    app.run(debug=True)