import requests
from bs4 import BeautifulSoup
import bcolors
import sys, argparse
from urllib.parse import urlparse

def banner():
    print("""

            
░██╗░░░░░░░██╗██████╗░░░░░░░██╗███╗░░██╗███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
░██║░░██╗░░██║██╔══██╗░░░░░░██║████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
░╚██╗████╗██╔╝██████╔╝█████╗██║██╔██╗██║█████╗░░██║░░██║██████╔╝██╔████╔██║███████║░░░██║░░░██║██║░░██║██╔██╗██║
░░████╔═████║░██╔═══╝░╚════╝██║██║╚████║██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══██║░░░██║░░░██║██║░░██║██║╚████║
░░╚██╔╝░╚██╔╝░██║░░░░░░░░░░░██║██║░╚███║██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
░░░╚═╝░░░╚═╝░░╚═╝░░░░░░░░░░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
                                                                                                     Code by NG          
          """)

if len(sys.argv) > 1:
        banner()
        if (sys.argv[1] == '-u'):
            try:
                input_url = sys.argv[2]
                input_code = requests.get(input_url)

                parser = argparse.ArgumentParser()
                parser.add_argument("-u", required=True)
                args = parser.parse_args()
                soup = BeautifulSoup(input_code.text, 'html.parser')
                title = soup.find_all('link', attrs={"media": "all"})
                try:
                    print(bcolors.OKMSG + 'Word Press application Version')
                    input_find = soup.find(attrs={"name": "generator"})
                    print(bcolors.OKMSG + input_find['content'] + '\n')
                except:
                    print('\n' + 'Version Not disclosed' + '\n')
                    print('***************************************************************')

                try:
                 i = 0
                 print(bcolors.OKMSG + 'Available Plugings')
                 while (i < len(title)):
                    i += 1
                    updated_input_url = input_url + '/wp-content/plugins/'

                    if updated_input_url in title[i].get('href'):
                        plug = urlparse(title[i].get('href'))
                        plugin_name=[m.split("/") for m in plug]
                        print(plugin_name[2][3])
                except:
                    print('\n' + 'Not able to find more Plugins, Most of them covered' + '\n')
                    print('***************************************************************')
                try:
                    themses_link = soup.find_all('link')
                    themes_url = input_url + '/wp-content/themes/'
                    j = 0
                    print(bcolors.OKMSG + 'Available Themes')
                    while (i < len(themses_link)):
                        j += 1
                        updated_input_url = input_url + '/wp-content/plugins/'
                        themses_link = soup.find_all('link')
                        if themes_url in themses_link[j].get('href'):
                            theses_path = urlparse(themses_link[j].get('href'))
                            plugin_name=[m.split("/") for m in plug]
                            print(plugin_name[2][3])
                except:
                            print('\n' + 'Not able to find more Themes, Most of them covered' + '\n')
                            print('***************************************************************')
            except:
                print(bcolors.ERRMSG + 'Please enter python wpplugins.py -u <valid URL with https://> ')

        elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
            print(bcolors.BOLD + 'usage: wpplugins.py [-h] -u URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                                 'show this help message and exit' '\n''-u URL of wordpress website on which you want to gather information,   --url URL')
else:
    banner()
    print(bcolors.ERR + 'Please select atleast 1 option from (-u) or -h, with a valid domain name of wordPress')


