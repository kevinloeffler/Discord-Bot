# Quick Start

### Discord
1. Download Discord:
https://discord.com/download
2. Become a Discord Developer:
https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications
3. In the Dev Portal create an Application and a Bot. You will need the API Key later.
4. Setup a Test Server (Guild).

### Create Virtual Environment (venv)
This step is not necessary but recommended. If you don't know hot set a Virtual Environment up, this article should help you:\n
https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/

### Install Python Packages
You need to install two Python Packages:
1.  pip install discord.py\n
    conda install -c cjmartian discord.py

2.  pip install python-dotenv\n
    conda install -c conda-forge python-dotenv

For the async library to work you need at least Python 3.7

### Add Enviorenment Variables
1. create .env file with:\n
DISCORD_TOKEN="TokenHere"  <- From Developer Portal\n
GUILD_NAME="YourDevServer"  <- Name of your Test Server\n

## Security
Make sure to keep the API Key secure. Use a .gitignore file to exclude your .env file from commits and do not use the Key anywhere in the code.
