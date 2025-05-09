# 🏰 Discord Tavern Bot

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Discord.py](https://img.shields.io/badge/discord.py-2.x-blueviolet?logo=discord)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-WIP-yellow)

A D&D-themed Discord bot to manage The Silver Stitches' tavern economy, quests, and achievements — all with a touch of style using embedded messages and emojis.

---

## 💰 Money System

Manage your in-tavern bank with ease:

- `/bank add Xgold Ysilver Zcopper note` – Add money to the bank with an optional note section.
- `/bank remove Xgold Ysilver Zcopper note` – Remove money from the bank with an optional note section.
- `/bank clear` – Clears the entire bank.
- `/balance` – Displays current balance.
- `/expenses` – Deducts a random amount (within set range) for tavern expenses.

---

## 🧭 Quest System

Track and manage your party’s ongoing and completed quests:

- `/quest add (quest name) (description)` – Adds a quest with details.
- `/quest complete (quest name)` – Marks a quest as complete.
- `/quest list` – Shows all active and completed quests.

---

## 🏆 Achievement System

Celebrate key moments with a timestamped achievement tracker:

- `/achievement add (name) (description)` – Adds a new achievement.
- `/achievement remove (name)` – Removes an achievement (for typos or retcons).
- `/achievement list` – Lists all current achievements.

---

## 🧩 Miscellaneous

- All outputs use embedded cards and emojis for better readability.
- renamed `/icyquest` and other sub-commands to `/quest` for simplicity.
- Merged `/questlist` and `/questlist_completed` into `/quest list`.

---

## 🛠️ Work in Progress (WIP)

- `/quest clear active` – Clear all active quests.
- `/quest clear completed` – Clear all completed quests.
- `/quest edit (old name) (new name) (new description (optional))` – Edit existing quests.
- Hosting online – Researched, not yet implemented.
- Confirmation buttons for all clear commands (quests and bank).
