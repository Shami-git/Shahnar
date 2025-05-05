# D&D Discord Bot Documentation

A custom Discord bot designed to manage in-game resources and quest tracking for The Silver Stitches.

---

## 📦 Features

### 💰 Money-Related Commands

1. **`/bank add Xgold Ysilver Zcopper`**  
   Adds the specified amount to the tavern's bank reserve. Automatically calculates and displays the new total.

2. **`/bank remove Xgold Ysilver Zcopper`**  
   Removes the specified amount from the bank reserve. Automatically calculates and displays the new total.

3. **`/balance`**  
   Displays the current balance of gold, silver, and copper in the bank.

4. **`/bank_clear`**  
   Clears all money from the bank reserve. *Confirmation prompt planned.*

5. **`/expenses`**  
   Randomly deducts a variable amount of gold, silver, and copper to simulate tavern expenses. The range can be configured.

---

### 📜 Quest-Related Commands

1. **`/icyquest add (questname) (description)`**  
   Adds a new quest to the quest log with the given name and description.

2. **`/icyquest complete (questname)`**  
   Marks the specified quest as completed.

3. **`/icyquestlist`**  
   Displays a list of all active quests.

4. **`/icyquestlist_completed`**  
   Displays a list of completed quests.

5. **`/icyquest_edit (questname) (new quest name) (new description)`** *(optional)*  
   Edits the name and/or description of a specific quest.

---

## ⚙️ Work In Progress (WIP) / Future Improvements

1. **`/icyquest_clear_active`**  
   Clears all active quests. *Confirmation prompt planned.*

2. **`/icyquest_clear_completed`**  
   Clears all completed quests. *Confirmation prompt planned.*

3. **Hosting the Bot**  
   Initial research completed on hosting options (e.g., Replit, Railway, self-hosting). Implementation pending.

4. **Confirmation Prompts**  
   Will be added to sensitive commands like `bank_clear`, `icyquest_clear_active`, and `icyquest_clear_completed` to prevent accidental deletions.

---

