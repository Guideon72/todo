#!/venv/Scripts/python
"""A basic ToDo list application written in Python 3.10"""

import todo_functions as tdf
import time


def main():
    """Allows user to create, update
    and maintain a simple task list
    """
    while True:
        print(time.strftime("%c"))
        uAction = (
            input('"Add", "See", "Edit", "Complete"? ("Exit" to quit) ').strip().lower()
        )

        if uAction.startswith("exit") or uAction.startswith("quit"):
            break

            # TODO: Add Enchant spell-checker functionality
        elif uAction.startswith("add"):
            tdf.add_task("./data/tl.txt", uAction)

        elif uAction.startswith("show"):
            tdf.show_tasks("./data/tl.txt")

        elif uAction.startswith("edit"):
            try:
                tdf.edit_task("./data/tl.txt", uAction)
            except ValueError:
                print("Please enter a valid task ID")
                continue

        elif uAction.startswith("complete"):
            try:
                tdf.complete_task("./data/tl.txt", uAction)
            except ValueError:
                print("Please enter a valid task ID")
                continue
            except IndexError:
                print("That task ID does not exist, please try again.")

        else:
            print(" That is an Invalid Entry")


if __name__ == "__main__":
    main()
