import tkinter as tk
import time

def increase_value(section, subsection):
    sections[section][subsection].set(sections[section][subsection].get() + 1)

def increase_value_directly(subsection):
    sections["endgame"][subsection].set(sections["endgame"][subsection].get() + 1)

def start_timers():
    global start_time_3, start_time_15, start_time_3_after_15, start_time_145, current_state

    start_time_3 = time.time()
    current_state = "auton"
    print_current_state()
    update_timer_3(start_time_3)

def update_timer_3(start_time_3):
    current_time = time.time() - start_time_3
    remaining_time = 3 - current_time

    if remaining_time > 0:
        timer_var_3.set(f"3s Countdown: {int(remaining_time)}s")
        root.after(1000, lambda: update_timer_3(start_time_3))  # Update every 1000 milliseconds (1 second)
    else:
        timer_var_3.set("3s Countdown: 0s")

        start_time_15 = time.time()
        current_state = "auton"
        print_current_state()
        root.after(0, lambda: update_timer_15(start_time_15))  # Start 15-second timer immediately after 3 seconds

def update_timer_15(start_time_15):
    global current_state
    current_time = time.time() - start_time_15
    remaining_time = 15 - current_time

    if remaining_time > 0:
        timer_var_15.set(f"15s Countdown: {int(remaining_time)}s")
        root.after(1000, lambda: update_timer_15(start_time_15))  # Update every 1000 milliseconds (1 second)
    else:
        timer_var_15.set("15s Countdown: 0s")

        start_time_3_after_15 = time.time()
        current_state = "teleop"
        print_current_state()
        root.after(0, lambda: update_timer_3_after_15(start_time_3_after_15))  # Start second 3-second timer immediately after 15 seconds

def update_timer_3_after_15(start_time_3_after_15):
    global current_state
    current_time = time.time() - start_time_3_after_15
    remaining_time = 3 - current_time

    if remaining_time > 0:
        timer_var_3_after_15.set(f"3s Countdown: {int(remaining_time)}s")
        root.after(1000, lambda: update_timer_3_after_15(start_time_3_after_15))  # Update every 1000 milliseconds (1 second)
    else:
        timer_var_3_after_15.set("3s Countdown: 0s")

        start_time_145 = time.time()
        current_state = "teleop"
        print_current_state()
        root.after(0, lambda: update_timer_145(start_time_145))  # Start 145-second timer immediately after second 3-second timer

def update_timer_145(start_time_145):
    global current_state
    current_time = time.time() - start_time_145
    remaining_time = 145 - current_time

    if remaining_time > 0:
        timer_var_145.set(f"145s Countdown: {int(remaining_time)}s")
        root.after(1000, lambda: update_timer_145(start_time_145))  # Update every 1000 milliseconds (1 second)

        # Set current_state to "endgame" when there are 30 seconds remaining
        if remaining_time <= 30:
            current_state = "endgame"
            print_current_state()
    else:
        timer_var_145.set("145s Countdown: 0s")

def print_current_state():
    print(f"Current State: {current_state}")
    update_buttons_visibility()

def get_current_state():
    return current_state

def update_buttons_visibility():
    if current_state == "endgame":
        btn_increase_subsec5.grid()
        btn_increase_subsec6.grid()
    else:
        btn_increase_subsec5.grid_remove()
        btn_increase_subsec6.grid_remove()

def update_values():
    

# Create main window
root = tk.Tk()
root.title("Tkinter UI")

# Define sections and subsections with values
sections = {
    "auton": {"subsec1": tk.IntVar(value=0), "subsec2": tk.IntVar(value=0)},
    "teleop": {"subsec3": tk.IntVar(value=0), "subsec4": tk.IntVar(value=0)},
    "endgame": {"subsec5": tk.IntVar(value=0), "subsec6": tk.IntVar(value=0)}
}

# Create labels and buttons for sections and subsections
for i, (section, subsections) in enumerate(sections.items()):
    tk.Label(root, text=section, font=("Helvetica", 14, "bold")).grid(row=i, column=0, pady=10, padx=20, sticky="w")

    for j, (subsection, value) in enumerate(subsections.items()):
        tk.Label(root, text=subsection).grid(row=i, column=j * 2 + 1, padx=10)
        tk.Label(root, textvariable=value).grid(row=i, column=j * 2 + 2, padx=10)

# Buttons to increase values directly
btn_increase_subsec5 = tk.Button(root, text="Increase Subsec5", command=lambda: increase_value_directly("subsec5"))
btn_increase_subsec6 = tk.Button(root, text="Increase Subsec6", command=lambda: increase_value_directly("subsec6"))

# Place buttons next to subsec5 and subsec6 initially hidden
btn_increase_subsec5.grid(row=3, column=1, padx=10, pady=10, sticky="w")
btn_increase_subsec6.grid(row=3, column=3, padx=10, pady=10, sticky="w")

# Timer variables
timer_var_3 = tk.StringVar()
timer_var_15 = tk.StringVar()
timer_var_3_after_15 = tk.StringVar()
timer_var_145 = tk.StringVar()

# Labels for countdown timers
tk.Label(root, textvariable=timer_var_3, font=("Helvetica", 12, "italic")).grid(row=0, column=len(sections) * 2 + 1, pady=5, padx=20, sticky="e")
tk.Label(root, textvariable=timer_var_15, font=("Helvetica", 12, "italic")).grid(row=1, column=len(sections) * 2 + 1, pady=5, padx=20, sticky="e")
tk.Label(root, textvariable=timer_var_3_after_15, font=("Helvetica", 12, "italic")).grid(row=2, column=len(sections) * 2 + 1, pady=5, padx=20, sticky="e")
tk.Label(root, textvariable=timer_var_145, font=("Helvetica", 12, "italic")).grid(row=3, column=len(sections) * 2 + 1, pady=5, padx=20, sticky="e")

# Start button to initiate timers
btn_start = tk.Button(root, text="Start Timers", command=start_timers)
btn_start.grid(row=len(sections), column=0, padx=20, pady=10, sticky="w")

# Run the Tkinter main loop
root.mainloop()