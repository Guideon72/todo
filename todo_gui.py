# Builds a front-end GUI interface for the todo_functions.py back end

import todo_functions as tdf
import PySimpleGUI as sg

FILEPATH = "./data/tl.txt"
def window_setup():
    sg.theme('DarkAmber')

    win_font_style = ("Helvetica", 15)
    task_list_box = sg.Listbox(values=tdf.get_tl(FILEPATH), key = "-lb-",
     enable_events=True, size=(50, 5))

    layout = [[sg.Titlebar(title="Simple ToDo App")],
              [sg.Push(), sg.Text('Tracking our ToDo list since 2022!'), sg.Push()],
              [sg.Text('Enter a new ToDo here: '),
               sg.InputText(tooltip="Enter ToDo", key="new_task"), sg.Button("Add")],
              [task_list_box],
              [sg.Button("Edit"), sg.Button("Complete"),sg.Exit()]]

    window = sg.Window(
        "This is overriden by sg.Titlebar() in the layout", layout, font=win_font_style)
    return window


def main():
    app_window = window_setup()
    while True:
        event, values = app_window.read()
        # print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        match event:
            case "Add":
                tdf.gui_add(FILEPATH, values["new_task"])
                app_window["-lb-"].update(values=tdf.get_tl(FILEPATH))
            case "-lb-":
                app_window["new_task"].update(value=values["-lb-"][0])
            case "Edit":
                tdf.gui_edit(FILEPATH, values["-lb-"][0], values["new_task"])
                app_window["-lb-"].update(values=tdf.get_tl(FILEPATH))
            case "Complete":
                tdf.gui_complete(FILEPATH, values["-lb-"][0])
                app_window["-lb-"].update(values=tdf.get_tl(FILEPATH))
            case _:
                pass
    app_window.close()


if __name__ == "__main__":
    main()
