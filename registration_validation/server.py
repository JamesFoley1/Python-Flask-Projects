from flask import Flask, render_template, request, redirect, session, flash
import re
import datetime
app = Flask(__name__)
app.secret_key = "#41U135#^@!$#i100$%*(9804@#$%055#!#$31Fff1"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def initsession():
    session.clear()
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm'] = request.form['confirm']
    session['street'] = request.form['street']
    session['city'] = request.form['city']
    return redirect('/')




@app.route('/')
def main():
    state_list = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    country_list = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua & Deps','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Rep','Chad','Chile','China','Colombia','Comoros','Congo','Congo {Democratic Rep}','Costa Rica','Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','East Timor','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Fiji','Finland','France','Gabon','Gambia','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland (Republic)','Israel','Italy','Ivory Coast','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea North','Korea South','Kosovo','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Myanmar, (Burma)','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russian Federation','Rwanda','St Kitts & Nevis','St Lucia','Saint Vincent & the Grenadines','Samoa','San Marino','Sao Tome & Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Sudan','Spain','Sri Lanka','Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Tonga','Trinidad & Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States']

    length = len(country_list) - 1

    return render_template('index.html', state_list = state_list, country_list = country_list, length = length)

@app.route('/user', methods=['POST'])
def login():
    if request.form['action'] == 'register':
        allfieldsValid = True
        initsession()
        if 'Reset' in request.form:
            if request.form['Reset'] == 'Reset':
                session.clear()
                return redirect('/')

        if len(request.form['first_name']) < 1:
            flash("- A first name is required!")
            allfieldsValid = False
        elif len(request.form['first_name']) > 200:
            flash("- Your first name is too long! Please enter a nickname.")
            allfieldsValid = False

        if len(request.form['last_name']) < 1:
            flash("- A last name is required!")
            allfieldsValid = False
        elif len(request.form['last_name']) > 201:
            flash("- Your lastst name is too long! Please enter a shorter name or abbreviate if possible.")
            allfieldsValid = False
        
        if len(request.form['email']) < 1:
            flash("- An email address is required!")
            allfieldsValid = False
        elif len(request.form['email']) > 121:
            flash("- Please enter an email address that is 120 characters or less!")
            allfieldsValid = False
        elif not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!")
            allfieldsValid = False

        if len(request.form['password']) < 1:
            flash("- A password is required!")
            allfieldsValid = False
        elif len(request.form['password']) > 121:
            flash("- Please enter a password that is 120 characters or less!")
            allfieldsValid = False

        if len(request.form['confirm']) < 1:
            flash("- Please confirm your password!")
            allfieldsValid = False
        elif request.form['confirm'] != request.form['password']:
            flash("- Your passwords do not match!")
            allfieldsValid = False
        elif len(request.form['confirm']) > 121:
            flash("- Please enter a password that is 120 characters or less!")
            allfieldsValid = False

        if len(request.form['street']) < 1:
            flash("- A street address is required!")
            allfieldsValid = False
        elif len(request.form['street']) > 201:
            flash("- Please enter an address that is 200 characters or less!")
            allfieldsValid = False

        if len(request.form['city']) < 1:
            flash("- A city is required")
            allfieldsValid = False
        elif len(request.form['city']) > 121:
            flash("- Please enter city name that is 120 characters or less!")
            allfieldsValid = False

        if allfieldsValid == True:
            flash("You have successfully registered!")
        

        print(request.form)
        return redirect('/')

if __name__=="__main__":
    app.run(debug=True)