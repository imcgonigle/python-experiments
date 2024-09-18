import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup

def fetch_links():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve URL:\n{e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize variables
    current_heading = 'No Heading'
    links_data = []

    # Define the tags to look for
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a']

    # Iterate over the elements in document order
    for element in soup.find_all(tags, recursive=True):
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            current_heading = element.get_text(strip=True)
        elif element.name == 'a':
            title = element.text.strip()
            href = element.get('href', '')
            target = element.get('target', '')
            rel = element.get('rel', '')
            if isinstance(rel, list):
                rel = ' '.join(rel)
            # Append the link data along with the current heading
            links_data.append((title, href, target, rel, current_heading))

    # Clear previous data
    for item in tree.get_children():
        tree.delete(item)

    # Insert new data into the treeview
    for data in links_data:
        tree.insert('', 'end', values=data)

# Set up GUI
root = tk.Tk()
root.title("Webpage Link Extractor")

# URL entry frame
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

url_label = tk.Label(entry_frame, text="Enter URL:")
url_label.pack(side=tk.LEFT)

url_entry = tk.Entry(entry_frame, width=50)
url_entry.pack(side=tk.LEFT, padx=5)

fetch_button = tk.Button(entry_frame, text="Fetch Links", command=fetch_links)
fetch_button.pack(side=tk.LEFT)

# Treeview frame
tree_frame = tk.Frame(root)
tree_frame.pack(fill=tk.BOTH, expand=True)

columns = ('Title', 'URL', 'Target', 'Rel', 'Location')
tree = ttk.Treeview(tree_frame, columns=columns, show='headings')

# Define headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor='w', stretch=True)

# Add vertical scrollbar
vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(side='right', fill='y')

tree.pack(side='left', fill=tk.BOTH, expand=True)

root.mainloop()

