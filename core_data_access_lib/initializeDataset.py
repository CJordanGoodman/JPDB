from os import posix_fallocate
from access_api import *
import JapaneseDownload.download as jd
from JapaneseParsers import *
from entities import *

def addJMdict(archaic=False, nsfw=True):
    fileName = jd.loadJMdict()
    for kana, item in parseJMdict.parseEntries(fileName, archaic, nsfw):
        
        if kana:
            for word, entry in item.items():
                # Get Definitions
                primary_eng_def = None
                altDefList = []
                for defin in entry['phrases'].keys():
                    if primary_eng_def is None:
                        primary_eng_def = defin
                    else:
                        altDefList.append(defin)
                alt_eng_defs = ','.join(altDefList)
                # Get Part-of-Speech
                pos = entry['part_of_speech']
                part_of_speech = ','.join(extractPosString(pos))

                Vocab(word, pronuns, primary_eng_def, alt_eng_defs, '', part_of_speech, transitivity, ex_lit_sentence, ex_fig_sentence)            

        # Print words with non-Kana elements
        else:
            for word, entry in item.items():
                # Get Kanji components
                comp_kanji = ','.join(extractNonKana(word))
                # Get Definitions
                primary_eng_def = None
                altDefList = []
                for defin in entry['phrases'].keys():
                    if primary_eng_def is None:
                        primary_eng_def = defin
                    else:
                        altDefList.append(defin)
                alt_eng_defs = ','.join(altDefList)
                # Get Part-of-Speech
                pos = entry['part_of_speech']
                part_of_speech = ','.join(extractPosString(pos))
        
                Vocab(word, pronuns, primary_eng_def, alt_eng_defs, comp_kanji, part_of_speech, transitivity, ex_lit_sentence, ex_fig_sentence)

def isHiragana(character):
    xChar = ord(character)
    return (xChar >= 0x3040) and (xChar <= 0x309f)

def isKatakana(character):
    xChar = ord(character)
    return (xChar >= 0x30a0) and (xChar <= 0x30ff)

def isPunctuation(character):
    xChar = ord(character)
    return (xChar >= 0x3000) and (xChar <= 0x303f)

def isHalfRoman(character):
    xChar = ord(character)
    return (xChar >= 0xff00) and (xChar <= 0xffef)

def extractNonKana(word):
    '''Returns a list of non-kana elements from a string
    '''
    return [v for v in word if not (isHalfRoman(v) and isHiragana(v) and isKatakana(v) and isPunctuation(v))]

def extractPosString(poss):
    '''Converts list of string of speech into a binary representation using the Vocab enum values
    '''
    posList = set()

    for pos in poss:
        pos = pos.lower()

        if (pos in ['counter', 'numeric']) or ('noun' in pos and 'pronoun' not in pos and 'prenominal' not in pos and 'pre-noun' not in pos):
            posList.add(Vocab.PartOfSpeech.NOUN)
        if (pos in ['pronoun']):
            posList.add(Vocab.PartOfSpeech.PRONOUN)
        if (pos in ['prefix']):
            posList.add(Vocab.PartOfSpeech.PREFIX)
        if (pos in ['suffix']):
            posList.add(Vocab.PartOfSpeech.SUFFIX)
        if ('adjectiv' in pos):
            posList.add(Vocab.PartOfSpeech.ADJECTIVE)
        if ('ichidan verb' in pos):
            posList.add(Vocab.PartOfSpeech.RU_VERB)
        if ('godan verb' in pos and 'irregular' not in pos):
            posList.add(Vocab.PartOfSpeech.U_VERB)
        if ('suru verb' in pos) or ('kuru verb' in pos) or ('irregular' in pos) or ('special' in pos):
            posList.add(Vocab.PartOfSpeech.SPECIAL_VERB)
        if (pos in ['copula']):
            posList.add(Vocab.PartOfSpeech.COPULA)
        if (pos in ['particle']):
            posList.add(Vocab.PartOfSpeech.PARTICLE)
        if ('adverb' in pos) or ('prenominal' in pos):
            posList.add(Vocab.PartOfSpeech.ADVERB)
        if (pos in ['conjunction']):
            posList.add(Vocab.PartOfSpeech.CONJUNCTION)
        if ('expressions' in pos) or ('interjection' in pos):
            posList.add(Vocab.PartOfSpeech.INTERJECTION)
        if ('auxiliary' in pos):
            posList.add(Vocab.PartOfSpeech.AUXILIARY)

    if len(posList) < 1:
        return 0
    
    sumResult = 0
    for num in posList:
        sumResult += 2 ** num
    return sumResult
