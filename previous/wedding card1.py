# using python language create a wedding card information form. 

import tkinter as tk
from tkinter import messagebox


# =========================
# MAIN WINDOW
# =========================
root = tk.Tk()
root.title("💍 Wedding Invitation Card")
root.geometry("1000x850")
root.configure(bg="#FFF5F8")
root.resizable(False, False)


# =========================
# COLORS
# =========================
PINK = "#D81B60"
DARK_PINK = "#880E4F"
LIGHT_PINK = "#FCE4EC"
PURPLE = "#6A1B9A"
GOLD = "#C59D1F"
CREAM = "#FFFDF7"
WHITE = "#FFFFFF"
TEXT = "#4A2635"


# =========================
# HEADER
# =========================
header = tk.Frame(root, bg=DARK_PINK, height=125)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="💍  WEDDING INVITATION  💍",
    font=("Georgia", 30, "bold"),
    bg=DARK_PINK,
    fg=WHITE
).pack(pady=(20, 5))

tk.Label(
    header,
    text="A beautiful beginning of a beautiful journey",
    font=("Georgia", 14, "italic"),
    bg=DARK_PINK,
    fg="#FFE082"
).pack()


# =========================
# MAIN CARD
# =========================
main = tk.Frame(
    root,
    bg=CREAM,
    highlightbackground=GOLD,
    highlightthickness=3
)
main.pack(padx=40, pady=25, fill="both", expand=True)


tk.Label(
    main,
    text="✨ Wedding Card Information ✨",
    font=("Georgia", 22, "bold"),
    bg=CREAM,
    fg=PURPLE
).pack(pady=(18, 12))


# =========================
# BRIDE & GROOM SECTION
# =========================
couple_frame = tk.Frame(main, bg=CREAM)
couple_frame.pack(pady=5)


# Bride
bride_box = tk.Frame(
    couple_frame,
    bg=LIGHT_PINK,
    highlightbackground="#F48FB1",
    highlightthickness=2
)
bride_box.grid(row=0, column=0, padx=15)

tk.Label(
    bride_box,
    text="👰  BRIDE",
    font=("Georgia", 16, "bold"),
    bg=LIGHT_PINK,
    fg=DARK_PINK
).pack(pady=(12, 5))

bride_entry = tk.Entry(
    bride_box,
    width=25,
    font=("Arial", 13),
    justify="center",
    bg=WHITE,
    fg=TEXT,
    relief="flat"
)
bride_entry.pack(padx=15, pady=(0, 15), ipady=7)


# Groom
groom_box = tk.Frame(
    couple_frame,
    bg="#F3E5F5",
    highlightbackground="#BA68C8",
    highlightthickness=2
)
groom_box.grid(row=0, column=1, padx=15)

tk.Label(
    groom_box,
    text="🤵  GROOM",
    font=("Georgia", 16, "bold"),
    bg="#F3E5F5",
    fg=PURPLE
).pack(pady=(12, 5))

groom_entry = tk.Entry(
    groom_box,
    width=25,
    font=("Arial", 13),
    justify="center",
    bg=WHITE,
    fg=TEXT,
    relief="flat"
)
groom_entry.pack(padx=15, pady=(0, 15), ipady=7)


# =========================
# DETAILS SECTION
# =========================
details = tk.Frame(main, bg=CREAM)
details.pack(pady=12)


def create_field(parent, row, column, label, width=22):
    frame = tk.Frame(parent, bg=CREAM)

    frame.grid(
        row=row,
        column=column,
        padx=15,
        pady=7
    )

    tk.Label(
        frame,
        text=label,
        font=("Arial", 11, "bold"),
        bg=CREAM,
        fg=TEXT
    ).pack(anchor="w")

    entry = tk.Entry(
        frame,
        width=width,
        font=("Arial", 11),
        bg=LIGHT_PINK,
        fg=TEXT,
        relief="flat"
    )
    entry.pack(ipady=6)

    return entry


date_entry = create_field(
    details, 0, 0, "📅 Wedding Date"
)

time_entry = create_field(
    details, 0, 1, "🕐 Wedding Time"
)

venue_entry = create_field(
    details, 1, 0, "🏛️ Wedding Venue"
)

city_entry = create_field(
    details, 1, 1, "📍 City"
)

contact_entry = create_field(
    details, 2, 0, "📞 Contact Number"
)


# =========================
# INVITATION MESSAGE
# =========================
tk.Label(
    main,
    text="💌  Invitation Message",
    font=("Georgia", 15, "bold"),
    bg=CREAM,
    fg=DARK_PINK
).pack(pady=(5, 5))


message_box = tk.Text(
    main,
    width=75,
    height=4,
    font=("Arial", 11),
    bg=LIGHT_PINK,
    fg=TEXT,
    relief="flat",
    wrap="word"
)
message_box.pack()


# =========================
# GENERATE CARD
# =========================
def generate_card():

    bride = bride_entry.get().strip()
    groom = groom_entry.get().strip()
    date = date_entry.get().strip()
    time = time_entry.get().strip()
    venue = venue_entry.get().strip()
    city = city_entry.get().strip()
    contact = contact_entry.get().strip()
    message = message_box.get("1.0", tk.END).strip()

    if not bride or not groom or not date or not venue:
        messagebox.showwarning(
            "Missing Information",
            "Please fill Bride, Groom, Date and Venue."
        )
        return

    # New window
    card = tk.Toplevel(root)
    card.title("💍 Your Wedding Card")
    card.geometry("700x750")
    card.configure(bg="#FFF8E7")
    card.resizable(False, False)

    # Decorative border
    border = tk.Frame(
        card,
        bg="#FFF8E7",
        highlightbackground=GOLD,
        highlightthickness=8
    )
    border.pack(
        padx=25,
        pady=25,
        fill="both",
        expand=True
    )

    tk.Label(
        border,
        text="🌸 WEDDING INVITATION 🌸",
        font=("Georgia", 25, "bold"),
        bg="#FFF8E7",
        fg=DARK_PINK
    ).pack(pady=(30, 10))

    tk.Label(
        border,
        text="With the blessings of our families",
        font=("Georgia", 13, "italic"),
        bg="#FFF8E7",
        fg=TEXT
    ).pack()

    tk.Label(
        border,
        text=bride,
        font=("Georgia", 28, "bold"),
        bg="#FFF8E7",
        fg=PINK
    ).pack(pady=(30, 3))

    tk.Label(
        border,
        text="♥  &  ♥",
        font=("Georgia", 18, "bold"),
        bg="#FFF8E7",
        fg=GOLD
    ).pack()

    tk.Label(
        border,
        text=groom,
        font=("Georgia", 28, "bold"),
        bg="#FFF8E7",
        fg=PURPLE
    ).pack(pady=(3, 25))

    tk.Label(
        border,
        text=f"📅  {date}     |     🕐  {time}",
        font=("Arial", 13, "bold"),
        bg="#FFF8E7",
        fg=TEXT
    ).pack(pady=5)

    tk.Label(
        border,
        text=f"🏛️  {venue}",
        font=("Arial", 14, "bold"),
        bg="#FFF8E7",
        fg=TEXT
    ).pack(pady=5)

    tk.Label(
        border,
        text=f"📍  {city}",
        font=("Arial", 12),
        bg="#FFF8E7",
        fg=TEXT
    ).pack()

    tk.Label(
        border,
        text="💌",
        font=("Arial", 22),
        bg="#FFF8E7"
    ).pack(pady=(18, 3))

    tk.Label(
        border,
        text=message if message else
        "We warmly invite you to celebrate this beautiful occasion with us.",
        font=("Georgia", 12, "italic"),
        bg="#FFF8E7",
        fg=TEXT,
        wraplength=570,
        justify="center"
    ).pack(padx=30)

    if contact:
        tk.Label(
            border,
            text=f"📞 Contact: {contact}",
            font=("Arial", 11, "bold"),
            bg="#FFF8E7",
            fg=DARK_PINK
        ).pack(pady=18)

    tk.Label(
        border,
        text="✨ Your presence will make our celebration more special ✨",
        font=("Georgia", 11, "italic"),
        bg="#FFF8E7",
        fg=GOLD
    ).pack(side="bottom", pady=25)


# =========================
# CLEAR FORM
# =========================
def clear_form():

    bride_entry.delete(0, tk.END)
    groom_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    venue_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    message_box.delete("1.0", tk.END)


# =========================
# BUTTONS
# =========================
button_frame = tk.Frame(main, bg=CREAM)
button_frame.pack(pady=15)


tk.Button(
    button_frame,
    text="💖  GENERATE WEDDING CARD",
    command=generate_card,
    font=("Arial", 12, "bold"),
    bg=PINK,
    fg=WHITE,
    activebackground=DARK_PINK,
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    width=25,
    pady=10
).grid(row=0, column=0, padx=10)


tk.Button(
    button_frame,
    text="🧹  CLEAR",
    command=clear_form,
    font=("Arial", 12, "bold"),
    bg=PURPLE,
    fg=WHITE,
    activebackground=DARK_PINK,
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    width=15,
    pady=10
).grid(row=0, column=1, padx=10)


# =========================
# FOOTER
# =========================
tk.Label(
    root,
    text="♥  With Love & Best Wishes  ♥",
    font=("Georgia", 13, "italic"),
    bg="#FFF5F8",
    fg=GOLD
).pack(pady=(0, 10))


root.mainloop()