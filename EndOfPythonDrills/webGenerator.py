#credit to falsetru on stackoverflow for direction


import os
import webbrowser

html = '<html><body>Stay tuned for our amazing summer sale!</body></html>'
path = os.path.abspath('summersale.html')
url = 'file://' + path

with open(path, 'w') as f:
    f.write(html)
webbrowser.open(url)


















#import webbrowser

#url = 'http://www.python.org/'

#webbrowser.open_new_tab(url + 'doc/')

#webbrowser.open_new(url)

