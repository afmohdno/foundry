from bottle import *

application = default_app()

# Define an handler for the root URL of our application.
@route('/')
def main():
	return template("views/index.html")

@route('/contact_us')
def contact():
	return template("views/contact.html")

@route('/tooling_making')
def service():
	return template("views/toolingmaking.html")

@route('/investment_casting')
def service():
	return template("views/investmentcasting.html")

@route('/tooling_making')
def service():
	return template("views/toolingmaking.html")

@route('/quality_assurance')
def QA():
	return template("views/qualityassurance.html")
	
@route('/favicon.ico')
def get_favicon():
    return server_static('favicon.ico')

# Define an handler for 404 errors.
@error(404)
def error_404(error):
	"""Return a custom 404 error."""
	return 'Sorry, Nothing at this URL.'

# Define an handler for 500 errors.
@error(500)
def error_500(error):
	"""Return a custom 500 error."""
	return "Sorry, couldn't connect to server ."

# specifying the path for the files
@route('/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static/')

if __name__ == '__main__':
    application.run(reloader=True, host="0.0.0.0", port=int(os.environ.get("PORT", 9000)))