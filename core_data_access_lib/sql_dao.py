class SqlDao:
	"""
	Class that adapts local data types into SQL queries and fulfills data requests
	"""

	# TODO: Determine state needed for class, define initialization
	def __init__(self):
		raise NotImplementedError

	# TODO: Define method
	def add_kanji(kanji_list):
		raise NotImplementedError

	# TODO: Define method
	def edit_kanji(kanji_list):
		raise NotImplementedError

	# TODO: Define method
	def delete_kanji(kanji_list):
		raise NotImplementedError

	# TODO: Define method
	def add_vocab(vocab_list):
		raise NotImplementedError

	# TODO: Define method
	def edit_vocab(vocab_list):
		raise NotImplementedError

	# TODO: Define method
	def delete_vocab(vocab_list):
		raise NotImplementedError

	# TODO: Define method
	def add_user(user):
		raise NotImplementedError

	# TODO: Define method
	def delete_user(user):
		raise NotImplementedError

	# TODO: Define method
	def add_tag(tag_id, username, term_id, term_type):
		raise NotImplementedError

	# TODO: Define method
	def delete_tag(tag_id, username, term_id, term_type):
		raise NotImplementedError

	# TODO: Define method
	def get_terms_with_tag(tag_id, username, term_type):
		raise NotImplementedError

	# TODO: Definte method
	def get_term(term_id, term_type):
		raise NotImplementedError