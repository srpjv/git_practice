# import HTMLSession from requests_html
from requests_html import HTMLSession
from IPython.core import ultratb
import sys
sys.excepthook = ultratb.FormattedTB(mode='Verbose', color_scheme='NoColor', call_pdb=False)
import urllib
import json



# request url
urlreq = 'https://airtable.com/shrRXLXmGwGPdOaLF/tblWjJI9H9EXyLPPF?backgroundColor=pink&layout=card&viewControls=on'
# get response
response = urllib.request.urlopen(urlreq)
# load as json
jresponse = json.load(response)

print(jresponse)

# write to file as pretty print

#with open('asdaresp.json', 'w') as outfile:
        #json.dump(jresponse, outfile, sort_keys=True, indent=4)
        #print(asdaresp.json)


