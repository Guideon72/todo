# Builds a front-end GUI interface for the todo_functions.py back end

import todo_functions
import PySimpleGUI as sg


def window_setup():
    sg.theme('DarkAmber')

    layout = [[sg.Titlebar(title="Custom Titlebar for ToDo App")],
              [sg.Text('Tracking our ToDo list since 2022!', justification='r')],
              [sg.Text('Enter a new ToDo here: '),
               sg.InputText(tooltip="Enter ToDo"), sg.Button("Add")],
              [sg.Listbox(values="Stuff will go here")],
              [sg.Cancel()]]

    window = sg.Window(
        "This is overriden by sg.Titlebar() in the layout", layout)
    return window


def main():
    while True:
        app_window = window_setup()
        event, values = app_window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break


if __name__ == "__main__":
    main()
