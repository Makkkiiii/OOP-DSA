import tkinter as tk
from tkinter import scrolledtext
from termcolor import colored # type: ignore
import requests #type: ignore
from bs4 import BeautifulSoup # type: ignore
import re
from datetime import datetime
from urllib.parse import urljoin


class WebCrawler:
    def __init__(self, url, max_depth, output_text_widget):
        self.url = url
        self.max_depth = max_depth
        self.subdomains = set()
        self.links = set()
        self.jsfiles = set()
        self.output_text = output_text_widget

    def start_crawling(self):
        self.crawl(self.url, depth=1)

    def crawl(self, url, depth):
        if depth > self.max_depth:
            return

        try:
            response = requests.get(url, timeout=3, allow_redirects=True)
            soup = BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as err:
            self.output_text.insert(tk.END, f"[-] An error occurred: {err}\n")
            return

        subdomain_query = fr"https?://([a-zA-Z0-9.-]+)"

        from bs4 import Tag

        for link in soup.find_all('a'):
            if isinstance(link, Tag):
                link_text = link.get('href')
                if isinstance(link_text, str) and link_text:
                    if re.match(subdomain_query, link_text) and link_text not in self.subdomains:
                        self.subdomains.add(link_text)
                    else:
                        full_link = urljoin(url, link_text)
                        if full_link != url and full_link not in self.links:
                            self.links.add(full_link)
                            self.crawl(full_link, depth + 1)

        for file in soup.find_all('script'):
            if isinstance(file, Tag):
                script_src = file.get('src')
                if isinstance(script_src, str) and script_src:
                    self.jsfiles.add(script_src)

    def print_banner(self):
        self.output_text.insert(tk.END, "-" * 80 + "\n")
        self.output_text.insert(tk.END,
                                f"{colored(f'Recursive Web Crawler starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}', 'cyan', attrs=['bold'])}\n")
        self.output_text.insert(tk.END, "-" * 80 + "\n")
        self.output_text.insert(tk.END, f"[*] URL".ljust(20, " "), ":", self.url + "\n")
        self.output_text.insert(tk.END, f"[*] Max Depth".ljust(20, " ") + ":", str(self.max_depth) + "\n")  # Fixed line
        self.output_text.insert(tk.END, "-" * 80 + "\n")

    def print_results(self):
        if self.subdomains:
            for subdomain in self.subdomains:
                self.output_text.insert(tk.END, f"[+] Subdomains : {subdomain}\n")

        if self.links:
            for link in self.links:
                self.output_text.insert(tk.END, f"[+] Links : {link}\n")

        if self.jsfiles:
            for file in self.jsfiles:
                self.output_text.insert(tk.END, f"[+] JS Files : {file}\n")


def start_crawl():
    url = url_entry.get()
    try:
        depth = int(depth_entry.get())
    except ValueError:
        output_text.insert(tk.END, "[-] Invalid depth value.\n")
        return

    if not url:
        output_text.insert(tk.END, "[-] Please enter a URL.\n")
        return

    # Clear the output text box before starting a new crawl
    output_text.delete(1.0, tk.END)

    # Initialize the web crawler with user input and display output
    web_crawler = WebCrawler(url, depth, output_text)
    web_crawler.print_banner()
    web_crawler.start_crawling()
    web_crawler.print_results()


# Set up the main window
root = tk.Tk()
root.title("Web Crawler GUI")

# Create and place the URL label and entry box
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create and place the Depth label and entry box
depth_label = tk.Label(root, text="Enter Depth:")
depth_label.pack(pady=5)
depth_entry = tk.Entry(root, width=50)
depth_entry.pack(pady=5)

# Create and place the Submit button
submit_button = tk.Button(root, text="Start Crawling", command=start_crawl)
submit_button.pack(pady=10)

# Create and place the Output text box with scroll functionality
output_text = scrolledtext.ScrolledText(root, width=80, height=20)
output_text.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
