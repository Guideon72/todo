
def get_tl(filepath):
    """
    Returns a list based on the contents
     of the file located in filepath
     """
    with open(filepath, "r") as tl:
        tl = tl.readlines()
        return tl


def write_tl(filepath, input):
    """
    Writes input back into 
    the file located in filepath
    """
    with open(filepath, "w") as tl:
        tl.writelines(input)


def add_task(app_filepath, choice):
    """Takes user choice and adds that task
     to the file located in app_filepath"""
    nTask = choice[4::]
    tasks = get_tl(app_filepath)
# BUG: Does not allow proper names
    tasks.append(nTask.capitalize() + "\n")
    write_tl(app_filepath, tasks)

#__________custom add function to support PySimpleGUI UI__________
def gui_add(app_filepath, choice):
    """Takes user choice and adds that task
     to the file located in app_filepath"""
    nTask = choice
    tasks = get_tl(app_filepath)
# BUG: Does not allow proper names
    tasks.append(nTask.capitalize() + "\n")
    write_tl(app_filepath, tasks)

def show_tasks(app_filepath):
    """Displays the current contents of the file in app_filepath,
     including index numbers for user to select"""
    with open(app_filepath, "r") as tl:
        for i, t in enumerate(tl, 1):
            t = t.strip('\n')
            print(f"{i}: {t}")


def edit_task(app_filepath, choice):
    """Allows user to edit the file in app_filepath,
     based on index provided by show_tasks"""
    tasks = get_tl(app_filepath)
    eTask = choice[5::]
    for item in enumerate(tasks, 1):
        if item[0] == int(eTask):
            # BUG: Does not allow proper names
            ntask = input(
                F"What would you like to change {item[1]} to? ").capitalize()
            tasks[item[0]-1] = ntask + "\n"
            write_tl(app_filepath, tasks)

#__________Custom edit function to support PySimpleGUI UI__________
def gui_edit(app_filepath, eTask, nTask):
    """Allows user to edit the file in app_filepath,
     based on eTask and nTask supplied by the calling UI"""
    tasks = get_tl(app_filepath)
    for item in tasks:
        if item == eTask:
            idx = tasks.index(item)
            tasks[idx] = nTask+'\n'.capitalize()
    write_tl(app_filepath, tasks)

def complete_task(app_filepath, choice):
    """Allows user to complete and remove a task 
    from the file in app_filepath, 
    based on index provided by show_tasks
    """
    tasks = get_tl(app_filepath)
    cTask = int(choice[9::])
    completed = tasks.pop(cTask - 1).strip("\n")
    print(F"'{completed}' is done.")
    write_tl(app_filepath, tasks)

#__________Custom complete function to support PySimpleGUI UI__________
def gui_complete(app_filepath, cTask):
    """Allows user to complete and remove a task 
    from the file in app_filepath, 
    based on index provided by show_tasks
    """
    tasks = get_tl(app_filepath)
    idx = tasks.index(cTask)
    print(F"In gui_complete; {idx}")
    completed = tasks.pop(idx).strip("\n")
    print(F"'{completed}' is done.")
    write_tl(app_filepath, tasks)

# if __name__ == '__main__':
#     main()
