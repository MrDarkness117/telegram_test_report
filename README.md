## Launch pytest tests using Telegram!

This project is an experimental draft for launching tests remotely using Telegram bots. 

You can use /pytest command and pass in params to launch tests with various settings.

1. Create a bot ( _t.me/BotFather_ )
2. Add bot API key to **bot.py** (or use .env and pass it through there)
3. Write some tests or whole test frameworks inside tests folder
4. Launch tests using _/pytest_ (see **handlers/commands.py**)
5. ???
6. **Profit!**
