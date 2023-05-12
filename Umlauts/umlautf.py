# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:59:35 2019

@author: Mariia
"""
import os
import hunspell
spellchecker = hunspell.HunSpell(os.getcwd() + "\\de_DE.dic",
                                 os.getcwd() + "\\de_DE.aff")
import nltk # nlp Python library
enc = spellchecker.get_dic_encoding() # dictionary's encoding
from sacremoses import MosesTokenizer, MosesDetokenizer # detokenizing package
md = MosesDetokenizer() 

misspellings = {u"AEffaeren": u"Affären",
               u"AEffare": u"Affäre",
               u"AEffaere": u"Affäre",
               u"OEkoe": u"Öko",
               u"OElivenoel": u"Olivenöl",
               u"UEbeschuesse": u"Überschüsse",
               u"UEberschusse": u"Überschüsse",
               u"AEusserungven": u"Äußerungen",
               u"AEusserungsrecht": u"Äußerungsrecht",
               u"UEbergangsszeiten": u"Übergangszeiten",
               u"AEusserungenvon": u"Äußerungen von",
               u"AEusserungs": u"Äußerungs",
               u"OElnachfragegroessen": u"Ölnachfragegrössen",
               u"UEbergangssstems": u"Übergangsystems",
               u"UEbeschuss": u"Überschuss",
               u"AEuch": u"Auch",
               u"OEinzelwagen": u"Einzelwagen",
               u"OEffung": u"Öffnung",
               u"OEfnung": u"Öffnung",
               u"OElxporte": u"Ölexporte",
               u"UEbereaktion": u"Überreaktion",
               u"OEfenbau": u"Öfenbau",
               u"UEbestunden": u"Überstunden",
               u"UEbernahmeund": u"Übernahme und",
               u"OEhlbohrdichtung": u"Ölbohrdichtung",
               u"OEkound": u"Öko und",
               u"UEergangsregelung": u"Übergangsregelung",
               u"AEngst": u"Angst",
               u"UEberrnahme": u"Übernahme",
               u"Aepfel saeure": u"Äpfelsäure",
               u"UEberraschang": u"Überraschung",
               u"UEberlandwk": u"Überlandwerk",
               u"AEnleger": u"Anleger",
               u"UEertragungstechnik": u"Übertragungstechnik",
               u"UEbenahme": u"Übernahme",
               u"UEberinterpration": u"Überinterpretation",
               u"OECDneben": u"OECD neben"}

class spell(): 
    
    def __init__(self, document):
        self.docs = document
        self.misspellings = misspellings
        
    def replace_umlaut(self):
        # if the text does not contain any umlaut
        if not any(uml in self.docs for uml in [u"ä", u"ö", u'ü', u'ß', u"Ä", u"Ö", u"Ü"]):
            # To split examples like 'STEUERN/Bundesrechnungshof' into two tokens with nltk,
            # replace '/' with ' / '.
            self.docs = self.docs.replace('/', ' / ')
            # '-Foerderung' => ' - Foerderung'
            self.docs = self.docs.replace('-', ' - ')
            
            tokens = nltk.word_tokenize(self.docs)  # tokenize a text
            tokens_new = []                         # empty list for a clean text
            for t in tokens:
                # check the token only if it contains an umlaut replacement
                if any(urepl in t for urepl in [u'ae', u'oe', u'ue', u'ss', u'AE', u'OE', u'UE']):
                    # proceed if the token does not contain any special character
                    if not any(s in t for s in [u'\xbc', u'\xa7', u'\xe1', u'\xa3', u'\xb1', u'\u0130']):
                        if spellchecker.spell(t) == False: # if spelling is wrong
                            # create a list of suggestions, keep suggestions with umlauts only
                            suggest = [su for su in spellchecker.suggest(t) if any(um in su for um in ["\xe4", "\xf6", "\xfc", "\xdf", "\xc4", "\xd6", "\xdc"])] 
                            if (bool(not suggest) == False): # if list is not empty
                                # take the first suggestion and change encoding to unicode:
                                t = suggest[0].decode(enc).encode('utf-8').decode('utf-8')
                                
                            # if the list with suggestions is empty, the token is not in the upper case, and the token contains
                            # 'AE', 'OE', or 'UE', a spellchecker does not know the word.
                            # Therefore, replace umlauts in these tokens manually.
                            elif (t.isupper() == False) and (any(urepl in t for urepl in [u'AE', u'OE', u'UE'])):
                                # I have spotted a few misspelled words containing u'AE', u'OE', or u'UE'.
                                # Either a spellchecker does not know these words, or the misspelling does not concern umlauts.
                                # Fix these words manually.
                                if t in self.misspellings:
                                    for k,v in self.misspellings.iteritems():
                                        t = t.replace(k,v)
                                        
                                # Now we replace u'AE', u'OE', and u'UE' with corresponding umlauts
                                # taking into account a few exceptions:
                                if t not in [u"AEntG"]:
                                        t = t.replace(u"AE", u"Ä")
                                        
                                if ((not ("OECD" in t)) & (t not in [u"OEMs"])):
                                    t = t.replace(u"OE", u"Ö")
                                    
                                t = t.replace(u"UE", u"Ü")
                                
                                # We fixed u'AE', u'OE', and u'UE'. However, these words might contain other umlauts as well.
                                # E.g., Überziehungszuschlägen.
                                if any(urepl in t for urepl in [u'ae', u'oe', u'ue', u'ss']):
                                    # change encoding to use a spellchecker
                                    t = t.encode(enc)
                                    # if spelling is wrong
                                    if spellchecker.spell(t) == False:
                                        # create a list of suggestions, keep suggestions with umlauts only
                                        suggest = [su for su in spellchecker.suggest(t) if (any(um in su for um in 
                                                       ["\xe4", "\xf6", "\xfc", "\xdf"]) & any(um in su for um in 
                                                       ["\xc4", "\xd6", "\xdc"]))] 
                                        # if the list is not empty
                                        if (bool(not suggest) == False):
                                            # take the first suggestion and change encoding to unicode:
                                            t = suggest[0].decode(enc).encode('utf-8').decode('utf-8')
                                        # if the list is empty
                                        else:
                                            # Try to find suggestions with "ae" and "oe" replaced with umlauts
                                            # This might help with long words containing several umlauts - 
                                            # it is difficult for a spellchecker to recognize the word
                                            # if there are several misspellings.
                                            
                                            # Keep suggestions with umlauts only.
                                            suggest = [su for su in spellchecker.suggest(t.replace("ae", "\xe4").replace("oe", "\xf6")) 
                                                            if (any(um in su for um in 
                                                                 ["\xe4", "\xf6", "\xfc", "\xdf"]) & any(um in su for um in 
                                                                   ["\xc4", "\xd6", "\xdc"]))]
                                            # If the list is not empty
                                            if (bool(not suggest) == False):
                                                # take the first suggestion and change encoding to unicode:
                                                t = suggest[0].decode(enc).encode('utf-8').decode('utf-8')
                                            else:
                                                # If a spellchecker has not recognized the word, replace 3/4 umlauts manually.
                                                # Manual inspection proved that this strategy helps to minimize the amount of misspellings.
                                                t = t.replace("ae", "\xe4")
                                                t = t.replace("oe", "\xf6")
                                                t = t.replace("ue", "\xfc")
                                                t = t.decode(enc).encode('utf-8').decode('utf-8')                                            
                                    else:
                                        t = t.decode(enc).encode('utf-8').decode('utf-8')
                            else:
                                # change encoding to use a spellchecker for words with umlauts
                                t = t.encode(enc)
                                # Try to find suggestions with "ae" and "oe" replaced with umlauts
                                suggest = [su for su in spellchecker.suggest(t.replace("ae", "\xe4").replace("oe", "\xf6")) 
                                                            if any(um in su for um in 
                                                                 ["\xe4", "\xf6", "\xfc", "\xdf"])]
                                # If the list is not empty
                                if (bool(not suggest) == False):
                                    # take the first suggestion and change encoding to unicode:
                                    t = suggest[0].decode(enc).encode('utf-8').decode('utf-8')
                                else:
                                    # If a spellchecker has not recognized the word, replace 3/4 umlauts manually.
                                    t = t.replace("ae", "\xe4")
                                    t = t.replace("oe", "\xf6")
                                    t = t.replace("ue", "\xfc")
                                    t = t.decode(enc).encode('utf-8').decode('utf-8')
                                
                tokens_new.append(t)
            self.docs = md.detokenize(tokens_new) # detokenize
            # replace '$' with ' $ '.
            self.docs = self.docs.replace('$', ' $ ')
            # replace '£' with ' £ '.
            self.docs = self.docs.replace(u"£", u' £ ')
            # replace 'Mill.' with ' Mill. '.
            self.docs = self.docs.replace(u"Mill.", u' Mill. ')
            # replace 'Mrd.' with ' Mrd. '.
            self.docs = self.docs.replace(u"Mrd.", u' Mrd. ')
            # replace "``" with ' " '.
            self.docs = self.docs.replace(u"``", u' " ')
            # replace "''" with ' " '.
            self.docs = self.docs.replace(u"''", u' " ')
            # replace "\u0130noenue" with the correct representation of the name "İnönü".
            self.docs = self.docs.replace(u"\u0130noenue", u"İnönü")
            # make sure that there are no extra white spaces
            self.docs = ' '.join(self.docs.split())
        return self.docs
       