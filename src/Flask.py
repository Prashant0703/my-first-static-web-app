
from flask import Flask, render_template, request

from flaskext.mysql import MySQL

 

app = Flask(__name__)

mysql = MySQL(app)

 

 

@app.route("/")

def main():

    return render_template('user details.html')

 

 

@app.route('/submit', methods=['GET', 'POST'])

def submit():

    if request.method == 'POST':

        user1 = request.form

        User_FullName = user1['Username']

        User_Gender = user1['Gender']

        User_MobileNumber = user1['Mobile number']

        User_UniqueID = user1['Unique ID number']

        User_Location = user1['Location']

        User_Pincode = user1['PinCode']

        # MySQL configurations

        app.config['MYSQL_DATABASE_USER'] = 'fai10119'

        app.config['MYSQL_DATABASE_PASSWORD'] = '643%#$102'

        app.config['MYSQL_DATABASE_DB'] = 'fai10119'

        app.config['MYSQL_DATABASE_HOST'] = '125.99.159.93'

        app.config['MYSQL_DATABASE_PORT'] = 6033

        conn = mysql.connect()

        cur = conn.cursor()

        mysql_insert_query = ("""INSERT INTO round_kart_order_details(Username,

                                 Gender,`Mobile number`,`Unique ID Number`,

                                 `Location`,PinCode)

                                 Values (%s, %s, %s, %s, %s, %s)""")

        record = (User_FullName, User_Gender, int(User_MobileNumber),

                  int(User_UniqueID), User_Location, int(User_Pincode))

        cur.execute(mysql_insert_query, record)

        conn.commit()

        cur.close()

    return render_template('user details.html')

 

 

if __name__ == "__main__":

    app.run()
