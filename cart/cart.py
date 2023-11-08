
class Cart():
	def __init__(self, request):
		self.session = request.session

		# Get the current session key if it exists
		cart = self.session.get('session_key')

		# If the user is new, no session key!  Create one!
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}


		# Make sure cart is available on all pages of site
		self.cart = cart

	def add(self, product):
		product_id = str(product.id)

		# Logic
		if product_id in self.cart:
			pass
		else:
			self.cart[product_id] = {'price': str(product.price)}

		self.session.modified = True



