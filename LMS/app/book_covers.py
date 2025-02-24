import os
import sqlite3
import requests
import re
from flask import current_app
from tqdm import tqdm

def get_db_path():
    from app import create_app  # Import inside the function to avoid circular import
    app = create_app()
    with app.app_context():
        return os.path.join(current_app.instance_path, "library.db")

def get_save_dir():
    from app import create_app  # Import inside the function
    app = create_app()
    with app.app_context():
        return os.path.join(current_app.static_folder, "covers")

def slugify(title):
    return re.sub(r'[\W_]+', '-', title.lower()).strip('-')

def get_book_titles():
    DB_PATH = get_db_path()  # Call inside function
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM book")
        titles = [row[0] for row in cursor.fetchall()]
        return titles
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
        return []

def get_cover_url(title):
    try:
        params = {"q": title}
        response = requests.get("https://www.googleapis.com/books/v1/volumes", params=params)
        data = response.json()

        if "items" in data:
            return data["items"][0]["volumeInfo"].get("imageLinks", {}).get("thumbnail")
        return None
    except requests.RequestException as e:
        print(f"❌ Request error: {e}")
        return None

def download_cover(title):
    SAVE_DIR = get_save_dir()  # Call inside function
    os.makedirs(SAVE_DIR, exist_ok=True)
    
    cover_url = get_cover_url(title)
    if not cover_url:
        print(f"❌ No cover found for: {title}")
        return

    filename = f"{slugify(title)}.jpg"
    filepath = os.path.join(SAVE_DIR, filename)

    try:
        response = requests.get(cover_url)
        if response.status_code == 200:
            with open(filepath, "wb") as f:
                f.write(response.content)
            print(f"✅ Downloaded: {filepath}")
        else:
            print(f"❌ Failed to download: {title}")
    except Exception as e:
        print(f"❌ Error downloading cover: {e}")

def main():
    book_titles = get_book_titles()
    for title in tqdm(book_titles, desc="Downloading covers"):
        download_cover(title)
