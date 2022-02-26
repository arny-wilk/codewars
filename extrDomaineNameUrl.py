# Python code to find the URL from an input string
# Using the regular expression

import re

def domain_name(url):
    
    regexp_url = r'^(https?://|[a-zA-Z0-9-]+\.)([a-zA-Z0-9-]+)\.([a-zA-Z0-9-]+).*$'
    
    string = re.search(regexp_url, url)
    
    if string :
        plain = string.group(0)
        protocol = string.group(1)
        domain = plain.replace(protocol, '')
        
        pattern = ''.join(domain.split('.')[0].split('/')[0])
        domain_name = pattern
        return domain_name
        
        
        

# Driver Code

print(domain_name('https://mail.google.com/mail/ca/u/0/#inbox'))
print(domain_name('http://google.com'))
print(domain_name('http://google.co.jp'))
print(domain_name('www.xakep.ru'))
print(domain_name('https://youtube.com'))
