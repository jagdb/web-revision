from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__) #using flask class to instantiate app
print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("database.txt", mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message'] 
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open("database.csv", mode='a', newline='') as database2:
        dw = csv.DictWriter(database2, delimiter=',', fieldnames=['email','subject','message'])
        dw.writerow(data)

# Write the header to the CSV file
headerlist = ['email','subject','message']
with open("database.csv", mode='w', newline='') as database2:
    dw = csv.DictWriter(database2, delimiter=',', fieldnames=headerlist)
    dw.writeheader()        
    
        




@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() #turning form data into dictionary
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return'did not save to database'
    else:
        return 'something went wrong. Try again'