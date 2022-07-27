# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 19:25:32 2022

@author: Nutzer
"""

import re

def clean_dpa_references(text):
    """  
    This function removes all dpa references from a string
    """

    text = re.sub('''[A-ZÄÖÜß]{,50}\s\(dpa\)\s-\s|
       |[A-ZÄÖÜß]{,50}\s\(dpa/vwd\)\s-\s|[A-ZÄÖÜß]{,50}\s\(dpa/tk\)\s-\s|[A-ZÄÖÜß]{,50}\s\(dpa-AFX\)\s-\s|
       |[A-ZÄÖÜß]{,50}\s\(dpa/tk\)\s-\s|[A-ZÄÖÜß]{,50}\s\(dpa-AFX/APA\)\s-\s|[A-ZÄÖÜß]{,50}\s\(euro adhoc\)\s-\s|
       |[A-ZÄÖÜß]{,50}\s\(ots\)\s-\s|[A-ZÄÖÜß]{,50}\s\(dpa-AFX Broker\)\s-\s|
       |[A-ZÄÖÜß]{,50}\s\(AFX-CH\)\s-\s|[A-ZÄÖÜß]{,50}\s\(AFX\)\s-\s''', '', text)    
    
    return(text)