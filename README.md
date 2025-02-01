---

## Telegram Forward Bot

This is a simple Telegram bot built using the **Pyrogram** library. The bot forwards messages from users or groups to a specified channel, excluding messages sent by the bot itself or from other channels.

### Features:
- Automatically forwards messages to a predefined channel.
- Ignores the messages you've sent
- Easy to set up

### How to Use:
1. Clone the repository.
2. ** If you have a UNIX system,you should create a venv for python
```bash
python -m venv myvenv
source myvenv/bin/activate
```
3. Install the required dependencies:
   ```bash
   pip install pyrogram
   pip install tgcrypto
   ```
4. Replace `"Your Id"` and `"Your api hash"` with your Telegram API credentials in the script.
5. Set the target channel ID in the `chanel` variable.
6. Run the bot:
   ```bash
   python main.py
   ```

### Requirements:
- Python 3.6 or higher.
- A Telegram API ID and hash from [my.telegram.org](https://my.telegram.org).

---
