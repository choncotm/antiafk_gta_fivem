# antiafk_gta_fivem

Small Python/Tkinter tool that keeps a GTA V / FiveM character from being kicked for inactivity.

## Problem

Some FiveM servers auto-kick players who don't produce any input for a while, which is annoying if you're AFK for a legitimate reason mid-session.

## Solution

A tiny always-on-top window with start/stop controls that simulates a periodic sequence of key presses (emote, animations) at a fixed interval, so the game keeps registering activity.

## Structure

```
.
└── antiafk_gta.py      # Tkinter GUI + anti-AFK key-press loop
```

The repo also has a committed Python virtualenv (`bin/`, `share/`, `pyvenv.cfg`) — not essential, only `antiafk_gta.py` matters.

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
