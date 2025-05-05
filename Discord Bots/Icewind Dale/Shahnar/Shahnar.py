import discord
from discord.ext import commands
from discord import app_commands
import random
import json
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree

BANK_FILE = "bank.json"
QUEST_FILE = "quests.json"

def load_bank():
    if os.path.exists(BANK_FILE):
        with open(BANK_FILE, "r") as f:
            return json.load(f).get("copper", 0)
    return 0

def save_bank(copper):
    with open(BANK_FILE, "w") as f:
        json.dump({"copper": copper}, f)

def load_quests():
    if os.path.exists(QUEST_FILE):
        with open(QUEST_FILE, "r") as f:
            return json.load(f)
    return {"active": {}, "completed": {}}

def save_quests(data):
    with open(QUEST_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Load initial data
bank_copper = load_bank()
quests = load_quests()

def format_currency(copper: int) -> str:
    gold = copper // 1000
    silver = (copper % 1000) // 100
    copper = copper % 100
    return f"{gold} gold, {silver} silver, {copper} copper"

# Bank commands
@tree.command(name="bank", description="Add or remove money from the tavern bank")
@app_commands.describe(
    action="Choose to add or remove money",
    gold="Gold amount",
    silver="Silver amount",
    copper="Copper amount"
)
@app_commands.choices(action=[
    app_commands.Choice(name="add", value="add"),
    app_commands.Choice(name="remove", value="remove")
])
async def bank_command(interaction: discord.Interaction, action: app_commands.Choice[str], gold: int = 0, silver: int = 0, copper: int = 0):
    global bank_copper
    total_copper = gold * 1000 + silver * 100 + copper

    if action.value == "add":
        bank_copper += total_copper
        save_bank(bank_copper)
        await interaction.response.send_message(
            f"Added {format_currency(total_copper)}.\nTotal: {format_currency(bank_copper)}")
    elif action.value == "remove":
        if total_copper > bank_copper:
            await interaction.response.send_message("Not enough funds!")
        else:
            bank_copper -= total_copper
            save_bank(bank_copper)
            await interaction.response.send_message(
                f"Removed {format_currency(total_copper)}.\nTotal: {format_currency(bank_copper)}")

@tree.command(name="expenses", description="Deduct random tavern expenses")
async def expenses(interaction: discord.Interaction):
    global bank_copper
    random_copper = random.randint(100, 500)
    if random_copper > bank_copper:
        random_copper = bank_copper

    bank_copper -= random_copper
    save_bank(bank_copper)
    await interaction.response.send_message(
        f"Tavern expenses deducted {format_currency(random_copper)}.\nRemaining: {format_currency(bank_copper)}")

@tree.command(name="balance", description="Show current tavern balance")
async def balance(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Tavern bank balance: {format_currency(bank_copper)}")

# New bank clear command
@tree.command(name="bank_clear", description="Clear all money in the bank")
async def bank_clear(interaction: discord.Interaction):
    global bank_copper
    bank_copper = 0
    save_bank(bank_copper)  # Save the cleared balance
    await interaction.response.send_message("All money in the bank has been cleared.")
    
# Quest commands
@tree.command(name="icyquest", description="Add or complete a quest")
@app_commands.describe(
    action="Add or complete",
    questname="Name of the quest",
    description="Optional description (required for add)"
)
@app_commands.choices(action=[
    app_commands.Choice(name="add", value="add"),
    app_commands.Choice(name="complete", value="complete")
])
async def icyquest(interaction: discord.Interaction, action: app_commands.Choice[str], questname: str, description: str = ""):
    questname = questname.strip()
    global quests

    if action.value == "add":
        if questname in quests["active"]:
            await interaction.response.send_message("That quest already exists!")
            return
        if not description:
            await interaction.response.send_message("Please include a description.")
            return
        quests["active"][questname] = description
        save_quests(quests)
        await interaction.response.send_message(f"Added quest: **{questname}**\nDescription: {description}")

    elif action.value == "complete":
        if questname not in quests["active"]:
            await interaction.response.send_message("That quest isn't in the active list.")
            return
        desc = quests["active"].pop(questname)
        quests["completed"][questname] = desc
        save_quests(quests)
        await interaction.response.send_message(f"Marked quest **{questname}** as completed.")

@tree.command(name="icyquestlist", description="List all active quests")
async def icyquestlist(interaction: discord.Interaction):
    if not quests["active"]:
        await interaction.response.send_message("There are no active quests.")
        return

    message = "**Active Quests:**\n"
    for name, desc in quests["active"].items():
        message += f"**{name}** — {desc}\n\n"
    await interaction.response.send_message(message)

@tree.command(name="icyquest_completed", description="List completed quests")
async def icyquest_completed(interaction: discord.Interaction):
    if not quests["completed"]:
        await interaction.response.send_message("No quests have been completed yet.")
        return

    message = "**Completed Quests:**\n"
    for name in quests["completed"]:
        message += f"**{name}**\n"
    await interaction.response.send_message(message)

@tree.command(name="icyquest_edit", description="Edit a quest's name or description")
@app_commands.describe(
    questname="Existing quest name",
    newname="New quest name (optional)",
    newdesc="New quest description (optional)"
)
async def icyquest_edit(interaction: discord.Interaction, questname: str, newname: str = "", newdesc: str = ""):
    global quests

    if questname not in quests["active"]:
        await interaction.response.send_message("That quest isn't in the active list.")
        return

    updated_name = newname.strip() if newname.strip() else questname
    updated_desc = newdesc.strip() if newdesc.strip() else quests["active"][questname]

    if updated_name != questname:
        quests["active"].pop(questname)
    quests["active"][updated_name] = updated_desc

    save_quests(quests)

    await interaction.response.send_message(
        f"Updated quest.\nName: **{updated_name}**\nDescription: {updated_desc}"
    )

# @tree.command(name="icyquest_clear_active", description="Clear all active quests")
# async def icyquest_clear_active(interaction: discord.Interaction):
#     global quests
#     save_quests["active"] = {}
#     save_quests(quests)
#     await interaction.response.send_message("All active quests have been cleared.")

# @tree.command(name="icyquest_clear_completed", description="Clear all completed quests")
# async def icyquest_clear_completed(interaction: discord.Interaction):
#     global quests
#     save_quests["completed"] = {}
#     save_quests(quests)
#     await interaction.response.send_message("All completed quests have been cleared.")


@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot is online as {bot.user}!")

bot.run("MTM2ODY5NjQyMzg1MTIzMzMwMA.Gj9u59.x4QhHfwYlcq5k65Ygdcr5VTOy9HoOV_wJ121ZY")  # Replace with your actual bot token