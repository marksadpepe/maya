# Introduction
Maya is a virtual assistant. Its a program aimed at supporting and counseling adolescents in the area of sexuality and interpersonal relationships. Maya offers unique advice and recommendations based on advanced sex therapy methods. It was created to provide a comfortable and safe atmosphere for discussing any issues related to sex life and relationships.

Maya is always ready to provide individualized advice, according to the needs and situation of each particular user.

# Running
1. You need to create a Telegram Bot, see the docs at https://core.telegram.org/bots/faq#how-do-i-create-a-bot. Also you will need to create an environment variable named ```BOT_TOKEN```, the value of which will be the token that Telegram itself will provide you with.
2. The next step is to create an API key on the OpenAI platform, see the docs at https://platform.openai.com/api-keys. After that you need to create an environment variable named ```MAYA_KEY``` and give it the value of the newly created API key.
```bash
export BOT_TOKEN="your_bot_token"
export MAYA_KEY="your_openai_api_key"
pip install -r requirements.txt
python3 ./app.py
python3 ./bot.py
```
The website is at http://localhost:5000