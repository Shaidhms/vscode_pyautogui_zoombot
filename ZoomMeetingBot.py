"""
Zoom Auto-Join & Greet Bot (PyAutoGUI)
======================================

Showcase-ready automation that:
- Opens a Zoom meeting link
- Mutes mic, turns off camera
- Opens chat and sends a greeting

Tested flows for macOS and Windows using **keyboard-first shortcuts** (more reliable than image-only). Optional image fallbacks are included for pre-join screens if your Zoom skin differs.

Requirements:
  pip install pyautogui pyperclip pillow

Security note: This script controls your mouse/keyboard. Keep FAILSAFE on and move mouse to a corner to abort.
"""

import time
import platform
import webbrowser
from typing import Optional

import pyautogui as pg
import pyperclip

# -----------------------------
# Global Safety & Settings
# -----------------------------
pg.FAILSAFE = True
pg.PAUSE = 0.2  # small pause between actions

OS = platform.system().lower()  # 'darwin' for macOS, 'windows' for Windows
IS_MAC = OS == 'darwin'
IS_WIN = OS == 'windows'

# Helper to press hotkeys in a platform-agnostic way
CMD = 'command' if IS_MAC else 'ctrl'
SHIFT = 'shift'

# -----------------------------
# Image helpers (optional)
# -----------------------------

def wait_for_image(path: str, timeout: float = 20, confidence: float = 0.9):
    """Wait until an image appears on screen and return its box, else None."""
    start = time.time()
    while time.time() - start < timeout:
        try:
            box = pg.locateOnScreen(path, confidence=confidence)
        except Exception:
            box = None
        if box:
            return box
        time.sleep(0.5)
    return None


def click_image(path: str, timeout: float = 20, confidence: float = 0.9) -> bool:
    box = wait_for_image(path, timeout=timeout, confidence=confidence)
    if box:
        pg.click(pg.center(box))
        return True
    return False

# -----------------------------
# Text helper
# -----------------------------

def type_paste(text: str):
    """Paste text using clipboard to avoid layout/IME issues."""
    pyperclip.copy(text)
    pg.hotkey(CMD, 'v') if IS_MAC else pg.hotkey('ctrl', 'v')

# -----------------------------
# ZOOM BOT
# -----------------------------

def join_zoom_and_greet(meeting_url: str, greet_text: str = "Hi everyone 👋", prejoin_wait: float = 6.0):
    """Open Zoom link, ensure Zoom is front, mute, stop video, open chat, send greeting."""
    # 1) Open the meeting link (Zoom app or browser → Zoom)
    webbrowser.open(meeting_url)
    time.sleep(prejoin_wait)

    # 2) Bring Zoom to front (Spotlight/Start search is robust across setups)
    if IS_MAC:
        pg.hotkey('command', 'space'); time.sleep(0.4)
        type_paste('zoom'); time.sleep(0.4)
        pg.press('enter')
    else:
        pg.press('win'); time.sleep(0.4)
        type_paste('zoom'); time.sleep(0.6)
        pg.press('enter')
    time.sleep(3)

    # 3) (Optional) Handle common pre-join buttons via images if you supply them
    # click_image('images/zoom_join_with_computer_audio.png', timeout=8, confidence=0.85)
    # click_image('images/zoom_join_button.png', timeout=8, confidence=0.85)

    # 4) Toggle Mute & Stop Video (works once in-meeting; on some clients also on pre-join)
    if IS_MAC:
        pg.hotkey(CMD, SHIFT, 'a')  # mute/unmute
        time.sleep(0.2)
        pg.hotkey(CMD, SHIFT, 'v')  # start/stop video
    else:
        pg.hotkey('alt', 'a')
        time.sleep(0.2)
        pg.hotkey('alt', 'v')
    time.sleep(0.6)

    # 5) Open Chat
    if IS_MAC:
        pg.hotkey(CMD, SHIFT, 'h')
    else:
        pg.hotkey('alt', 'h')
    time.sleep(0.5)

    # 6) Send greeting
    type_paste(greet_text)
    time.sleep(0.2)
    pg.press('enter')


# -----------------------------
# CLI Runner
# -----------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Zoom Auto-Join & Greet Bot')
    parser.add_argument('--url', required=True, help='Zoom meeting URL (e.g., https://us02web.zoom.us/j/...)')
    parser.add_argument('--greet', default='Hi everyone 👋', help='Greeting text to send in Zoom chat')
    parser.add_argument('--wait', type=float, default=6.0, help='Seconds to wait for pre-join screens to load')
    args = parser.parse_args()

    print(f"Detected OS: {OS}; mac={IS_MAC}; win={IS_WIN}")
    print("Starting in 3 seconds. Move mouse to a corner to ABORT.")
    time.sleep(3)

    join_zoom_and_greet(args.url, args.greet, prejoin_wait=args.wait)
    print("Done.")


if __name__ == '__main__':
    main()
