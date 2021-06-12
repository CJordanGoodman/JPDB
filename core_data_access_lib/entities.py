class Kanji:
	"""Represents a single Kanji"""	
	def __init__(self, enc_character, onyomi_pros=None, kunyomi_pros=None, primary_eng_def=None, \
		alt_eng_defs=None, examp_words=None, jlpt_lvl=None, ex_lit_sentence=None, ex_fig_sentence=None):
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
			self.enc_character, self.onyomi_pros or "", self.kunyomi_pros or "", self.primary_eng_def or "", 
			self.alt_eng_defs or "", self.examp_words or "", self.jlpt_lvl or "", self.ex_lit_sentence or "", 
			self.ex_fig_sentence or "")
		

class Vocab:
	"""Represents a single Vocab term"""	
	def __init__(self, enc_vocab, pronuns=None, primary_eng_def=None, alt_eng_defs=None, \
		comp_kanji=None, part_of_speech=None, transitivity = None, ex_lit_sentence=None, ex_fig_sentence=None):
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
			self.enc_vocab, self.pronuns or "", self.primary_eng_def or "", self.alt_eng_defs or "", 
			self.comp_kanji or "", self.part_of_speech or "", self.transitivity or "", 
			self.ex_lit_sentence or "", self.ex_fig_sentence or "")

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
		return "({0})".format(username)

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

	def __str(self):
		return "({0}, {1}, {2}, {3})".format(username, tag_id, term_id, term_type)

	class TermType:
		"""
		Enum representing the possible types of terms.
		"""
		KANJI = 0
		VOCAB = 1
