##
# Brandon Pangilinan
# Due 12/10/2024
# Project 5 — Create a pizza program that creates a customized pizza and prints 
# the order on a reciept
##

#Import
from tkinter import *

# Initialize the root window
root = Tk()

# Function to handle the order submission and calculate totals
def click(size):
    """
    Handles the 'Place Order' button click.
    Updates the receipt with user selections and calculates the total cost.
    """
    size_var.set(size)  # Update the selected size

    # Get user inputs
    first_name = entry_first_name.get()  # Get first name
    last_name = entry_last_name.get()  # Get last name
    phone_number = entry_phone.get()  # Get phone number
    crust_type = crust_var.get()  # Get selected crust type
    selected_toppings = [topping for topping, var in toppings_vars.items() if var.get()]  # Get selected toppings

    # Calculate subtotal
    if size == "Small":
        size_cost = 10.99
    elif size == "Medium":
        size_cost = 12.99
    elif size == "Large":
        size_cost = 14.99
    else:
        size_cost = 12.99

    toppings_cost = len(selected_toppings) * 1.25  # Cost of additional toppings
    subtotal = size_cost + toppings_cost  # Subtotal
    tax = round(subtotal * 0.0875, 2)  # Tax (8.75%)
    total = round(subtotal + tax, 2)  # Total cost

    # Update receipt
    receipt.delete(0.0, END)  # Clear previous receipt content
    receipt.insert(END, f"Customer Name: {first_name} {last_name}\n")
    receipt.insert(END, f"Phone Number: {phone_number}\n")
    receipt.insert(END, f"Pizza Size: {size} (${size_cost:.2f})\n")
    receipt.insert(END, f"Crust Type: {crust_type}\n")
    receipt.insert(END, "Toppings:\n")
    for topping in selected_toppings:
        receipt.insert(END, f"  - {topping} ($1.25)\n")
    if not selected_toppings:
        receipt.insert(END, "  - Cheese (Included)\n")

    receipt.insert(END, "\nItemized Pricing:\n")
    receipt.insert(END, f"Pizza Size:       ${size_cost:.2f}\n")
    if selected_toppings:
        receipt.insert(END, f"Toppings:         ${toppings_cost:.2f}\n")
    receipt.insert(END, f"Subtotal:         ${subtotal:.2f}\n")
    receipt.insert(END, f"Tax:              ${tax:.2f}\n")
    receipt.insert(END, f"Total:            ${total:.2f}\n")

# Window size and title
root.geometry("1100x600")
root.title("Project 5 — Pizza Application")

# Application Title
label_Title = Label(root, text="Welcome to OCC's Pizzaria!", font=("Times New Roman", 18))
label_Title.pack(padx=20, pady=10)

# Banner Picture
banner_image = PhotoImage(file="pizza_banner.gif")  # Banner image
banner_label = Label(root, image=banner_image, bg="black")  # Add a black background for contrast
banner_label.pack(padx=20, pady=10)

# Main Frame to organize sections side by side
frame_main = Frame(root)
frame_main.pack(anchor="w", padx=10, pady=10)

# Pizza Size Section
frame_size = Frame(frame_main, relief="groove", bd=3, padx=10, pady=10, bg="#f0f0f0")  # Added outline and background
frame_size.grid(row=0, column=0, padx=10, pady=10)

# Label for size selection
label_size = Label(frame_size, text="Step 1: Enter the size:", font=("Times New Roman", 11), anchor="w", bg="#f0f0f0")
label_size.pack(anchor="w")

# Pizza Image
pizza_image = PhotoImage(file="pizza_slice.gif")  # Pizza slice image
pizza_label = Label(frame_size, image=pizza_image, bg="white", relief="ridge", bd=5)  # Add a border around the image
pizza_label.pack(anchor="w", padx=5, pady=10)

# Variable to track selected pizza size
size_var = StringVar(value="Medium")  # Default size

# Buttons for different sizes
button_frame = Frame(frame_size, bg="#f0f0f0")  # Frame for size buttons
button_frame.pack(pady=10)

button_small = Button(button_frame, text="Small: $10.99", font=("Times New Roman", 10), command=lambda: click("Small"))
button_small.pack(side="left", padx=5, pady=10)

button_medium = Button(button_frame, text="Medium: $12.99", font=("Times New Roman", 10), command=lambda: click("Medium"))
button_medium.pack(side="left", padx=5, pady=10)

button_large = Button(button_frame, text="Large: $14.99", font=("Times New Roman", 10), command=lambda: click("Large"))
button_large.pack(side="left", padx=5, pady=0)

# Crust Type Section
frame_crust = Frame(frame_size, relief="groove", bd=3, padx=10, pady=10, bg="#f0f0f0")  # Added outline and background
frame_crust.pack(anchor="w", padx=10, pady=10)

label_crust = Label(frame_crust, text="Step 2: Choose the crust type:", font=("Times New Roman", 11), anchor="w", bg="#f0f0f0")
label_crust.pack(anchor="w")

crust_var = StringVar(value="Hand-tossed")  # Default crust

# Crust Options (Radio Buttons)
crust_options = [("Hand-tossed", "Hand-tossed"), ("Deep-dish", "Deep-dish"), ("Thin-crust", "Thin-crust")]
for text, value in crust_options:
    rb = Radiobutton(frame_crust, text=text, variable=crust_var, value=value, font=("Times New Roman", 10), bg="#f0f0f0")
    rb.pack(anchor="w")

# Toppings Section
frame_toppings = Frame(frame_main, relief="groove", bd=3, padx=10, pady=10, bg="#f0f0f0")  # Added outline and background
frame_toppings.grid(row=0, column=1, padx=20, pady=5)

label_toppings = Label(frame_toppings, text="Step 3: Choose your toppings:", font=("Times New Roman", 11), anchor="w", bg="#f0f0f0")
label_toppings.pack(anchor="w")

# Checkboxes for toppings
toppings_vars = {}
toppings_options = ["Pepperoni", "Sausage", "Mushrooms", "Onions"]  # Available toppings

for topping in toppings_options:
    var = BooleanVar(value=False)  # Default is unchecked
    toppings_vars[topping] = var
    cb = Checkbutton(frame_toppings, text=topping, variable=var, font=("Times New Roman", 10), bg="#f0f0f0")
    cb.pack(anchor="w")

# Input Fields Section
frame_inputs = Frame(frame_toppings, bg="#f0f0f0")  # Section for user details
frame_inputs.pack(pady=10)

label_first_name = Label(frame_inputs, text="First Name:", font=("Times New Roman", 10), bg="#f0f0f0")
label_first_name.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_first_name = Entry(frame_inputs, width=30, font=("Times New Roman", 10))
entry_first_name.grid(row=0, column=1, padx=5, pady=5)

label_last_name = Label(frame_inputs, text="Last Name:", font=("Times New Roman", 10), bg="#f0f0f0")
label_last_name.grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_last_name = Entry(frame_inputs, width=30, font=("Times New Roman", 10))
entry_last_name.grid(row=1, column=1, padx=5, pady=5)

label_phone = Label(frame_inputs, text="Phone Number:", font=("Times New Roman", 10), bg="#f0f0f0")
label_phone.grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_phone = Entry(frame_inputs, width=30, font=("Times New Roman", 10))
entry_phone.grid(row=2, column=1, padx=5, pady=5)

# Order Button
order_button = Button(frame_toppings, text="Place Order", font=("Times New Roman", 12), bg="green", fg="white", command=lambda: click(size_var.get()))
order_button.pack(pady=10)

# Receipt Header
receipt_header = Label(root, text="Receipt", font=("Times New Roman", 14, "bold"), anchor="w")
receipt_header.place(x=850, y=160)

# Receipt Text Box
receipt = Text(root, width=30, height=17, wrap=WORD, font=("Courier", 12), background="white", relief="groove", bd=3)
receipt.place(x=750, y=190)

# Run the application
root.mainloop()