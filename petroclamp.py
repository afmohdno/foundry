from bottle import *

application = default_app()

# Define an handler for the root URL of our application.
@route('/')
def main():
	return template("views/index.html")

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

@route('/products')
def product():
	return template("views/product.html")

@route('/services')
def service():
	return template("views/services.html")

@route('/investment_casting')
def service():
	return template("views/investmentcasting.html")

@route('/qa')
def QA():
	return template("views/qa.html")

@route('/customers')
def customers():
	return template("views/customers.html")

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
	return "Sorry, couldn't connect to server ."

# specifying the path for the files
@route('/<filepath:path>')
@route('/about/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static/')

if __name__ == '__main__':
    application.run(reloader=True, host="0.0.0.0", port=int(os.environ.get("PORT", 9000)))