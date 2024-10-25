from flask import Flask,render_template,redirect,url_for,flash
from flask_mail import Mail,Message


app=Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']='your_email@gmail.com'
app.config['MAIL_PASSWORD']='your_password'
app.config['MAIL_DEFAULT_SENDER']='your_email@gmail.com'



mail=Mail(app)


 
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_email')


def send_email():
    try:
        # Creating the message object
        msg=Message("Test Email", recipients=["recipient_email@gmail.com"])
        msg.body="This is the body of the email."
        msg.html="<b>This is the body of the email in HTML format.</b>"

         # Send the email
        mail.send(msg)

        flash('Email sent successfully!', 'success')
     except Exception as e:
         flash(f"An error occurred: {e}",'danger')

    return redirect(url_for('index'))
                                                                                                                                                                                            
if __name__ == '__main__': 
    app.secret_key='your_secret_key' # Required for flashing messages
    app.run(debug=True)           