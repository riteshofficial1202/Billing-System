import tkinter as tk
root = tk.Tk()
root.title("Restaurant Billing System")
root.geometry("600x500")
# Frames for organization
menu_frame = tk.Frame(root)
menu_frame.pack()
order_summary_frame = tk.Frame(root)
order_summary_frame.pack()
calculation_frame = tk.Frame(root)
calculation_frame.pack()
control_frame = tk.Frame(root)
control_frame.pack()
# Menu items with prices
menu_items = {
    "Burger": 60,
    "Pizza": 120,
    "Soda": 80,
    "Coffee": 50,
}
item_entries = {}
for item, price in menu_items.items():
    tk.Label(menu_frame, text=f"{item} - Rs.{price}").pack()
    qty_entry = tk.Entry(menu_frame)
    qty_entry.pack()
    item_entries[item] = qty_entry

def calculate_total():
    subtotal = 0
    for item, price in menu_items.items():
        qty = item_entries[item].get()
        if qty:
            subtotal += int(qty) * price

    tax = 0.1 * subtotal  # 10% tax
    discount = 0.05 * subtotal  # 5% discount
    total = subtotal + tax - discount

    result_text = f"Subtotal: {subtotal:.2f} Rupee\nTax: {tax:.2f} Rupee\nDiscount: {discount:.2f} Rupee\nTotal: {total:.2f} Rupee"
    result_label.config(text=result_text)

result_label = tk.Label(calculation_frame, text="", font=("Arial", 12))
result_label.pack()

tk.Button(control_frame, text="Calculate Bill", command=calculate_total).pack()
tk.Button(control_frame, text="Clear", command=lambda: [entry.delete(0, tk.END) for entry in item_entries.values()]).pack()
tk.Button(control_frame, text="Exit", command=root.quit).pack()
root.mainloop()