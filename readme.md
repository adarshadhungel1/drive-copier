# GOOGLE DRIVE COPIER

This is a simple python app that can copy files and folder from your drive or publiv link to your personal or team drive.
This code is extracted from [python-aria-mirror-bot](https://github.com/lzzy12/python-aria-mirror-bot).

## Installation

### Requirements
- Python3 installed

### Clone the repo and install required modules
```
git clone https://github.com/adarshadhungel/drive-copier.git
cd drive-copier
pip install -r requirements.txt
``` 
### Getting Credentials.json for authenicating to drive
- Visit the [Google Cloud Console](https://console.developers.google.com/apis/credentials)
- Go to the OAuth Consent tab, fill it, and save.
- Go to the Credentials tab and click Create Credentials -> OAuth Client ID
- Choose Other and Create.
- Use the download button to download your credentials.
- Move that file to the root of drive-copier, and rename it to credentials.json
- Visit [Google API page](https://console.developers.google.com/apis/library)
- Search for Drive and enable it if it is disabled
- Finally generate token file
```
python3 generate_drive_token.py
```

### Configuring the destination path
- Open file helper.py
- On line 23 set up parent_id with folder id of destination folder like
```
parent_id = "1ndsjbfdbjh3332" 
```
- Folder id is the string after https://drive.google.com/drive/folders/ in the drive link.
- This is the folder where the copied files are stored.
- Set the value for line 24 to **True** or **False** for your case. Do not put quotation mark around these values

### Running the code
Just type
```
python3 copier.py <drive link>
```
It will copy the content of the link to parent_id provided above and gives the link of the copy in output
