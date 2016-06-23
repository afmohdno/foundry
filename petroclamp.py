from bottle import *
import requests
import json

application = default_app()

# Define an handler for the root URL of our application.
@route('/')
def main():
	return template("views/index.html")

@post('/contact-us')
def contact_us():

	name = request.forms.name
	email = request.forms.email
	message = request.forms.message

	requests.post(
		"https://api.mailgun.net/v3/mg.e2u.website/messages",
		auth=("api", "key-14366526c7caae8e8cd517d98329d19c"),
		data={"from": "Petroclamp Contact Us<petroclamp@e2u.website>",
			  "to": ["anasfaris@yahoo.com","afmohdno@gmail.com"],
			  "subject": "Message from Contact Us Page",
			  "html": template(
			  	'views/contact-email.html', 
			  	name=name,			  	
			  	message=message, 
			  	email=email)
	})

	return json.dumps({'result':'success'})

@route('/contact')
def contact():
	return template("views/contact.html")

@route('/about')
def about_us():
	return template("views/about.html")

@route('/about/background')
def about_us1():
	return template("views/background.html")

@route('/about/structure')
def about_us2():
	return template("views/structure.html")

@route('/about/policy')
def about_us3():
	return template("views/policy.html")

@route('/manufacturing')
def manufacturing():
	return template("views/manufacturing.html")

@route('/investment_casting')
def service1():
	return template("views/investment_casting.html")

@route('/sand_casting')
def service2():
	return template("views/sand_casting.html")

@route('/facility')
def service3():
	return template("views/facility.html")

@route('/quality/process')
def process():
	return template("views/qa.html")

@route('/quality/testing')
def testing():
	return template("views/testing.html")

@route('/customers')
def customers():
	return template("views/customers.html")

@route('/certificate')
def certificate():
	return template("views/certificate.html")

@route('/blank')
def blank():
	return template("views/blank-page.html")
	
@route('/favicon.ico')
def get_favicon():
    return server_static('favicon.ico')

# Define an handler for 404 errors.
@error(404)
def error_404(error):
	"""Return a custom 404 error."""
	return template("views/404.html")

# Define an handler for 500 errors.
@error(500)
def error_500(error):
	"""Return a custom 500 error."""
	return "Sorry, could not connect to server."

# specifying the path for the files
@route('/<filepath:path>')
@route('/about/<filepath:path>')
@route('/quality/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static/')

if __name__ == '__main__':
    application.run(reloader=True, host="0.0.0.0", port=int(os.environ.get("PORT", 9000)))