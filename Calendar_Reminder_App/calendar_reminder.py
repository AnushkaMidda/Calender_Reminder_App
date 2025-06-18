import tkinter as tk
from tkinter import messagebox
import calendar
import datetime

# -----------------------
# App Setup
# -----------------------
root = tk.Tk()
root.title("Calendar and Reminder App")
root.geometry("420x550")
root.configure(bg="#FFFACD")  # Light Yellow Background

reminders = []

# -----------------------
# Exit App Confirmation
# -----------------------
def exit_app():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

# -----------------------
# Show Calendar Function
# -----------------------
def show_calendar():
    # Loading Screen
    for widget in root.winfo_children():
        widget.destroy()

    loading_label = tk.Label(root, text="🔄 Loading Calendar...", font=("Helvetica", 25, "italic"), bg="#FFFACD")
    loading_label.pack(pady=50)
    root.after(1000, build_calendar_ui)  # Wait 1 second before showing calendar

# -----------------------
# Build Calendar UI
# -----------------------
def build_calendar_ui():
    for widget in root.winfo_children():
        widget.destroy()

    heading = tk.Label(root, text="📅 Here's Your Monthly Calendar!",
                       font=("Helvetica", 20, "bold"), bg="#FFFACD")
    heading.pack(pady=10)

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    cal_text = calendar.month(year, month)

    cal_frame = tk.Frame(root, bg="#FFFACD", bd=2, relief="groove")
    cal_frame.pack(pady=10)
    cal_label = tk.Label(cal_frame, text=cal_text,
                         font=("Courier", 16, "bold"), bg="#FFFACD", justify="left")
    cal_label.pack(padx=10, pady=5)

    # Reminder Section
    reminder_heading = tk.Label(root, text="📝 Set a Reminder Below",
                                font=("Helvetica", 18, "bold"), bg="#FFFACD")
    reminder_heading.pack(pady=10)

    # Date Entry
    date_label = tk.Label(root, text="Enter date (DD-MM-YYYY):", font=("Helvetica", 17), bg="#FFFACD")
    date_label.pack()
    date_entry = tk.Entry(root, width=35, font=("Helvetica", 14))
    date_entry.pack(pady=5)

    # Message Entry
    msg_label = tk.Label(root, text="Reminder Message:", font=("Helvetica", 17), bg="#FFFACD")
    msg_label.pack()
    msg_entry = tk.Entry(root, width=35, font=("Helvetica", 14))
    msg_entry.pack(pady=5)

    # Save Reminder Function
    def save_reminder():
        date = date_entry.get()
        message = msg_entry.get()
        if date and message:
            reminders.append((date, message))
            messagebox.showinfo("Reminder Saved", f"📌 Reminder on {date}:\n{message}")
            date_entry.delete(0, tk.END)
            msg_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Missing Info", "Please fill in both fields.")

    # View Reminders
    def view_reminders():
        if reminders:
            reminder_text = "\n".join([f"📅 {d} - {m}" for d, m in reminders])
            messagebox.showinfo("Your Saved Reminders", reminder_text)
        else:
            messagebox.showinfo("No Reminders", "You haven't saved any reminders yet.")

    # Buttons
    save_btn = tk.Button(root, text="💾 Save Reminder", command=save_reminder,
                         bg="#2196F3", fg="white", padx=10, pady=5, font=("Helvetica", 15, "bold"))
    save_btn.pack(pady=8)

    view_btn = tk.Button(root, text="📖 View All Reminders", command=view_reminders,
                         bg="#FFC107", fg="black", padx=10, pady=5, font=("Helvetica", 15, "bold"))
    view_btn.pack(pady=5)

    exit_btn = tk.Button(root, text="❌ Exit App", command=exit_app,
                         bg="#F44336", fg="white", padx=10, pady=5, font=("Helvetica", 15, "bold"))
    exit_btn.pack(pady=20)

# -----------------------
# Welcome Screen
# -----------------------
welcome_label = tk.Label(
    root,
    text="✨ Welcome to the Calendar and Reminder App!",
    font=("Helvetica", 22, "bold"),
    wraplength=350,
    justify="center",
    bg="#FFFACD"
)
welcome_label.pack(pady=60)

start_button = tk.Button(
    root,
    text="👉 Click to Begin",
    command=show_calendar,
    bg="#4CAF50",
    fg="white",
    padx=12,
    pady=6,
    font=("Helvetica", 16, "bold")
)
start_button.pack()

# -----------------------
# Run the App
# -----------------------
root.mainloop()
