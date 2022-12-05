# Builds a front-end GUI interface for the todo_functions.py back end

import todo_functions as tdf
import PySimpleGUI as sg

FILEPATH = "./data/tl.txt"
def window_setup():
    sg.theme('DarkAmber')

    win_font_style = ("Helvetica", 20)

    layout = [[sg.Titlebar(title="Simple ToDo App")],
              [sg.Push(), sg.Text('Tracking our ToDo list since 2022!'), sg.Push()],
              [sg.Text('Enter a new ToDo here: '),
               sg.InputText(tooltip="Enter ToDo", key="new_task"), sg.Button("Add")],
              [sg.Listbox(values="Stuff will go here")],
              [sg.Exit()]]

    window = sg.Window(
        "This is overriden by sg.Titlebar() in the layout", layout, font=win_font_style)
    return window


def main():
    while True:
        app_window = window_setup()
        event, values = app_window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        match event:
            case "Add":
                tdf.gui_add(FILEPATH, values["new_task"])
                # print(values["new_task"])
    app_window.close()


if __name__ == "__main__":
    main()
