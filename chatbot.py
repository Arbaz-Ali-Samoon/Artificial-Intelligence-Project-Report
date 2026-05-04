import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# =========================
# MAIN WINDOW
# =========================
window = tk.Tk()
window.title("AI Student Assistant Chatbot")
window.geometry("720x720")
window.configure(bg="#0f172a")
window.resizable(False, False)

# =========================
# TITLE
# =========================
title = tk.Label(
    window,
    text="AI Student Assistant Chatbot",
    font=("Arial", 20, "bold"),
    bg="#0f172a",
    fg="white"
)
title.pack(pady=10)

# =========================
# CHAT FRAME
# =========================
chat_frame = tk.Frame(window, bg="#334155", bd=2, relief="solid")
chat_frame.pack(padx=15, pady=10)

chat_area = scrolledtext.ScrolledText(
    chat_frame,
    width=75,
    height=25,
    font=("Arial", 12),
    bg="#1e293b",
    fg="white",
    insertbackground="white"
)
chat_area.pack()
chat_area.config(state='disabled')

# Welcome message
chat_area.config(state='normal')
chat_area.insert(tk.END, "Bot: Hello! I am your AI Assistant.\n")
chat_area.insert(tk.END, "Bot: Ask me anything simple.\n\n")
chat_area.config(state='disabled')

# =========================
# RESPONSE FUNCTION
# =========================
def get_response(msg):
    msg = msg.lower().strip()

    # Greetings
    if msg in ["hi", "hello", "hey", "hi there", "good morning", "good evening"]:
        return "Hello! How can I help you?"

    elif "how are you" in msg:
        return "I am just a program, but I am working fine 👍"

    # AI questions
    elif "what is ai" in msg:
        return "AI stands for Artificial Intelligence."

    elif "machine learning" in msg:
        return "Machine Learning is a branch of AI where systems learn from data."

    elif "nlp" in msg:
        return "NLP helps computers understand human language."

    elif "python" in msg:
        return "Python is a programming language used in AI and development."

    elif "chatbot" in msg:
        return "A chatbot is a program that talks with users."

    # Time & Date
    elif "time" in msg:
        return "Current time is " + datetime.now().strftime("%I:%M %p")

    elif "date" in msg:
        return "Today's date is " + datetime.now().strftime("%d-%m-%Y")

    # Calculator
    elif "+" in msg:
        try:
            a, b = msg.split("+")
            return "Answer: " + str(float(a) + float(b))
        except:
            return "Enter like 5+3"

    # Exit
    elif "bye" in msg or "exit" in msg:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I didn't understand that."

# =========================
# SEND MESSAGE
# =========================
def send_message():
    user_msg = entry.get()

    if user_msg.strip() == "":
        return

    chat_area.config(state='normal')
    chat_area.insert(tk.END, "You: " + user_msg + "\n")

    response = get_response(user_msg)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")

    chat_area.config(state='disabled')
    chat_area.yview(tk.END)

    entry.delete(0, tk.END)

# =========================
# CLEAR CHAT
# =========================
def clear_chat():
    chat_area.config(state='normal')
    chat_area.delete(1.0, tk.END)
    chat_area.config(state='disabled')

# =========================
# INPUT FRAME
# =========================
input_frame = tk.Frame(window, bg="#0f172a")
input_frame.pack(pady=10)

entry = tk.Entry(
    input_frame,
    width=40,
    font=("Arial", 14),
    justify="center"
)
entry.grid(row=0, column=0, padx=10)

# SEND BUTTON
send_btn = tk.Button(
    input_frame,
    text="➤",
    font=("Arial", 14, "bold"),
    bg="#22c55e",
    fg="white",
    width=4,
    command=send_message,
    cursor="hand2"
)
send_btn.grid(row=0, column=1, padx=5)

# DELETE BUTTON
delete_btn = tk.Button(
    input_frame,
    text="🗑 Delete",
    font=("Arial", 12, "bold"),
    bg="#ef4444",
    fg="white",
    width=10,
    command=clear_chat,
    cursor="hand2"
)
delete_btn.grid(row=0, column=2, padx=5)

# =========================
# FOOTER
# =========================
footer = tk.Label(
    window,
    text="Powered by Arbaz Ali Samoon",
    bg="#0f172a",
    fg="#94a3b8",
    font=("Arial", 10, "italic")
)
footer.pack(pady=5)

# ENTER KEY SUPPORT
window.bind("<Return>", lambda event: send_message())

# RUN APP
window.mainloop()