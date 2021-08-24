from flask import Flask, render_template, request

print(__name__)
app = Flask (__name__)

@app.route ("/") # Start page
def start_page():
    return "<p><a href='/index'>You can check content warnings on this site.</a></p>"

@app.route ("/index")
def index_page():
    return render_template ("index.html")

series_list = ['A very English Scandal', 'Akte X', 'Babylon Berlin', 'Bones', 'Breaking Bad', 'Call the midwife', 'Charite', 'Chernobyl', 'Death in paradise', 'Der Name der Rose', 'Dexter', 'Die Sopranos', 'Doctor Who', 'Downton Abbey', 'Dr. House', 'Escape artist', 'Firefly', 'Fleabag', 'Gotham', 'Grimm', 'Halt and catch fire', 'His dark materials', 'Inspector Barnaby', 'Killing Eve', 'Limitless', 'Lovecraft Country', 'Monk', 'MotherFatherSon', 'Mr. Robot', 'Orange is the new black', 'Outlander', 'Penny Dreadful', 'Retribution', 'S.W.A.T.', 'Sharp Objects', 'Supernatural', 'Tabula Rasa', 'Teen Wolf', 'The Alienist', 'The Big Bang Theory', 'The Crown', 'The Flash', 'The Good Doctor', 'The IT Crowd', 'The Last Kingdom', 'The miniaturist', 'The Outsider', 'The Pacific', 'The Undoing', 'True Blood', 'Vikings', 'Watchmen', 'Westworld', 'Years & Years']
animal_death = ['A very English Scandal', 'Akte X', 'Babylon Berlin', 'Bones', 'Breaking Bad','Call the midwife', 'Charite', 'Chernobyl', 'Death in paradise', 'Der Name der Rose', 'Dexter', 'Die Sopranos', 'Doctor Who', 'Downton Abbey', 'Dr. House', 'Firefly', 'Gotham', 'Grimm', 'Halt and catch fire', 'His dark materials', 'Inspector Barnaby', 'Killing Eve', 'Lovecraft Country', 'Monk', 'MotherFatherSon', 'Mr. Robot', 'Orange is the new black', 'Outlander', 'Penny Dreadful', 'Retribution', 'S.W.A.T.', 'Sharp Objects', 'Supernatural', 'Tabula Rasa', 'Teen Wolf', 'The Alienist', 'The Big Bang Theory', 'The Crown', 'The Flash', 'The Good Doctor', 'The Last Kingdom', 'The miniaturist', 'The Outsider', 'The Pacific', 'True Blood', 'Vikings', 'Watchmen', 'Westworld']
suicide = ['A very English Scandal', 'Akte X', 'Babylon Berlin', 'Bones', 'Breaking Bad', 'Call the midwife', 'Charite', 'Chernobyl', 'Death in paradise', 'Der Name der Rose', 'Dexter', 'Die Sopranos', 'Doctor Who', 'Downton Abbey', 'Dr. House', 'Firefly', 'Fleabag', 'Gotham', 'Grimm', 'Halt and catch fire', 'His dark materials', 'Inspector Barnaby', 'Killing Eve', 'Monk', 'MotherFatherSon', 'Mr. Robot', 'Orange is the new black', 'Outlander', 'Penny Dreadful', 'Retribution', 'Sharp Objects', 'Supernatural', 'Tabula Rasa', 'Teen Wolf', 'The Alienist', 'The Crown', 'The Flash', 'The Good Doctor', 'The IT Crowd', 'The Outsider', 'The Pacific', 'True Blood', 'Vikings', 'Watchmen', 'Westworld']
sexual_assault = ['Akte X', 'Babylon Berlin','Bones', 'Breaking Bad', 'Call the midwife', 'Der Name der Rose', 'Dexter', 'Die Sopranos', 'Downton Abbey', 'Dr. House', 'Escape artist', 'Firefly', 'Fleabag', 'Grimm', 'Inspector Barnaby', 'Lovecraft Country', 'Mr. Robot', 'Orange is the new black', 'Outlander', 'Penny Dreadful', 'Retribution', 'S.W.A.T.', 'Sharp Objects', 'Supernatural', 'The Alienist', 'The Good Doctor', 'The IT Crowd', 'The Last Kingdom', 'The Outsider', 'The Undoing', 'True Blood', 'Vikings', 'Watchmen', 'Westworld']
self_injurious_behavior = ['Akte X', 'Bones', 'Breaking Bad', 'Call the midwife', 'Charite', 'Chernobyl', 'Der Name der Rose', 'Dexter', 'Die Sopranos', 'Downton Abbey', 'Dr. House', 'Firefly', 'Fleabag', 'Gotham', 'Grimm', 'His dark materials', 'Inspector Barnaby', 'Killing Eve', 'Lovecraft Country', 'MotherFatherSon', 'Mr. Robot', 'Orange is the new black', 'Outlander', 'Penny Dreadful', 'Retribution', 'Sharp Objects', 'Supernatural', 'Tabula Rasa', 'Teen Wolf', 'The Alienist', 'The Crown', 'The Flash', 'The Good Doctor', 'The IT Crowd', 'The Outsider', 'True Blood', 'Vikings', 'Westworld']
child_harm = ['Akte X', 'Babylon Berlin', 'Bones', 'Breaking Bad', 'Call the midwife', 'Charite', 'Chernobyl', 'Dexter', 'Die Sopranos', 'Doctor Who', 'Downton Abbey', 'Dr. House', 'Firefly', 'Gotham', 'His dark materials', 'Inspector Barnaby', 'Killing Eve', 'Lovecraft Country', 'MotherFatherSon', 'Mr. Robot', 'Orange is the new black', 'Outlander', 'Penny Dreadful', 'S.W.A.T.', 'Sharp Objects', 'Supernatural', 'Tabula Rasa', 'Teen Wolf', 'The Alienist', 'The Big Bang Theory', 'The Flash', 'The Good Doctor', 'The Outsider', 'The Undoing', 'True Blood', 'Vikings', 'Watchmen', 'Westworld']

@app.route("/series/<series>")
def series_page(series):
    return render_template("series.html",series = series)

@app.route("/series_list")
def series_list_page():
    return render_template ("series_list.html", series_list = series_list )

@app.route("/animal_death")
def animal_death_page():
    return render_template ("animal_death.html", animal_death = animal_death)

@app.route("/self_injurious_behavior")
def self_injurious_behavior_page():
    return render_template ("self_injurious_behavior.html", self_injurious_behavior = self_injurious_behavior)

@app.route("/suicide")
def suicide_page():
    return render_template ("suicide.html", suicide = suicide)

@app.route("/sexual_assault")
def sexual_assault_page():
    return render_template ("sexual_assault.html", sexual_assault = sexual_assault)

@app.route("/child_harm")
def child_harm_page():
    return render_template ("child_harm.html", child_harm = child_harm)


@app.route('/search', methods = ['GET', 'POST'])
def search():
	result = []
	query = ''
	
	if request.method == 'POST':
		query = request.form['query'].strip()
		result = [series for series in series_list	if query.lower() in series.lower()]
	
	return render_template( 'search.html', query = query, series_list = result )

headings = ('Series', 'Animal death', 'Suicide', 'Sexual Assault', 'Self injurious behavior', 'Child harm')
data = (
('A very English Scandal', 'yes', 'yes', 'no', 'no', 'no'),
('Akte X', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Babylon Berlin', 'yes', 'yes', 'yes', 'no', 'yes'),
('Bones', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Breaking Bad', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Call the Midwife', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Charité', 'yes', 'yes', 'no', 'yes', 'yes'),
('Chernobyl', 'yes', 'yes', 'no', 'yes', 'yes'),
('Death in paradise', 'yes', 'yes', 'no', 'no', 'no'),
('Der Name der Rose', 'yes', 'yes', 'yes', 'yes', 'no'),
('Dexter', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Die Sopranos', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Doctor Who', 'yes', 'yes', 'no', 'no', 'yes'),
('Downton Abbey', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Dr. House', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Escape artist', 'no', 'no', 'yes', 'no', 'no'),
('Firefly', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Fleabag', 'no', 'yes', 'yes', 'yes', 'no'),
('Gotham', 'yes', 'yes', 'no', 'yes', 'yes'),
('Grimm', 'yes', 'yes', 'yes', 'yes', 'no'),
('Halt and catch fire', 'yes', 'yes', 'no', 'no', 'no'),
('His dark materials', 'yes', 'yes', 'no', 'yes', 'yes'),
('Inspector Barnaby', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Killing Eve', 'yes', 'yes', 'no', 'yes', 'yes'),
('Limitless', 'no', 'no', 'no', 'no', 'no'),
('Lovecraft Country', 'yes', 'no', 'yes', 'yes', 'yes'),
('Monk', 'yes', 'yes', 'no', 'no', 'no'),
('MotherFatherSon', 'yes', 'yes', 'no', 'yes', 'yes'),
('Mr. Robot', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Orange is the new black', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Outlander', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Penny Dreadful', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Retribution', 'yes', 'yes', 'yes', 'yes', 'no'),
('S.W.A.T.', 'yes', 'no', 'yes', 'no', 'yes'),
('Sharp Objects', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Supernatural', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Tabula Rasa', 'yes', 'yes', 'no', 'yes', 'yes'),
('Teen Wolf', 'yes', 'yes', 'no', 'yes', 'yes'),
('The Alienist', 'yes', 'yes', 'yes', 'yes', 'yes'),
('The Big Bang Theory', 'yes', 'no', 'no', 'no', 'yes'),
('The Crown', 'yes', 'yes', 'no', 'yes', 'no'),
('The Flash', 'yes', 'yes', 'no', 'yes', 'yes'),
('The Good Doctor', 'yes', 'yes', 'yes', 'yes', 'yes'),
('The IT Crowd', 'no', 'yes', 'yes', 'yes', 'no'),
('The Last Kingdom', 'yes', 'no', 'yes', 'no', 'no'),
('The miniaturist', 'yes', 'no', 'no', 'no', 'no'),
('The Outsider', 'yes', 'yes', 'yes', 'yes', 'yes'),
('The Pacific', 'yes', 'yes', 'no', 'no', 'no'),
('The Undoing', 'no', 'no', 'yes', 'no', 'yes'),
('True Blood', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Vikings', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Watchmen', 'yes', 'yes', 'yes', 'no', 'yes'),
('Westworld', 'yes', 'yes', 'yes', 'yes', 'yes'),
('Years & Years', 'no', 'no', 'no', 'no', 'no'),
)

@app.route("/table")
def table_page():
    return render_template ("table.html", headings=headings, data=data)