import sqlite3
from entities import *

# NOTE: This script will not work unless the jp.db sqlite database has been set up as-per 
# https://github.com/JapaneseDatabase/JPDB/wiki/SQLite-Setup-Guide

### KANJI EDIT METHODS ###

# TODO: Define method
def add_kanji(kanji_list):
	conn = sqlite3.connect('jp.db')
	cursor = conn.cursor()

	execute_string = "INSERT INTO kanji (enc_char, onyomi_pros, kunyomi_pros, prim_eng_def, alt_eng_defs, " \
					 "ex_words, jlpt_lvl, ex_lit_sent, ex_fig_sent) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

	for kanji in kanji_list:
		cursor.execute(execute_string, kanji.return_list())

	conn.commit()
	conn.close()

# TODO: Define method
def edit_kanji(kanji_list):
	conn = sqlite3.connect('jp.db')
	cursor = conn.cursor()

	execute_string = "UPDATE kanji SET onyomi_pros = ?, kunyomi_pros = ?, prim_eng_def = ?, alt_eng_defs = ?, " \
					 "ex_words = ?, jlpt_lvl = ?, ex_lit_sent = ?, ex_fig_sent = ? WHERE enc_char = ?"

	for kanji in kanji_list:
		kanji_values = kanji.return_list()
		kanji_values.append(kanji_values.pop(0)) # Move first value to the end
		cursor.execute(execute_string, kanji_values)

	conn.commit()
	conn.close()

# TODO: Define method
def delete_kanji(kanji_list):
	conn = sqlite3.connect('jp.db')
	cursor = conn.cursor()

	execute_string = "DELETE FROM kanji WHERE enc_char = ?"

	for kanji in kanji_list:
		cursor.execute(execute_string, (kanji.enc_character,))

	conn.commit()
	conn.close()


### VOCAB EDIT METHODS ###

# TODO: Define method
def add_vocab(vocab_list):
	conn = sqlite3.connect('jp.db')
	cursor = conn.cursor()

	execute_string = "INSERT INTO vocab (enc_term, pros, prim_eng_def, alt_eng_defs, " \
					 "comp_kanji, part_of_speech, transitivity, ex_lit_sent, ex_fig_sent) " \
					 "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

	for vocab in vocab_list:
		cursor.execute(execute_string, vocab.return_list())

	conn.commit()
	conn.close()

# TODO: Define method
def edit_vocab(vocab_list):
	conn = sqlite3.connect('jp.db')
	cursor = conn.cursor()

	execute_string = "UPDATE vocab SET pros = ?, prim_eng_def = ?, alt_eng_defs = ?, " \
					 "comp_kanji = ?, part_of_speech = ?, transitivity = ?, ex_lit_sent = ?, ex_fig_sent = ? " \
					 "WHERE enc_term = ?"

	for vocab in vocab_list:
		vocab_values = vocab.return_list()
		vocab_values.append(vocab_values.pop(0)) # Move first value to the end
		cursor.execute(execute_string, vocab_values)

	conn.commit()
	conn.close()

# TODO: Define method
def delete_vocab(vocab_list):
	conn = sqlite3.connect('jp.db')
	cursor = conn.cursor()

	execute_string = "DELETE FROM vocab WHERE enc_term = ?"

	for vocab in vocab_list:
		cursor.execute(execute_string, (vocab.enc_vocab,))

	conn.commit()
	conn.close()


### USER EDIT METHODS ###

# TODO: Define method
def add_user(user):
	raise NotImplementedError

# TODO: Define method
def delete_user(user):
	raise NotImplementedError


### TAG EDIT METHODS ###

# TODO: Define method
def add_tag(tag_id, username, term_id, term_type):
	raise NotImplementedError

# TODO: Define method
def delete_tag(tag_id, username, term_id, term_type):
	raise NotImplementedError


### SEARCH METHODS ###

# TODO: Clean up method result
def get_terms_with_tag(tag_id, username, term_type):
	conn = sqlite3.connect('jp.db')
	cursor = conn.cursor()

	if term_type == Tag.TermType.KANJI:
		execute_string = "SELECT * FROM tag LEFT JOIN kanji ON tag.term_id = kanji.kanji_id WHERE " \
		"tag.term_type = \"kanji\" tag.username = \"{0}\", tag.tag_id = \"{1}\"".format(username, tag_id)
	elif term_type == Tag.TermType.VOCAB:
		execute_string = "SELECT * FROM tag LEFT JOIN vocab ON tag.term_id = vocab.term_id WHERE " \
		"tag.term_type = \"vocab\" tag.username = \"{0}\", tag.tag_id = \"{1}\"".format(username, tag_id)

	result = cursor.execute(execute_string).fetchall()[0]

	conn.commit()
	conn.close()

	return result

# TODO: clean up method result
def get_tags_for_user(username):
	conn = sqlite3.connect('jp.db')
	cursor = conn.cursor()

	execute_string = "SELECT DISTINCT tag_id FROM tag WHERE tag.username = \"{0}\"".format(username)

	result = cursor.execute(execute_string).fetchall()

	conn.commit()
	conn.close()

	return result

def get_term(enc_term, term_type):
	conn = sqlite3.connect('jp.db')
	cursor = conn.cursor()

	if term_type == Tag.TermType.KANJI:
		execute_string = "SELECT * FROM kanji WHERE enc_char = \"{0}\"".format(enc_term)
	elif term_type == Tag.TermType.VOCAB:
		execute_string = "SELECT * FROM vocab WHERE enc_term = \"{0}\"".format(enc_term)

	result = cursor.execute(execute_string).fetchall()[0]

	conn.commit()
	conn.close()

	if term_type == Tag.TermType.KANJI:
		return convert_sql_string_to_kanji(result)
	elif term_type == Tag.TermType.VOCAB:
		return convert_sql_string_to_vocab(result)


def convert_sql_string_to_kanji(row):
	return Kanji(row[1], onyomi_pros=row[2], kunyomi_pros=row[3], 
		primary_eng_def=row[4], alt_eng_defs=row[5], examp_words=row[6], jlpt_lvl=row[7], 
		ex_lit_sentence=row[8], ex_fig_sentence=row[9])


def convert_sql_string_to_vocab(row):
	return Vocab(row[1], pronuns=row[2], primary_eng_def=row[3], 
		alt_eng_defs=row[4], comp_kanji=row[5], part_of_speech=row[6], transitivity=row[7], 
		ex_lit_sentence=row[8], ex_fig_sentence=row[9])


if __name__ == '__main__':
	## The below code is an EXTREMELY basic sanity test. Be aware that it currently does not delete
	## the test data between runs, so over time it pollutes the tables with similar entries.
	## This should be replaced by more rigorous unit tests soon.

	add_kanji([Kanji(enc_character = "abcd"), Kanji(enc_character = "efgh")])
	add_vocab([Vocab(enc_vocab = "abcd"), Vocab(enc_vocab = "efgh")])
	print(get_term("abcd", Tag.TermType.KANJI))
	print(get_term("efgh", Tag.TermType.KANJI))
	print(get_term("abcd", Tag.TermType.VOCAB))
	print(get_term("efgh", Tag.TermType.VOCAB))

	edit_kanji([Kanji(enc_character = "abcd", jlpt_lvl='N2')])
	edit_vocab([Vocab(enc_vocab = "abcd", pronuns='Verb'), Vocab(enc_vocab = "efgh", pronuns='Noun')])
	print(get_term("abcd", Tag.TermType.KANJI))
	print(get_term("efgh", Tag.TermType.KANJI))
	print(get_term("abcd", Tag.TermType.VOCAB))
	print(get_term("efgh", Tag.TermType.VOCAB))

	delete_kanji([Kanji(enc_character = "abcd"), Kanji(enc_character = "efgh")])
	delete_vocab([Vocab(enc_vocab = "abcd"), Vocab(enc_vocab = "efgh")])
	print(get_term("abcd", Tag.TermType.KANJI))
	print(get_term("efgh", Tag.TermType.KANJI))
	print(get_term("abcd", Tag.TermType.VOCAB))
	print(get_term("efgh", Tag.TermType.VOCAB))
