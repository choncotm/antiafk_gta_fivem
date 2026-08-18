# antiafk_gta_fivem

Small Python/Tkinter tool that keeps a GTA V / FiveM character from being kicked for inactivity. It simulates a periodic sequence of key presses (emote, animations) at a fixed interval while running.

## Usage

```sh
python antiafk_gta.py
```

A small window opens with three buttons:

- **start** — begin the anti-AFK loop
- **stop** — stop it
- **launch_fivem** — shortcut to launch FiveM (path is hardcoded, edit `launch_fivem()` in the script to match your install)

## Requirements

- `pyautogui`
- `pynput`
- `python-xlib`
- `tkinter`

## Note

For personal/offline use — check the terms of service of any server you connect to before using automation tools.
