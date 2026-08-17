import tkinter as tk
from tkinter import messagebox


# =========================================================
# MAIN WINDOW
# =========================================================
root = tk.Tk()
root.title("💍 Wedding Invitation Card")
root.geometry("1000x900")
root.configure(bg="#FFF5F8")
root.resizable(False, False)


# =========================================================
# COLORS
# =========================================================
PINK = "#D81B60"
DARK_PINK = "#880E4F"
LIGHT_PINK = "#FCE4EC"
PURPLE = "#6A1B9A"
LIGHT_PURPLE = "#F3E5F5"
GOLD = "#C59D1F"
CREAM = "#FFFDF7"
WHITE = "#FFFFFF"
TEXT = "#4A2635"


# =========================================================
# HEADER
# =========================================================
header = tk.Frame(
    root,
    bg=DARK_PINK,
    height=125
)
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


# =========================================================
# MAIN CARD / FORM
# =========================================================
main = tk.Frame(
    root,
    bg=CREAM,
    highlightbackground=GOLD,
    highlightthickness=3
)

main.pack(
    padx=40,
    pady=25,
    fill="both",
    expand=True
)


tk.Label(
    main,
    text="✨ Wedding Card Information ✨",
    font=("Georgia", 22, "bold"),
    bg=CREAM,
    fg=PURPLE
).pack(pady=(18, 12))


# =========================================================
# GUEST NAME SECTION
# =========================================================
guest_box = tk.Frame(
    main,
    bg="#FFF3E0",
    highlightbackground=GOLD,
    highlightthickness=2
)
guest_box.pack(
    padx=30,
    pady=8,
    fill="x"
)

tk.Label(
    guest_box,
    text="💌  CARD FOR / GUEST NAME",
    font=("Georgia", 14, "bold"),
    bg="#FFF3E0",
    fg=DARK_PINK
).pack(pady=(10, 4))

guest_entry = tk.Entry(
    guest_box,
    width=50,
    font=("Arial", 13),
    justify="center",
    bg=WHITE,
    fg=TEXT,
    relief="flat"
)
guest_entry.pack(
    pady=(0, 12),
    ipady=7
)


# =========================================================
# BRIDE & GROOM SECTION
# =========================================================
couple_frame = tk.Frame(
    main,
    bg=CREAM
)
couple_frame.pack(pady=5)


# -------------------------
# Bride
# -------------------------
bride_box = tk.Frame(
    couple_frame,
    bg=LIGHT_PINK,
    highlightbackground="#F48FB1",
    highlightthickness=2
)

bride_box.grid(
    row=0,
    column=0,
    padx=15
)

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

bride_entry.pack(
    padx=15,
    pady=(0, 15),
    ipady=7
)


# -------------------------
# Groom
# -------------------------
groom_box = tk.Frame(
    couple_frame,
    bg=LIGHT_PURPLE,
    highlightbackground="#BA68C8",
    highlightthickness=2
)

groom_box.grid(
    row=0,
    column=1,
    padx=15
)

tk.Label(
    groom_box,
    text="🤵  GROOM",
    font=("Georgia", 16, "bold"),
    bg=LIGHT_PURPLE,
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

groom_entry.pack(
    padx=15,
    pady=(0, 15),
    ipady=7
)


# =========================================================
# DETAILS SECTION
# =========================================================
details = tk.Frame(
    main,
    bg=CREAM
)

details.pack(pady=10)


def create_field(parent, row, column, label, width=22):

    frame = tk.Frame(
        parent,
        bg=CREAM
    )

    frame.grid(
        row=row,
        column=column,
        padx=15,
        pady=6
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

    entry.pack(
        ipady=6
    )

    return entry


date_entry = create_field(
    details,
    0,
    0,
    "📅 Wedding Date"
)

time_entry = create_field(
    details,
    0,
    1,
    "🕐 Wedding Time"
)

venue_entry = create_field(
    details,
    1,
    0,
    "🏛️ Wedding Venue"
)

city_entry = create_field(
    details,
    1,
    1,
    "📍 City"
)

contact_entry = create_field(
    details,
    2,
    0,
    "📞 Contact Number"
)


# =========================================================
# INVITATION MESSAGE
# =========================================================
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


# =========================================================
# GENERATE WEDDING CARD
# =========================================================
def generate_card():

    guest = guest_entry.get().strip()
    bride = bride_entry.get().strip()
    groom = groom_entry.get().strip()
    date = date_entry.get().strip()
    time = time_entry.get().strip()
    venue = venue_entry.get().strip()
    city = city_entry.get().strip()
    contact = contact_entry.get().strip()
    message = message_box.get("1.0", tk.END).strip()


    # Required fields
    if not guest:
        messagebox.showwarning(
            "Guest Name Missing",
            "Please enter the name of the person you want to give this card to."
        )
        return

    if not bride or not groom or not date or not venue:
        messagebox.showwarning(
            "Missing Information",
            "Please fill Bride, Groom, Date and Venue."
        )
        return


    # =====================================================
    # NEW CARD WINDOW
    # =====================================================
    card = tk.Toplevel(root)

    card.title("💍 Personalized Wedding Card")

    card.geometry(
        "750x820"
    )

    card.configure(
        bg="#FFF8E7"
    )

    card.resizable(
        False,
        False
    )


    # =====================================================
    # DECORATIVE BORDER
    # =====================================================
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


    # =====================================================
    # CARD TITLE
    # =====================================================
    tk.Label(
        border,
        text="🌸 WEDDING INVITATION 🌸",
        font=("Georgia", 25, "bold"),
        bg="#FFF8E7",
        fg=DARK_PINK
    ).pack(
        pady=(25, 8)
    )


    tk.Label(
        border,
        text="With the blessings of our families",
        font=("Georgia", 13, "italic"),
        bg="#FFF8E7",
        fg=TEXT
    ).pack()


    # =====================================================
    # GUEST NAME
    # =====================================================
    tk.Label(
        border,
        text=f"💌 Dear {guest},",
        font=("Georgia", 17, "bold"),
        bg="#FFF8E7",
        fg=PURPLE
    ).pack(
        pady=(25, 10)
    )


    tk.Label(
        border,
        text="You are cordially invited to celebrate",
        font=("Georgia", 12, "italic"),
        bg="#FFF8E7",
        fg=TEXT
    ).pack()


    # =====================================================
    # BRIDE
    # =====================================================
    tk.Label(
        border,
        text=bride,
        font=("Georgia", 28, "bold"),
        bg="#FFF8E7",
        fg=PINK
    ).pack(
        pady=(18, 3)
    )


    tk.Label(
        border,
        text="♥  &  ♥",
        font=("Georgia", 18, "bold"),
        bg="#FFF8E7",
        fg=GOLD
    ).pack()


    # =====================================================
    # GROOM
    # =====================================================
    tk.Label(
        border,
        text=groom,
        font=("Georgia", 28, "bold"),
        bg="#FFF8E7",
        fg=PURPLE
    ).pack(
        pady=(3, 20)
    )


    # =====================================================
    # DATE / TIME
    # =====================================================
    tk.Label(
        border,
        text=f"📅  {date}     |     🕐  {time}",
        font=("Arial", 13, "bold"),
        bg="#FFF8E7",
        fg=TEXT
    ).pack(
        pady=5
    )


    # =====================================================
    # VENUE
    # =====================================================
    tk.Label(
        border,
        text=f"🏛️  {venue}",
        font=("Arial", 14, "bold"),
        bg="#FFF8E7",
        fg=TEXT
    ).pack(
        pady=5
    )


    tk.Label(
        border,
        text=f"📍  {city}",
        font=("Arial", 12),
        bg="#FFF8E7",
        fg=TEXT
    ).pack()


    # =====================================================
    # MESSAGE
    # =====================================================
    tk.Label(
        border,
        text="💌",
        font=("Arial", 22),
        bg="#FFF8E7"
    ).pack(
        pady=(15, 3)
    )


    final_message = message

    if not final_message:
        final_message = (
            "We warmly invite you to celebrate "
            "this beautiful occasion with us."
        )


    tk.Label(
        border,
        text=final_message,
        font=("Georgia", 12, "italic"),
        bg="#FFF8E7",
        fg=TEXT,
        wraplength=570,
        justify="center"
    ).pack(
        padx=30
    )


    # =====================================================
    # CONTACT
    # =====================================================
    if contact:

        tk.Label(
            border,
            text=f"📞 Contact: {contact}",
            font=("Arial", 11, "bold"),
            bg="#FFF8E7",
            fg=DARK_PINK
        ).pack(
            pady=15
        )


    # =====================================================
    # FOOTER
    # =====================================================
    tk.Label(
        border,
        text="✨ Your presence will make our celebration more special ✨",
        font=("Georgia", 11, "italic"),
        bg="#FFF8E7",
        fg=GOLD
    ).pack(
        side="bottom",
        pady=20
    )


# =========================================================
# CLEAR FORM
# =========================================================
def clear_form():

    guest_entry.delete(0, tk.END)
    bride_entry.delete(0, tk.END)
    groom_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    venue_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)

    message_box.delete(
        "1.0",
        tk.END
    )


# =========================================================
# BUTTONS
# =========================================================
button_frame = tk.Frame(
    main,
    bg=CREAM
)

button_frame.pack(
    pady=14
)


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
).grid(
    row=0,
    column=0,
    padx=10
)


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
).grid(
    row=0,
    column=1,
    padx=10
)


# =========================================================
# FOOTER
# =========================================================
tk.Label(
    root,
    text="♥  With Love & Best Wishes  ♥",
    font=("Georgia", 13, "italic"),
    bg="#FFF5F8",
    fg=GOLD
).pack(
    pady=(0, 10)
)


# =========================================================
# START PROGRAM
# =========================================================
root.mainloop()