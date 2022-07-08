from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

import JapaneseDownload
import JapansesParsers
import os
import core_data_access_lib.entities as entity


# Tools to create the database
def initializeDatabase():
    os.mkdir('data')

    # Add JMdict data
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
    JapaneseDownload.download.JMdict()
    for kana, item in JapansesParsers.parseJMdict.parseEntries(os.path.join('data', 'JMdict_e_examp.xml')):
        vocabList = []
        if kana:
            for word in item.keys():
                definitions = '; '.join(item[word]['phrases'])
                parts = item[word]['part_of_speech']
                pos, isVerb, isTrans = simplifyPartOfSpeech(parts)
                if isVerb:
                    trans = isTrans
                else:
                    trans = ''
                examples = item[word]['examples']
                sentence = ''
                for example in examples:
                    sentence += example[3] + '\t' + example[2] + '\n'
                sentence = sentence[:-1]


                vocabList.append(entity.Vocab(
                    enc_vocab = word,
                    primary_eng_def = definitions,
                    part_of_speech = pos,
                    transitivity = trans,
                    ex_lit_sentence = sentence
                ))
        else:
            for word in item.keys():
                for pronounce in item[word].keys():
                    definitions = '; '.join(item[word][pronounce]['phrases'])
                    parts = item[word][pronounce]['part_of_speech']
                    pos, isVerb, isTrans = simplifyPartOfSpeech(parts)
                    if isVerb:
                        trans = isTrans
                    else:
                        trans = ''
                    examples = item[word][pronounce]['examples']
                    sentence = ''
                    for example in examples:
                        sentence += example[3] + '\t' + example[2] + '\n'
                    sentence = sentence[:-1]

                    vocabList.append(entity.Vocab(
                        enc_vocab = word,
                        pronuns = pronounce,
                        primary_eng_def = definitions,
                        part_of_speech = pos,
                        transitivity = trans,
                        ex_lit_sentence = sentence
                    ))

def simplifyPartOfSpeech(posList):
    pos = []
    isVerb = False
    isTrans = False
    for part in posList:
        if part in ["unclassified"]:
            pos.append(entity.Vocab.PartOfSpeech.UNKNOWN)
        elif part in ["noun (common) (futsuumeishi)", "adverbial noun (fukushitekimeishi)", "proper noun", "noun, used as a prefix", "noun, used as a suffix", "noun (temporal) (jisoumeishi)", "numeric", "counter"]:
            pos.append(entity.Vocab.PartOfSpeech.NOUN)
        elif part in ["pronoun"]:
            pos.append(entity.Vocab.PartOfSpeech.PRONOUN)
        elif part in ["prefix"]:
            pos.append(entity.Vocab.PartOfSpeech.PREFIX)
        elif part in ["suffix"]:
            pos.append(entity.Vocab.PartOfSpeech.SUFFIX)
        elif part in ["noun or verb acting prenominally", "adjective (keiyoushi)", "adjective (keiyoushi) - yoi/ii class", "'kari' adjective (archaic)", "'ku' adjective (archaic)", "adjectival nouns or quasi-adjectives (keiyodoshi)", "archaic/formal form of na-adjective", "nouns which may take the genitive case particle 'no'", "pre-noun adjectival (rentaishi)", "'shiku' adjective (archaic)", "'taru' adjective"]:
            pos.append(entity.Vocab.PartOfSpeech.ADJECTIVE)
        elif part in ["Ichidan verb"]:
            isVerb = True
            pos.append(entity.Vocab.PartOfSpeech.RU_VERB)
        elif part in ["Godan verb - -aru special class", "Godan verb with 'bu' ending", "Godan verb with 'gu' ending", "Godan verb with 'ku' ending", "Godan verb - Iku/Yuku special class", "Godan verb with 'mu' ending", "Godan verb with 'nu' ending", "Godan verb with 'ru' ending", "Godan verb with 'su' ending", "Godan verb with 'tsu' ending", "Godan verb with 'u' ending", "Godan verb - Uru old class verb (old form of Eru)"]:
            isVerb = True
            pos.append(entity.Vocab.PartOfSpeech.U_VERB)
        elif part in ["verb unspecified", "Ichidan verb - kureru special class", "Godan verb with 'ru' ending (irregular verb)", "Godan verb with 'u' ending (special class)", "Kuru verb - special class", "irregular nu verb", "irregular ru verb, plain form ends with -ri", "noun or participle which takes the aux. verb suru", "su verb - precursor to the modern suru", "suru verb - included", "suru verb - special class", "Ichidan verb - zuru verb (alternative form of -jiru verbs)"]:
            isVerb = True
            pos.append(entity.Vocab.PartOfSpeech.SPECIAL_VERB)
        elif part in ["copula"]:
            pos.append(entity.Vocab.PartOfSpeech.COPULA)
        elif part in ["particle"]:
            pos.append(entity.Vocab.PartOfSpeech.PARTICLE)
        elif part in ["adverb (fukushi)", "adverb taking the 'to' particle"]:
            pos.append(entity.Vocab.PartOfSpeech.ADVERB)
        elif part in ["conjunction"]:
            pos.append(entity.Vocab.PartOfSpeech.CONJUNCTION)
        elif part in ["expressions (phrases, clauses, etc.)","interjection (kandoushi)"]:
            pos.append(entity.Vocab.PartOfSpeech.INTERJECTION)
        elif part in ["auxiliary", "auxiliary adjective", "auxiliary verb"]:
            pos.append(entity.Vocab.PartOfSpeech.AUXILIARY)

        elif part in ["transitive verb"]:
            isVerb = True
            isTrans = True
        elif part in ["intransitive verb"]:
            isVerb = True
            isTrans = False

    return list(set(pos)), isVerb, isTrans


class PostDevelopCommand(develop):
    def run(self):
        initializeDatabase()

class PostInstallCommand(install):
    def run(self):
        initializeDatabase

# Read the README file
with open("README.md", 'r', encoding='utf-8') as f:
    longDes = f.read()

# Create setup
setup(
    name='Japanese_Dictionary_DataBase',
    version='0.0.1',
    author='34-Matt, CJordanGoodman',
    author_email='mmdstanley@gmail.com',
    description='Manages and accesses the SQL Japanese Dictionary Database',
    long_description=longDes,
    long_description_content_type="text/markdown",
    url='https://github.com/JapaneseDatabase/JPDB/wiki',
    project_urls={
        "Bug Tracker": "https://github.com/JapaneseDatabase/JPDB/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    packages=setuptools.find_packages(where=''),
    python_requires=">=3.6",
    cmdclass={
        "develop": PostDevelopCommand,
        'install': PostInstallCommand,
    },
)