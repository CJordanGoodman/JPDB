# NOTE: Multiple entries should be separated by semicolons (definition 1;def2; def in tion 3)

from _typeshed import Self


def __addStr(clf, str1: str, str2: str) -> str:
	''' Adds str1 to str2 with a semicolon while removing leading and trailing commas
	Needs to check a previous entries and remove duplicates
	'''
	strList = str1.split(';')
	strList.extend(str2.split(';'))
	strList = [s.strip() for s in strList] # Remove excess white space
	strList = list(set(strList)) # Remove duplicates
	return ';'.join(strList)

class Kanji:
	"""Represents a single Kanji"""	
	def __init__(self, enc_character, onyomi_pros='', kunyomi_pros='', primary_eng_def='', \
		alt_eng_defs='', examp_words='', jlpt_lvl='', ex_lit_sentence='', ex_fig_sentence=''):
		"""
		Form a Kanji.

		Keyword arguments:
		enc_character -- UTF-8 encoded Kanji
		onyomi_pros -- Comma separated UTF-8 on'yomi kana pronunciations in descending order of prevalence
		kunyomi_pros -- Comma separated UTF-8 kun'yomi kana pronunciations in descending order of prevalence
		primary_eng_def -- Most prevalent english definition of the kanji
		alt_eng_defs -- Comma separated english definitions of the kanji
		examp_words -- Comma separated list of words/terms using this kanji (UTF-8 encoded)
		jlpt_lvl -- JLPT level, None to indicate unknown/undefined
		ex_lit_sentence -- Example sentence using the kanji for its literal meaning (UTF-8 encoded)
		ex_fig_sentence -- Example sentence using the kanji figuratively (UTF-8 encoded)
		"""
		self.enc_character = enc_character 
		self.onyomi_pros = onyomi_pros 
		self.kunyomi_pros = kunyomi_pros
		self.primary_eng_def = primary_eng_def
		self.alt_eng_defs = alt_eng_defs
		self.examp_words = examp_words
		self.jlpt_lvl = jlpt_lvl
		self.ex_lit_sentence = ex_lit_sentence
		self.ex_fig_sentence = ex_fig_sentence

	def __str__(self):
		return "(\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \"{6}\", \"{7}\", \"{8}\")".format(
			self.enc_character, self.onyomi_pros, self.kunyomi_pros, self.primary_eng_def, 
			self.alt_eng_defs, self.examp_words, self.jlpt_lvl, self.ex_lit_sentence, 
			self.ex_fig_sentence)

	def return_list(self):
		''' Returns data as a list

		Returns list in form (enc, onyomi, kunyomi, primary, alt, example, lvl, ex_lit, ex_fig)
		'''
		return [self.enc_character, self.onyomi_pros, self.kunyomi_pros, self.primary_eng_def, 
			self.alt_eng_defs, self.examp_words, self.jlpt_lvl, self.ex_lit_sentence, self.ex_fig_sentence]

	def combine(self, newKanji: 'Kanji') -> bool:
		''' Adds information from another Kanji object if the character is the same
		newKanji: another Kanji object with the missing information
		
		Returns boolean if operation is successful (True)
		'''
		if self.enc_character == newKanji.enc_character:
			self.onyomi_pros = __addStr(self.onyomi_pros, newKanji.onyomi_pros)
			self.kunyomi_pros = __addStr(self.kunyomi_pros, newKanji.kunyomi_pros)
			self.primary_eng_def = __addStr(self.primary_eng_def, newKanji.primary_eng_def)
			self.alt_eng_defs = __addStr(self.alt_eng_defs, newKanji.alt_eng_defs)
			self.examp_words = __addStr(self.examp_words, newKanji.examp_words)
			self.jlpt_lvl = __addStr(self.jlpt_lvl, newKanji.jlpt_lvl)
			self.ex_lit_sentence = __addStr(self.ex_lit_sentence, newKanji.ex_lit_sentence)
			self.ex_fig_sentence = __addStr(self.ex_fig_sentence, newKanji.ex_fig_sentence)
			
			return True
		else:
			return False

	def __add__(self, newKanji: 'Kanji') -> 'Kanji':
		'''Adds two Kanji objects together (Kanji + Kanji)
		If newKanji does not use the same enc_character, will return the left Kanji object
		'''
		if self.enc_character == newKanji.enc_character:
			onyomi_pros = __addStr(self.onyomi_pros, newKanji.onyomi_pros)
			kunyomi_pros = __addStr(self.kunyomi_pros, newKanji.kunyomi_pros)
			primary_eng_def = __addStr(self.primary_eng_def, newKanji.primary_eng_def)
			alt_eng_defs = __addStr(self.alt_eng_defs, newKanji.alt_eng_defs)
			examp_words = __addStr(self.examp_words, newKanji.examp_words)
			jlpt_lvl = __addStr(self.jlpt_lvl, newKanji.jlpt_lvl)
			ex_lit_sentence = __addStr(self.ex_lit_sentence, newKanji.ex_lit_sentence)
			ex_fig_sentence = __addStr(self.ex_fig_sentence, newKanji.ex_fig_sentence)
			
			return Kanji(self.enc_character,onyomi_pros, kunyomi_pros, primary_eng_def,
				alt_eng_defs, examp_words, jlpt_lvl, ex_lit_sentence, ex_fig_sentence)
		else:
			return self

class Vocab:
	"""Represents a single Vocab term"""	
	def __init__(self, enc_vocab, pronuns='', primary_eng_def='', alt_eng_defs='', \
		comp_kanji='', part_of_speech='', transitivity='', ex_lit_sentence='', ex_fig_sentence=''):
		"""
		Form a Vocab.

		Keyword arguments:
		enc_vocab -- UTF-8 encoded Vocab
		pronuns -- Comma separated UTF-8 pronunciations in descending order of prevalence
		primary_eng_def -- Most prevalent english definition of the kanji
		alt_eng_defs -- Comma separated english definitions of the kanji
		comp_kanji -- Comma separated list of kanji using this term (UTF-8 encoded)
		part_of_speech -- Enum indicating which part of speech the term is classified as
		transitivity -- Enum indicating whether a verb is transitive or not. Unused for non-verbs
		ex_lit_sentence -- Example sentence using the kanji for its literal meaning (UTF-8 encoded)
		ex_fig_sentence -- Example sentence using the kanji figuratively (UTF-8 encoded)
		"""
		self.enc_vocab = enc_vocab
		self.pronuns = pronuns 
		self.primary_eng_def = primary_eng_def
		self.alt_eng_defs = alt_eng_defs
		self.comp_kanji = comp_kanji
		self.part_of_speech = part_of_speech
		self.transitivity = transitivity
		self.ex_lit_sentence = ex_lit_sentence
		self.ex_fig_sentence = ex_fig_sentence

	def __str__(self):
		return "(\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \"{6}\", \"{7}\", \"{8}\")".format(
			self.enc_vocab, self.pronuns, self.primary_eng_def, self.alt_eng_defs, self.comp_kanji, 
			self.part_of_speech, self.transitivity, self.ex_lit_sentence, self.ex_fig_sentence)

	def return_list(self):
		''' Returns data as a list

		Returns list in form (enc, pronouns, primary, alt, kanji, pos, transitivity, lvl, ex_lit, ex_fig)
		'''
		return [self.enc_vocab, self.pronuns, self.primary_eng_def, self.alt_eng_defs, self.comp_kanji, 
			self.part_of_speech, self.transitivity, self.ex_lit_sentence, self.ex_fig_sentence]

	def combine(self, newVocab: 'Vocab') -> bool:
		''' Adds information from another Vocab object if the word is the same
		newVocab: another Vocab object with the missing information
		
		Returns boolean if operation is successful (True)
		'''
		if self.enc_vocab == newVocab.enc_vocab:
			self.pronuns = __addStr(self.pronuns, newVocab.pronuns)
			self.primary_eng_def = __addStr(self.primary_eng_def, newVocab.primary_eng_def)
			self.alt_eng_defs = __addStr(self.alt_eng_defs, newVocab.alt_eng_defs)
			self.comp_kanji = __addStr(self.comp_kanji, newVocab.comp_kanji)
			self.part_of_speech = __addStr(self.part_of_speech, newVocab.part_of_speech)
			self.transitivity = __addStr(self.transitivity, newVocab.transitivity)
			self.ex_lit_sentence = __addStr(self.ex_lit_sentence, newVocab.ex_lit_sentence)
			self.ex_fig_sentence = __addStr(self.ex_fig_sentence, newVocab.ex_fig_sentence)

			return True
		else:
			return False

	def __add__(self, newVocab: 'Vocab') -> 'Vocab':
		'''Adds two Vocab objects together (Vocab + Vocab)
		If newKanji does not use the same enc_character, will return the left Vocab object
		'''
		if self.enc_vocab == newVocab.enc_vocab:
			pronuns = __addStr(self.pronuns, newVocab.pronuns)
			primary_eng_def = __addStr(self.primary_eng_def, newVocab.primary_eng_def)
			alt_eng_defs = __addStr(self.alt_eng_defs, newVocab.alt_eng_defs)
			comp_kanji = __addStr(self.comp_kanji, newVocab.comp_kanji)
			part_of_speech = __addStr(self.part_of_speech, newVocab.part_of_speech)
			transitivity = __addStr(self.transitivity, newVocab.transitivity)
			ex_lit_sentence = __addStr(self.ex_lit_sentence, newVocab.ex_lit_sentence)
			ex_fig_sentence = __addStr(self.ex_fig_sentence, newVocab.ex_fig_sentence)

			return Vocab(self.enc_vocab, pronuns, primary_eng_def, alt_eng_defs,
				comp_kanji, part_of_speech, transitivity, ex_lit_sentence, ex_fig_sentence)
		else:
			return self

	class PartOfSpeech:
		"""
		Enum representing all possible parts of speech for terms as listed at
		https://en.wikibooks.org/wiki/Japanese/Grammar#Parts_of_speech
		"""
		NOUN = 0
		PRONOUN = 1
		NA_ADJECTIVE = 2
		VERB = 3
		I_ADJECTIVE = 4
		COPULA = 5
		PARTICLE = 6
		ADVERB = 7
		CONJUNCTION = 8
		INTERJECTION = 9



	class Transitivity:
		"""Enum indicating whether a verb is transitive or intransitive"""
		TRANSITIVE = 0
		INTRANSITIVE = 1
		NOT_APPLICABLE = 2


class User:
	"""Represents a single User"""	
	def __init__(self, username):
		"""
		Form a User.

		Keyword arguments:
		username -- Unique identifier for the user
		"""
		self.username = username

	def __str__(self):
		return "({0})".format(self.username)

class Tag:
	"""Represents a single Tag"""
	def __init__(self, tag_id, username, term_id, term_type):
		"""
		For a Tag.

		Keyword arguments:
		tag_id -- Identifier for the tag
		username -- Identifier for the user owning the tag
		term_id -- Identifier for the term to be tagged
		term_type -- Enum indicating whether the term is a Kanji or a Vocab
		"""
		self.tag_id = tag_id
		self.username = username
		self.term_id = term_id
		self.term_type = term_type

	def __str__(self):
		return "({0}, {1}, {2}, {3})".format(self.username, self.tag_id, self.term_id, self.term_type)

	class TermType:
		"""
		Enum representing the possible types of terms.
		"""
		KANJI = 0
		VOCAB = 1
