import tkinter as tk

def generate_fibonacci():
    num = int(fibonacci_entry.get())
    fib_list = [0, 1]
    for i in range(2, num):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    fib_output.config(text=f"Fibonacci Terms: {fib_list}")

def add_element():
    element = add_entry.get()
    gui_list.append(element)
    list_output.config(text=f"List: {gui_list}")
    list_count.config(text=f"List Count: {len(gui_list)}")

def delete_element():
    element = delete_entry.get()
    if element in gui_list:
        gui_list.remove(element)
        list_output.config(text=f"List: {gui_list}")
        list_count.config(text=f"List Count: {len(gui_list)}")

def return_to_menu():
    fib_frame.pack_forget()
    list_frame.pack_forget()
    menu_frame.pack()

window = tk.Tk()
window.title("GUI EL")

gui_list = []

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

win_width = int(screen_width / 2)
win_height = int(screen_height / 2)

win_x = int((screen_width - win_width) / 2)
win_y = int((screen_height - win_height) / 2)

window.geometry(f"{win_width}x{win_height}+{win_x}+{win_y}")

menu_frame = tk.Frame(window)
menu_frame.pack()

fib_button = tk.Button(menu_frame, text="Fibonacci", command=lambda: [menu_frame.pack_forget(), fib_frame.pack()])
fib_button.pack(pady=10)

list_button = tk.Button(menu_frame, text="List Manipulation", command=lambda: [menu_frame.pack_forget(), list_frame.pack()])
list_button.pack(pady=10)

fib_frame = tk.Frame(window)

fib_label = tk.Label(fib_frame, text="Enter the number of terms:")
fib_label.pack(pady=10)

fibonacci_entry = tk.Entry(fib_frame)
fibonacci_entry.pack(pady=5)

generate_button = tk.Button(fib_frame, text="Generate", command=generate_fibonacci)
generate_button.pack(pady=10)

fib_output = tk.Label(fib_frame, text="Fibonacci Terms: ")
fib_output.pack(pady=10)

return_button = tk.Button(fib_frame, text="Return to Menu", command=return_to_menu)
return_button.pack(pady=10)

list_frame = tk.Frame(window)

add_label = tk.Label(list_frame, text="Add Element:")
add_label.pack(pady=10)

add_entry = tk.Entry(list_frame)
add_entry.pack(pady=5)

add_button = tk.Button(list_frame, text="Add", command=add_element)
add_button.pack(pady=5)

delete_label = tk.Label(list_frame, text="Delete Element:")
delete_label.pack(pady=10)

delete_entry = tk.Entry(list_frame)
delete_entry.pack(pady=5)

delete_button = tk.Button(list_frame, text="Delete", command=delete_element)
delete_button.pack(pady=5)

list_output = tk.Label(list_frame, text="My List: ")
list_output.pack(pady=10)

list_count = tk.Label(list_frame, text="List Count: ")
list_count.pack(pady=10)

return_button = tk.Button(list_frame, text="Return to Menu", command=return_to_menu)
return_button.pack(pady=10)

window.mainloop()
