import json
import os

FILE_NAME = "prompts.json"


def load_prompts():
    """Load prompts from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_prompts(prompts):
    """Save prompts to the JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(prompts, file, indent=4)


def add_prompt():
    """Add a new prompt to a category."""
    prompts = load_prompts()

    category = input("Enter category (e.g. marketing, church, business, saas): ").strip()
    title = input("Enter prompt title: ").strip()
    content = input("Enter prompt content: ").strip()

    if category not in prompts:
        prompts[category] = []

    prompts[category].append({
        "title": title,
        "content": content
    })

    save_prompts(prompts)
    print(f"\nPrompt '{title}' added successfully under '{category}'.\n")


def view_prompts():
    """Display all prompts by category."""
    prompts = load_prompts()

    if not prompts:
        print("\nNo prompts found.\n")
        return

    print("\nSaved Prompts:\n")
    for category, items in prompts.items():
        print(f"Category: {category}")
        for index, prompt in enumerate(items, start=1):
            print(f"  {index}. {prompt['title']}")
            print(f"     {prompt['content']}")
        print()


def search_prompts():
    """Search prompts by keyword."""
    prompts = load_prompts()
    keyword = input("Enter keyword to search: ").strip().lower()

    found = False
    print("\nSearch Results:\n")
    for category, items in prompts.items():
        for prompt in items:
            if keyword in prompt["title"].lower() or keyword in prompt["content"].lower():
                print(f"Category: {category}")
                print(f"Title: {prompt['title']}")
                print(f"Content: {prompt['content']}\n")
                found = True

    if not found:
        print("No matching prompts found.\n")


def main():
    """Main menu."""
    while True:
        print("AI Prompt Organizer")
        print("1. Add Prompt")
        print("2. View Prompts")
        print("3. Search Prompts")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            view_prompts()
        elif choice == "3":
            search_prompts()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()
