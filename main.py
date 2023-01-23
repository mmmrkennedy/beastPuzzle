import tkinter as tk
from tkinter import PhotoImage

# Create a new Tkinter window
root = tk.Tk()
root.title("Beast From Beyond Symbols Solver")
root.iconbitmap('Beast Symbols/logo.ico')

# Create a list to store the selected buttons
selected_buttons = []

def on_button_click(button_id):
    # Add the button's ID to the list of selected buttons
    selected_buttons.append(button_id)
    # Update the window to show the selected buttons
    update_window()

def reset_program():
    global selected_buttons
    selected_buttons = []
    for i in range(12):
        button = tk.Button(root)
        button.config(state="normal")
    update_window()

def update_window():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # List to store updated Buttons
    updated_buttons = []
    duplicate = False
    # Create a grid of buttons
    for i in range(12):
        button = tk.Button(root)
        button.grid(row=i//4, column=i%4, padx=0, pady=0)
        img = PhotoImage(file=f"Beast Symbols/picture {i}.png")
        button.config(image=img)
        if len(selected_buttons) < 4:
            button.config(command=lambda id=i: on_button_click(id))
        else:
            button.config(state="disable")
        button.image = img

    # Create a label to display the selected buttons
    label = tk.Label(root)
    label.grid(row=4, column=0, columnspan=4, padx=0, pady=0)
    for i in range(len(selected_buttons)):
        updated_buttons.append(selected_buttons[i] + 1)
    label.config(text=f"Selected buttons: {updated_buttons}")

    if len(selected_buttons) == 4:
        if len(set(selected_buttons)) != 4:
            duplicate = True
        else:
            result = process_buttons(selected_buttons)
            if result:
                for j, idx in enumerate(result):
                    img = PhotoImage(file=f"Beast Symbols/picture {idx}.png")
                    label = tk.Label(root, image=img)
                    label.grid(row=5, column=j)
                    label.image = img
            else:
                label.config(text=f"Selected buttons: {updated_buttons} \n "
                                  f"Result: {result} \n "
                                  f"Invalid Sequence: Please Reset to Try Again")
        if duplicate:
            label.config(text=f"Selected buttons: {updated_buttons} \n "
                              f"Invalid Sequence: You have selected duplicate button Please Reset to Try Again")

    # Create the reset button
    reset_button = tk.Button(root, text="Reset", command=reset_program)
    reset_button.grid(row=6, column=0, columnspan=4)



def process_buttons(numbers):
    lines = [[1, 2, 3, 4, 0, 5], [6, 5, 8, 9, 7, 1], [9, 10, 7, 8, 6, 1], [9, 4, 3, 0, 5, 2], [1, 11, 3, 2, 0, 5], [4, 11, 0, 2, 5, 8]]
    for line in lines:
        if all(n in line for n in numbers):
            ordered_numbers = [x for x in line if x in numbers]
            return ordered_numbers
    return False

update_window()

# Run the Tkinter event loop
root.mainloop()
