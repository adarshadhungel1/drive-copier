import sys
from helper import GoogleDriveHelper

def cloneNode(link):
    if 'https://drive.google.com/' in link:
        print(f"Cloning: {link}")
        gd = GoogleDriveHelper()
        result = gd.clone(link)
        print(result)
    else:
        print("Provide G-Drive Shareable Link to Clone.")

cloneNode(sys.argv[1])