import gui

while True:
    current_state = gui.get_current_state()
    print(current_state)

    # Check if the Tkinter window is closed
    if current_state is None:
        break

    # Manually update Tkinter window
    gui.root.update()