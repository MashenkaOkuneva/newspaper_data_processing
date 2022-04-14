# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 14:08:25 2021

@author: mOkuneva
"""

import re


def chained_articles(inputs_cont):
    """ 
    This function returns a list with two tuples.
    The first tuple contains two indices corresponging to the first and second
    part of a chained article. These two parts must be merged into one article.
    
    The second tuple contains two indices as well. The first index corresponds to
    a part of the chained article that is a duplicate because the merged
    version of this chained article already exists in the database. The article with
    this index must be deleted. The second index corresponds to the merged version
    of the chained article. This article must be kept in the database.
    
    An input is a tuple, where the first element is a row of the dataframe 
    corresponding to the second part of the chained article.
    The second element of the tuple is a dataframe containing all articles published
    on the same day as the second part of the chained article, i.e. all articles
    that could potentially be the first part of the chained article.
    """

    # The second part of a chained article usually contains a string like
    # 'Fortsetzung von Seite B12'. Here page_letter = 'B', page_numbers = ['12'].
    page_letter = ''
    page_numbers = []
    # An index of the second part of the chained article in the dataframe 
    # 'continued_articles'.
    ind = inputs_cont[0].index[0]
    # Use a regular expression to find the string like 'Fortsetzung von Seite B12'
    # in the second part of the chained article.
    fort_pat = re.findall(r"Fortsetzung von Seite [a-zA-Z0-9 ]+", inputs_cont[0]['texts'][ind], re.I)
    
    # The first part of the chained article typically contains a string like
    # 'Fortsetzung Seite B13'. If we know from the metadata which page
    # the second part of the chained article is published on (e.g., B13), we will
    # search for the first part using this information and the corresponding 
    # string 'Fortsetzung Seite B13'.
    # If information on the page number is not available, we will retrieve the page
    # number of the first part using fort_pat. We will assume that the second
    # part of the chained article is pusblished on the next page or the page
    # after that.
    # For example, if the second part of the article contains the string
    # 'Fortsetzung von Seite 13', we would consider articles containing either
    # 'Fortsetzung Seite 14' or 'Fortsetzung Seite 15' as the first part of the
    #  chained article.
    
    # If metadata contains information on the page number of the second part:
    if inputs_cont[0]['page'][ind] != '':
        # Save the page number of the second part
        page = inputs_cont[0]['page'][ind]
        # If 'page' is a number (e.g., 13), we will search for the 
        # first part using a string like 'Fortsetzung Seite 13'.
        if page.isdigit() == True:
            page_numbers = [str(int(page))]
        # If 'page' contains a letter and digits (e.g., B13)
        elif page.isalnum() == True:
            page_letter = page[0].upper()
            page_numbers = [str(int(page[1:]))]
            
    # If there is no page number of the second part in the metadata:
    else:
        # Search for the first part assuming that the second part is published on
        # the next page or the page after that.
        if fort_pat != []:
            # Save the page number of the first part
            page = fort_pat[0].split(' ')[3]
            # If 'page' is a number (e.g., 13), we will search for the first
            # part using strings like 'Fortsetzung Seite 14' and 'Fortsetzung Seite 15'.
            if page.isdigit() == True:
                page_numbers = [str(int(page)+1) , str(int(page)+2) ]
            # If 'page' is a letter (e.g., Fortsetzung von Seite B 13):
            elif page.isalpha() == True:
                page_letter = page
                page_numbers = [str(int(fort_pat[0].split(' ')[4])+1), str(int(fort_pat[0].split(' ')[4])+2)]
            # If 'page' is an alphanumeric (e.g., Fortsetzung von Seite B13):
            elif page.isalnum() == True:
                page_letter = page[0]
                page_numbers = [str(int(page[1:])+1), str(int(page[1:])+2)]

    # To find the first part of a chained article, we will use one of the following
    # strings:
    fort_strings = []
    for page_number in page_numbers:
        # The case where 'page' is a number. An article can not be continued
        # on the first page.
        if page.isdigit() == True and page_number != '1':
            fort_strings.append([
                        r'Fortsetzung Seite ' + page_number + r'\b',
                        r'Fortsetung Seite' + page_number + r'\b',
                        r'Fortsetzung auf Seite ' + page_number + r'\b',
                        r'Fortsetzung S\. ' + page_number + r'\b',
                        r'Fortsetzung S\.' + page_number + r'\b',
                        r'Fortsetzung Seiten ' + page_number + r'\b',
                        r'Seite ' + page_number + r'\b',
                        r'Seiten ' + page_number + r'\b',
                        r'FORTSETZUNG SEITE ' + page_number + r'\b',
                        r'FORTSETZUNG AUF SEITE ' + page_number + r'\b',
                        r'FORTSETZUNG S\. ' + page_number + r'\b',
                        r'FORTSETZUNG S\.' + page_number + r'\b',
                        r'FORTSETZUNG SEITEN ' + page_number + r'\b',
                        r'SEITE ' + page_number + r'\b',
                        r'SEITEN ' + page_number + r'\b'])
        # The case where 'page' is not a number. An article can not be continued
        # on the first page.
        elif page_number != '1':
            fort_strings.append([
                        r'Fortsetzung Seite ' + page_letter + page_number + r'\b', 
                        r'Fortsetung Seite ' + page_letter + page_number + r'\b', 
                        r'Fortsetzung Seite ' + page_letter + ' ' + page_number + r'\b',
                        r'Fortsetung Seite ' + page_letter + ' ' + page_number + r'\b', 
                        r'FORTSETZUNG SEITE ' + page_letter + page_number + r'\b',
                        r'FORTSETZUNG SEITE ' + page_letter + ' ' + page_number + r'\b',
                        r'Fortsetzung auf Seite ' + page_letter + page_number + r'\b',
                        r'Fortsetzung auf Seite ' + page_letter + ' ' + page_number + r'\b',
                        r'FORTSETZUNG AUF SEITE ' + page_letter + page_number + r'\b',
                        r'FORTSETZUNG AUF SEITE ' + page_letter + ' ' + page_number + r'\b',
                        r'Fortsetzung S\. ' + page_letter + page_number + r'\b',
                        r'Fortsetzung S\.' + page_letter + page_number + r'\b',
                        r'Fortsetzung S\. ' + page_letter + ' ' + page_number + r'\b',
                        r'Fortsetzung S\.' + page_letter + ' ' + page_number + r'\b',
                        r'FORTSETZUNG S\. ' + page_letter + page_number + r'\b',
                        r'FORTSETZUNG S\.' + page_letter + page_number + r'\b',
                        r'FORTSETZUNG S\. ' + page_letter + ' ' + page_number + r'\b',
                        r'FORTSETZUNG S\.' + page_letter + ' ' + page_number + r'\b',
                        r'Fortsetzung Seiten ' + page_letter + page_number + r'\b',
                        r'Fortsetzung Seiten ' + page_letter + ' ' + page_number + r'\b',
                        r'FORTSETZUNG SEITEN ' + page_letter + page_number + r'\b',
                        r'FORTSETZUNG SEITEN ' + page_letter + ' ' + page_number + r'\b',
                        r'Seite ' + page_letter + page_number + r'\b',
                        r'Seite ' + page_letter + ' ' + page_number + r'\b',
                        r'SEITE ' + page_letter + page_number + r'\b',
                        r'SEITE ' + page_letter + ' ' + page_number + r'\b',
                        r'Seiten ' + page_letter + page_number + r'\b',
                        r'Seiten ' + page_letter + ' ' + page_number + r'\b',
                        r'SEITEN ' + page_letter + page_number + r'\b',
                        r'SEITEN ' + page_letter + ' ' + page_number + r'\b',
                        ])
    
    # df is a data frame with the articles published on the same day as the considered
    # chained article.
    df = inputs_cont[1]
    
    
    # Try to find the first part of a chained article.
    first_part = []
    # Strings that are normally met in the second part.
    second_strings = ['Fortsetzung von Seite', 'FORTSETZUNG VON SEITE']
    
    # If metadata contains information on the page number of the second part:
    if len(fort_strings) == 1:
        # 1. The candidates for the first part do not contain any of the strings
        # from the 'second_strings' list. Articles that do include one of these strings
        # have already been merged.
        # 2. The candidates for the first part contain one of the strings from the 
        # 'fort_strings' list (like 'Fortsetzung Seite ...').
        first_part = list(df[(~df.texts.str.contains('|'.join(second_strings))) &
                     (df.texts.str.contains('|'.join(fort_strings[0])))].index)
    # If metadata does not contain information on the page number of the second part,
    # an article does not begin with 'AUSLÄNDISCHE' (these articles are merged based
    # on the beginning of the title), and
    # 'page_number' is not equal to 1 (same as len(fort_strings)!=0):    
    elif (inputs_cont[0]['texts'][ind][:12] != 'AUSLÄNDISCHE') and (len(fort_strings) != 0):
        # Again search for the first part candidates.
        # Here we assume that the second part is continued on the next page
        # or the page after that (other cases are not considered).
        first_part = list(df[(~df.texts.str.contains('|'.join(second_strings))) &
                      ((df.texts.str.contains('|'.join(fort_strings[0]))) |
                      (df.texts.str.contains('|'.join(fort_strings[1])) )
                       )].index)
    
    # It is possible that 'first_part' contains more than one article's index.
    # Therefore, we need some rules to choose the correct first part of a chained
    # article.
    
    # 1. If an article from the 'first_part' list has the same beginning as 
    # the second part of a chained article, we select this article as the correct
    # first part.  
    if len(first_part) > 1:
        for j in range(len(first_part)):                
            if df['texts'][first_part[j]][:5] == inputs_cont[0]['texts'][ind][:5]:
                first_part = [first_part[j]]
                break
            
    # 2. If the first rule does not apply, we use the second rule.
    # The second part of a chained article often begins with a sentence like
    # 'Fortsetzung von Seite B1.' The next sentence might be a title or
    # include words defining the topic of the article. 'common_word'
    # is a word that comes after 'Fortsetzung von Seite B1.'. If an article from
    # the 'first_part' includes the 'common_word', we select it as the correct
    # first part.       
    common_word = re.findall(r"(Fortsetzung von Seite [a-zA-Z0-9 ]+)([. ]+)([a-zA-Z\u00C0-\u017F]+\b)", inputs_cont[0]['texts'][ind], re.I)
    if common_word != []:
        common_word = common_word[0][-1]
    else:
        common_word = 'None'
           
    if len(first_part) > 1:
        for j in range(len(first_part)):
            if (common_word in df['texts'][first_part[j]]) and (common_word != 'None') and \
                (inputs_cont[0]['texts'][ind][:12] != 'AUSLÄNDISCHE'):
                    first_part = [first_part[j]]
                    break
                    
    # 3. In case the first two rules do not apply, we use the third rule.
    # Some of the candidates for the first part of a chained article might start
    # from the capitalized word (e.g., GELDPOLITIK). This word is a title or it
    # defines the main topic of an article. We save it as a variable 'common_word_2'.
    # If the second part of a chained article contains the 'common_word_2', then
    # the article that starts from the 'common_word_2' is the correct first part.          
    if len(first_part) > 1:
        for j in range(len(first_part)):
            # Extract the capitalized word from the first part candidate, if present.
            common_word_2 = re.findall(r"(?:^)([A-ZÄÖÜ]+\b)", df['texts'][first_part[j]])
            if common_word_2 != []:
                common_word_2 = common_word_2[0]
            else:
                common_word_2 = 'None'
            # Use rule #3 to decide on the first part article.    
            if (common_word_2.lower() in inputs_cont[0]['texts'][ind].lower()) and (common_word_2 != 'None') and \
                (inputs_cont[0]['texts'][ind][:12] != 'AUSLÄNDISCHE'):
                    first_part = [first_part[j]]
                    break
        # If after applying the first three rules, we can not pick one article,
        # do not merge the second part with any article.
        if len(first_part) > 1:
            first_part = []
    
    
    # If there is no 'Fortsetzung ...' string in the first part candidate,
    # try to find an article that has the same beginning of the title as
    # the second part of a chained article.
    
    # The artilces that start from these strings are not chained articles.
    exceptions = ['Nachrichten', 'Geldticker', 'Wirtschaft', 'Fortsetzun']
    if (first_part == []):
        for i in df.index:
            if (df['texts'][i][:15] == inputs_cont[0]['texts'][ind][:15]) and \
            (df['texts'][i][:10] not in exceptions) and \
                (fort_pat[0] not in df['texts'][i]): # The second part of a chained article we consider is part of 'df' data frame.
                    first_part = [i]
                
    # The first output is a tuple 'chained' that contains two indices corresponging 
    # to the first and second part of a chained article. 
    # These two parts must be merged into one article.
    chained = ()
    if (first_part != []):
        chained = (first_part[0], inputs_cont[0]['index'][ind])    
    
    # There are a few cases where the chained artilcles have been merged,
    # but one of the parts (the first or the second) still exists in the database
    # as a separate entry. We treat these parts of the chained articles as duplicates
    # and delete them from the data base.
    
    # We are searching for all the articles that contain:
    # 1. either the last 200 characters from the second part of the chained article,
    # 2. or 100 characters after the string 'Fortsetzung von Seite ...'  
    # from the second part of the chained article,
    # 3. or 100 characters after the first sentence in the second part of the
    # chained article.
    dup = []
    for i in df.index:
        if (inputs_cont[0]['texts'][ind][-200:].replace('.', '') in  \
            df['texts'][i].replace('.', '')) or \
            (inputs_cont[0]['texts'][ind].split(fort_pat[0], 1)[1].lstrip('. ')[:100] in \
             df['texts'][i]) or \
            (inputs_cont[0]['texts'][ind].split('.', 1)[1].lstrip(' ')[:100] in \
             df['texts'][i]):
                dup.append(i) 
    
    # If the list 'dup' contains more than one index, then there is a duplicate
    # in the data base (remember that one of the indices corresponds to the chained 
    # article we consider).      
    if len(dup)>1:
        # We assume that the shorter article from the 'dup' list is a duplicate.
        min_wc = min(df.loc[dup]['word_count'].values)
        # Extract the index of the duplicated article.
        dup_ind = df.loc[dup][df.loc[dup]['word_count'] == min_wc].index[0]
        # To check that 'dup_ind' is indeed a duplicate, we also output
        # an index of the merged article.
        non_dup = df.loc[dup][df.loc[dup]['word_count'] != min_wc].index[0]
    else:
        dup_ind = -1
        non_dup = -1
    
  
    return([chained, (dup_ind, non_dup)])

