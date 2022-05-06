from entities import *
from sql_dao import *

from typing import List


class JPDBAccessAPI:
	"""
	API that provides functions to read and modify the SQL databases underlying the JPDB project
	"""



	### KANJI API

	# TODO: Define method
	def add_kanji(kanji: Kanji) -> None:
		'''Add a new kanji to the dictionary
		If one already exists, it will create a new entry
		
		:param kanji: The kanji to be added to the database
		'''
		add_kanji([kanji])

	# TODO: Define method
	def batch_add_kanji(kanji_list: List[Kanji]) -> None:
		'''Add a list of new kanji to the dictionary
		If one already exists, it will create a new entry
		
		:param kanji_list: The list of kanji to be added to the database
		'''
		add_kanji(kanji_list)

	# TODO: Define method
	def edit_kanji(kanji: Kanji):
		''' Edits a kanji that is already in the list

		:param kanji: The kanji to edit in the database
		'''
		oldKanji = get_term(kanji.enc_character,Tag.TermType.KANJI)
		newKanji = kanji + oldKanji
		edit_kanji([newKanji])

	# TODO: Define method
	def batch_edit_kanji(kanji_list: List[Kanji]):
		''' Edits a list of kanji that is already in the list

		:param kanji_list: The list of kanji to edit in the database
		'''
		for kanji in kanji_list:
			oldKanji = get_term(kanji.enc_character,Tag.TermType.KANJI)
			newKanji = kanji + oldKanji
			edit_kanji([newKanji])

	# TODO: Define method
	def delete_kanji(kanji):
		raise NotImplementedError

	# TODO: Define method
	def batch_delete_kanji(kanji_list):
		raise NotImplementedError

	# TODO: Define method
	def add_tag_to_kanji(kanji, user_id, tag_id):
		raise NotImplementedError

	# TODO: Define method
	def remove_tag_from_kanji(kanji, user_id, tag_id):
		raise NotImplementedError

	# TODO: Define method
	def get_kanji_with_tag(tag_id, username="admin"):
		raise NotImplementedError

	# TODO: Define method
	def get_kanji(kanji):
		raise NotImplementedError




	### VOCAB API ###

	# TODO: Define method
	def add_kanji(kanji):
		raise NotImplementedError

	# TODO: Define method
	def batch_add_kanji(kanji_list):
		raise NotImplementedError

	# TODO: Define method
	def edit_kanji(kanji):
		raise NotImplementedError

	# TODO: Define method
	def batch_edit_kanji(kanji_list):
		raise NotImplementedError

	# TODO: Define method
	def delete_kanji(kanji):
		raise NotImplementedError

	# TODO: Define method
	def batch_delete_kanji(kanji_list):
		raise NotImplementedError

	# TODO: Define method
	def add_tag_to_kanji(kanji, user_id, tag_id):
		raise NotImplementedError

	# TODO: Define method
	def remove_tag_from_kanji(kanji, user_id, tag_id):
		raise NotImplementedError

	# TODO: Define method
	def get_kanji_with_tag(tag_id, username="admin"):
		raise NotImplementedError

	# TODO: Define method
	def get_kanji(kanji):
		raise NotImplementedError