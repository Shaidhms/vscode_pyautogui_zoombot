#  Zoom Meeting – Auto-Join & Greet

A simple yet powerful Python automation bot to **join Zoom meetings**, mute your microphone, turn off your video, open group chat, and send a greeting message — all hands-free!  
Perfect for daily meetings, automation projects, and quick demos.

***

**✨ Features**

- **Auto-Join Meeting:** Open any Zoom link and bring Zoom to the foreground.
- **Mute & Stop Video:** Instantly mutes your mic and turns off your camera.
- **Greet the Group:** Opens the Zoom group chat and posts your custom greeting message.
- **Cross-Platform:** Works on **macOS** and **Windows**.
- **Keyboard-First:** Relies on reliable native shortcuts, not fragile image-only automation.
- **Customizable with Image Fallbacks:** You can add your own button screenshots for custom Zoom layouts or pre-join screens.
- **Fail-safe:** Move your mouse to any screen corner to immediately abort (PyAutoGUI failsafe enabled).

***

**📋 Requirements**

- Python 3.7 or newer
- Install dependencies:  
  `pip install pyautogui pyperclip pillow`

***

**🛠️ Setup**

1. **Clone this repo:**
    - `git clone https://github.com/Shaidhms/vscode_pyautogui_zoombot.git`
    - `cd vscode_pyautogui_zoombot`
2. (**Optional**) Create and activate a virtual environment:
    - `python -m venv venv`
    - `source venv/bin/activate`      (macOS/Linux)
    - `venv\Scripts\activate`         (Windows)
3. **Install the required Python packages:**
    - `pip install pyautogui pyperclip pillow`

***

**🚦 Usage**

- Run from your command line or VS Code terminal:
    - `python ZoomMeetingBot.py --url "YOUR_ZOOM_LINK" --greet "Hi everyone 👋"`

**Options:**

| Argument  | Description                                         |
|-----------|-----------------------------------------------------|
| `--url`   | (Required) Your Zoom meeting link                   |
| `--greet` | (Optional) Chat greeting message                    |
| `--wait`  | (Optional) Seconds to wait before starting (default: 6) |

***

**🖼️ Custom Zoom Layout?**

- If you get a pre-join screen (e.g. "Join with Computer Audio") that's different from the default:
    - Take a screenshot of the button
    - Save it in your project folder
    - Update the filename in the `click_image` line inside `ZoomMeetingBot.py` to enable image detection

***

**🎯 Example**

- `python ZoomMeetingBot.py --url "https://us02web.zoom.us/j/1234567890" --greet "Salaam! Meeting Bot joined 👋"`

***

**🛑 Security and Safety**

- This script controls your mouse & keyboard. Always keep FAILSAFE enabled (move your mouse to any screen corner to instantly abort).
- Only run automations from trusted sources.

***

 Roadmap

- After joining, wait 2 minutes, take a screenshot, and auto-send it to the community WhatsApp group with a “Meeting started” message
- Join by Meeting ID + Passcode (no URL)
- Configurable presets for different greetings (stand-up, late notice, etc.)
- Simple tray app with Start/Stop button


***

**📃 License**

MIT License

***

Credits

Built by Shaid with a daily learning sprint mindset. If you try this in your team’s stand-up, share your results and ideas for improvements.

*Happy Zooming! For further tips or troubleshooting, check the script comments or open an issue on the repo.*
