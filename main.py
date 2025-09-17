# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 22:25:53 2025

This script contain free advance query for LinkedIn Lead Generation

See how to scrape result in the second chapiter

@author: harivonyratefiarison
"""

from script.google_search import get_search_results
from pprint import pprint

"""
    I - SAMPLE QUERY
"""

### 1 - Search By Role (Head of Data, CEO, Manager, etc.)
query_role = 'site:linkedin.com/in intitle:("Head of Data" or "CTO")'

### 2 - Generate Leads by Sector or Industry
query_sector = 'site:linkedin.com/in intext:("FinTech" OR "Telecommunications")'

### 3 - Searching Lead by Country (France, Canada, Etc) :
query_country = 'site:linkedin.com/in ("CEO") ("Espagne" OR "France")'

### 4 - Searching LinkedIn Startups Leads
query_startup = 'site:linkedin.com/in ("Founder" OR "Co-Founder") "Startup" "Madagascar"'

### 5 - Generate lead and exclude noise (recruteur, hiring, talent, etc)
query_filtred = 'site:linkedin.com/in ("CEO" OR "CMO" OR "CTO") -recruiter -hiring -talent -intitle:jobs'

### 6 - Generate Experienced Profile Lead (Senior Level) :
query_experienced = 'site:linkedin.com/in ("Senior" OR "VP" OR "Vice President" OR "Executive Director" OR "Head of") "Marketing"'

### 7 - Search by Company Size (Startup, SME, Enterprise, Fortune 500)
query_startup = 'site:linkedin.com/in "HR Manager" "Fortune 500"'

### 8 - Search by Education or Alumni (Graduates from Harvard, HEC, MIT, etc.)
query_alumni = 'site:linkedin.com/in "MBA" "HEC Paris" "CEO"'

### 9 - Search by Keywords in Bio or Posts (e.g., “AI Enthusiast”, “SaaS Expert”)
query_bio = 'site:linkedin.com/in "SaaS" "Growth Hacking"'

### 10 - Combining Search Technique : role, industries, country, recruteur exclusion :
query_combined = 'site:linkedin.com/in ("Marketing Director" OR "Head of Marketing") "SaaS" "Germany" -recruiter -jobs'


"""
    II - TESTING 
"""
# pick a query and run the lead profile scraping
response = get_search_results(key_word=query_combined)
pprint(response)
