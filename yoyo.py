import random
from datetime import datetime
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext

# ------------------ Original logic functions adapted for GUI ------------------

def item_id():
    return random.randint(10000, 99999)

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def save_file(filename, records):
    with open(filename, "w") as f:
        for rec in records:
            f.write(" | ".join(rec) + "\n")

def loadfiles(filename):
    records = []
    if not os.path.exists(filename):
        return records
    with open(filename, "r") as f:
        for line in f:
            fields = [x.strip() for x in line.split("|")]
            records.append(fields)
    return records

# filenames (same as original)
FOUND_FILE = "found.txt"
LOST_FILE  = "lost.txt"

# ------------------ GUI App ------------------

class LostFoundApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("College Lost & Found Manager")
        self.geometry("760x520")
        self.resizable(False, False)

        # container for pages
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (HomePage, FoundReportPage, LostReportPage, AdminLoginPage, AdminPanelPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

# ------------------ Pages ------------------

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        header = tk.Label(self, text="LOST & FOUND SYSTEM", font=("Helvetica", 18, "bold"))
        header.pack(pady=20)

        btn_found = tk.Button(self, text="Report Found Item", width=25, command=lambda: controller.show_frame(FoundReportPage))
        btn_found.pack(pady=8)

        btn_lost = tk.Button(self, text="Report Lost Item", width=25, command=lambda: controller.show_frame(LostReportPage))
        btn_lost.pack(pady=8)

        btn_admin = tk.Button(self, text="Admin Login", width=25, command=lambda: controller.show_frame(AdminLoginPage))
        btn_admin.pack(pady=8)

        btn_exit = tk.Button(self, text="Exit", width=25, command=self.quit)
        btn_exit.pack(pady=8)


class FoundReportPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Report Found Item", font=("Helvetica", 14, "bold")).pack(pady=12)

        form = tk.Frame(self)
        form.pack(pady=8)

        tk.Label(form, text="Item Name:").grid(row=0, column=0, sticky="e", padx=6, pady=6)
        self.name_entry = tk.Entry(form, width=50)
        self.name_entry.grid(row=0, column=1)

        tk.Label(form, text="Description:").grid(row=1, column=0, sticky="e", padx=6, pady=6)
        self.desc_entry = tk.Entry(form, width=50)
        self.desc_entry.grid(row=1, column=1)

        tk.Label(form, text="Finder Name:").grid(row=2, column=0, sticky="e", padx=6, pady=6)
        self.finder_entry = tk.Entry(form, width=50)
        self.finder_entry.grid(row=2, column=1)

        tk.Label(form, text="Contact Number:").grid(row=3, column=0, sticky="e", padx=6, pady=6)
        self.contact_entry = tk.Entry(form, width=50)
        self.contact_entry.grid(row=3, column=1)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=12)
        tk.Button(btn_frame, text="Submit", command=self.submit_found).grid(row=0, column=0, padx=6)
        tk.Button(btn_frame, text="Back", command=lambda: controller.show_frame(HomePage)).grid(row=0, column=1, padx=6)

    def submit_found(self):
        item_ID = str(item_id())
        name = self.name_entry.get().strip()
        desc = self.desc_entry.get().strip()
        finder = self.finder_entry.get().strip()
        contact = self.contact_entry.get().strip()
        date = timestamp()
        status = "unclaimed"
        claimed_by = "None"

        # mimic original: minimal validation (don't add features)
        if not name or not desc or not finder or not contact:
            messagebox.showwarning("Missing Data", "Please fill all fields.")
            return

        record = [item_ID, name, desc, finder, contact, date, status, claimed_by]
        with open(FOUND_FILE, "a") as f:
            f.write(" | ".join(record) + "\n")

        messagebox.showinfo("Success", f"Item Recorded Successfully!\nFound ID = {item_ID}")
        # clear fields
        self.name_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.finder_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)


class LostReportPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Report Lost Item", font=("Helvetica", 14, "bold")).pack(pady=12)

        form = tk.Frame(self)
        form.pack(pady=8)

        tk.Label(form, text="Item Name:").grid(row=0, column=0, sticky="e", padx=6, pady=6)
        self.name_entry = tk.Entry(form, width=50)
        self.name_entry.grid(row=0, column=1)

        tk.Label(form, text="Description:").grid(row=1, column=0, sticky="e", padx=6, pady=6)
        self.desc_entry = tk.Entry(form, width=50)
        self.desc_entry.grid(row=1, column=1)

        tk.Label(form, text="Your Name:").grid(row=2, column=0, sticky="e", padx=6, pady=6)
        self.owner_entry = tk.Entry(form, width=50)
        self.owner_entry.grid(row=2, column=1)

        tk.Label(form, text="Contact Number:").grid(row=3, column=0, sticky="e", padx=6, pady=6)
        self.contact_entry = tk.Entry(form, width=50)
        self.contact_entry.grid(row=3, column=1)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=12)
        tk.Button(btn_frame, text="Submit", command=self.submit_lost).grid(row=0, column=0, padx=6)
        tk.Button(btn_frame, text="Back", command=lambda: controller.show_frame(HomePage)).grid(row=0, column=1, padx=6)

    def submit_lost(self):
        lost_id = str(item_id())
        name = self.name_entry.get().strip()
        desc = self.desc_entry.get().strip()
        owner = self.owner_entry.get().strip()
        contact = self.contact_entry.get().strip()
        date = timestamp()
        status = "unresolved"
        matched = "None"

        if not name or not desc or not owner or not contact:
            messagebox.showwarning("Missing Data", "Please fill all fields.")
            return

        record = [lost_id, name, desc, owner, contact, date, status, matched]
        with open(LOST_FILE, "a") as f:
            f.write(" | ".join(record) + "\n")

        messagebox.showinfo("Success", f"Lost Report Submitted!\nLost ID = {lost_id}")
        # clear fields
        self.name_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.owner_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)


class AdminLoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Admin Login", font=("Helvetica", 14, "bold")).pack(pady=12)

        form = tk.Frame(self)
        form.pack(pady=8)

        tk.Label(form, text="Enter Admin Password:").grid(row=0, column=0, padx=6, pady=6)
        self.pw_entry = tk.Entry(form, show="*", width=30)
        self.pw_entry.grid(row=0, column=1)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Login", command=self.check_login).grid(row=0, column=0, padx=6)
        tk.Button(btn_frame, text="Back", command=lambda: controller.show_frame(HomePage)).grid(row=0, column=1, padx=6)

    def check_login(self):
        entered = self.pw_entry.get()
        # password same as original
        if entered == "admin123":
            messagebox.showinfo("Login Successful", "Access Granted")
            self.pw_entry.delete(0, tk.END)
            self.controller.show_frame(AdminPanelPage)
        else:
            messagebox.showerror("Login Failed", "Wrong password")
            self.pw_entry.delete(0, tk.END)


class AdminPanelPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        header = tk.Label(self, text="ADMIN PANEL", font=("Helvetica", 14, "bold"))
        header.pack(pady=10)

        btnframe = tk.Frame(self)
        btnframe.pack(pady=6)

        tk.Button(btnframe, text="View Found Items", width=18, command=self.view_found).grid(row=0, column=0, padx=6, pady=4)
        tk.Button(btnframe, text="View Lost Reports", width=18, command=self.view_lost).grid(row=0, column=1, padx=6, pady=4)
        tk.Button(btnframe, text="Mark Item Claimed", width=18, command=self.mark_claimed).grid(row=1, column=0, padx=6, pady=4)
        tk.Button(btnframe, text="Auto-Match", width=18, command=self.auto_match).grid(row=1, column=1, padx=6, pady=4)
        tk.Button(btnframe, text="View Statistics", width=18, command=self.view_stats).grid(row=2, column=0, padx=6, pady=4)
        tk.Button(btnframe, text="Back to Main Menu", width=38, command=lambda: controller.show_frame(HomePage)).grid(row=3, column=0, columnspan=2, pady=8)

        # area to show results
        self.output = scrolledtext.ScrolledText(self, width=86, height=18)
        self.output.pack(pady=8)
        self.output.configure(state='disabled')

    def write_output(self, text):
        self.output.configure(state='normal')
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, text)
        self.output.configure(state='disabled')

    def view_found(self):
        items = loadfiles(FOUND_FILE)
        if not items:
            self.write_output("No items found.\n")
            return
        s = "========= Found Items =========\n\n"
        for i in items:
            s += f"ID: {i[0]}\nItem: {i[1]}\nDescription: {i[2]}\nFinder: {i[3]}\nContact: {i[4]}\nDate: {i[5]}\nStatus: {i[6]}\nClaimed by: {i[7]}\n"
            s += "----------------------------------\n"
        self.write_output(s)

    def view_lost(self):
        items = loadfiles(LOST_FILE)
        if not items:
            self.write_output("No lost reports.\n")
            return
        s = "========= Lost Reports =========\n\n"
        for i in items:
            s += f"ID: {i[0]}\nItem: {i[1]}\nDescription: {i[2]}\nOwner: {i[3]}\nContact: {i[4]}\nDate: {i[5]}\nStatus: {i[6]}\nMatch: {i[7]}\n"
            s += "----------------------------------\n"
        self.write_output(s)

    def mark_claimed(self):
        # simple dialog using a small window to gather ID and claimer (matching original)
        win = tk.Toplevel(self)
        win.title("Mark Item Claimed")
        win.geometry("400x160")
        tk.Label(win, text="Enter the item ID:").pack(pady=6)
        id_entry = tk.Entry(win, width=30)
        id_entry.pack(pady=4)
        tk.Label(win, text="Enter name of person who claimed:").pack(pady=6)
        claimer_entry = tk.Entry(win, width=30)
        claimer_entry.pack(pady=4)

        def do_mark():
            item_id_val = id_entry.get().strip()
            claimed_by_val = claimer_entry.get().strip()
            if not item_id_val or not claimed_by_val:
                messagebox.showwarning("Missing Data", "Please fill all fields.")
                return

            items = loadfiles(FOUND_FILE)
            for i in items:
                if i[0] == item_id_val:
                    i[6] = "claimed"
                    i[7] = claimed_by_val
                    save_file(FOUND_FILE, items)
                    messagebox.showinfo("Success", "Item marked as claimed successfully!")
                    win.destroy()
                    self.view_found()
                    return
            messagebox.showerror("Error", "Invalid ID")

        tk.Button(win, text="Mark Claimed", command=do_mark).pack(pady=8)

    def auto_match(self):
        found = loadfiles(FOUND_FILE)
        lost = loadfiles(LOST_FILE)
        out_lines = []
        for L in lost:
            if L[6] == "resolved":
                continue
            for F in found:
                if F[6] == "claimed":
                    continue
                if L[1].lower() in F[1].lower() or F[1].lower() in L[1].lower():
                    out_lines.append(f" Possible Match → Found ID: {F[0]} | {F[1]} | {F[2]}\n")
        if not out_lines:
            self.write_output("No possible matches found.\n")
        else:
            self.write_output("--- Possible Matches ---\n\n" + "".join(out_lines))

    def view_stats(self):
        found = loadfiles(FOUND_FILE)
        lost = loadfiles(LOST_FILE)
        total_found = len(found)
        total_lost = len(lost)
        claimed = sum(1 for i in found if i[6] == "claimed")
        unresolved = sum(1 for i in lost if i[6] == "unresolved")
        s = "\n---- Statistics Dashboard ----\n"
        s += f"Total Found Items: {total_found}\n"
        s += f"Total Lost Reports: {total_lost}\n"
        s += f"Total Claimed Items: {claimed}\n"
        s += f"Unresolved Lost Items: {unresolved}\n"
        s += "----------------------------------\n"
        self.write_output(s)


# ------------------ Run App ------------------

if __name__ == "__main__":
    app = LostFoundApp()
    app.mainloop()
