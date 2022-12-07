# Builds a front-end GUI interface for the todo_functions.py back end

import todo_functions as tdf
import PySimpleGUI as sg
import time

FILEPATH = "./data/tl.txt"
def window_setup():
    sg.theme('Kayak')

    win_font_style = ("Helvetica", 15)
    task_list_box = sg.Listbox(values=tdf.get_tl(FILEPATH), key = "-lb-",
     enable_events=True, size=(50, 5))
    time_label = sg.Text("", key="clock")

    layout = [
        [sg.Titlebar(title="Simple ToDo App")],
        [time_label],
        [sg.Text('Enter a new ToDo here: '),
        sg.InputText(tooltip="Enter ToDo", key="new_task"), sg.Button("Add")],
        [task_list_box],
        [sg.Button("Edit"), sg.Button("Complete"),sg.Exit()]
    ]

    window = sg.Window(
        "This is overriden by sg.Titlebar() in the layout", layout, font=win_font_style)
    return window


def main():
    app_window = window_setup()
    while True:
        event, values = app_window.read(timeout=300)
        # print(event, values)
        app_window["clock"].update(time.strftime("%b %d %Y %H:%M:%S"))
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        match event:
            case "Add":
                tdf.gui_add(FILEPATH, values["new_task"])
                app_window["-lb-"].update(values=tdf.get_tl(FILEPATH))

            case "-lb-":
                app_window["new_task"].update(value=values["-lb-"][0])

            case "Edit":
                try:
                    tdf.gui_edit(FILEPATH, values["-lb-"][0], values["new_task"])
                    app_window["-lb-"].update(values=tdf.get_tl(FILEPATH))
                    app_window["new_task"].update(value="") #Yes, 'no value' is intended here to clear display
                except IndexError:
                    sg.popup(F"No task has been selected to {event}", line_width = 50, font=("Helvetica", 12), no_titlebar=True, grab_anywhere=True)

            case "Complete":
                try:
                    tdf.gui_complete(FILEPATH, values["-lb-"][0])
                    app_window["-lb-"].update(values=tdf.get_tl(FILEPATH))
                    app_window["new_task"].update(value="") #Yes, 'no value' is intended here to clear display
                except IndexError:
                    sg.popup(F"No task has been selected to {event}", line_width = 50, font=("Helvetica", 12), no_titlebar=True, grab_anywhere=True)
            case _:
                # sg.popup(F"You should do something about this {event}.")
                continue
    app_window.close()


if __name__ == "__main__":
    main()
