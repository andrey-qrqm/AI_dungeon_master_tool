<h2> Welcome to AI Dungeon Master Tool </h2>
<body>
The Tool build to assist your DM and players with answering your questions about D&D 5e in real
time and help with world generation. And let your adventure begin!

This Application is run as Discord Bot, so you don't need to download any new software during your campaign.

Behind the scenes is the custom version of the Meta llama3.2:1B model.

Link to access Discord Bot: <a href="https://discord.com/oauth2/authorize?client_id=1342138027723456654&permissions=75776&integration_type=0&scope=bot"> Click here </a>  


INSTRUCTIONS TO RUN BY YOURSELF:

The whole project can be launched with  “docker-compose up  --build -d” command. However, it must be said that in order to launch it locally users are required to create and set their own discord bot application here: https://discord.com/developers/applications/. Then it is required to create a .env file in the root directory of the project with the structure:


TOKEN_DISCORD_BOT="YOUR DISCORD TOKEN"

API_URL="YOUR BACKEND API URL"


Then the DM Assistant will be launched on your local machine.


INSTRUCTIONS TO LAUNCH JUST THE MODEL:

Download the Modelfile.md from the GitHub repository and do these commands:

ollama serve 

ollama create custom_m -f /root/Modelfile.md

ollama run custom_m


</body>