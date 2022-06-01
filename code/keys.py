from typing import Set

from talon import Module, Context, actions, app
import sys

alphabet = "air bat cap drum each fine gust harp ice judge crunch look made near oink pit quench red sun trap urge vest whale plex yank zip".split(
    " "
)
letters_string = "abcdefghijklmnopqrstuvwxyz"

ctx = Context()

alphabet = dict(zip(alphabet, letters_string))
ctx.lists["self.letter"] = alphabet

modifier_keys = {
    "alt": "alt",
    "alter": "alt",
    "control": "ctrl",
    "troll": "ctrl",
    "shift": "shift",
    "big": "shift",
    "super": "super",
    "command": "cmd",
    "option": "alt",
}

ctx.lists["self.modifier_key"] = modifier_keys

