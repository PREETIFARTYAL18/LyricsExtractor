import tkinter as tk
from lyrics_extractor import SongLyrics

def fetch_lyrics():
    title = input_box.get()
    key = "AIzaSyAcZ6KgA7pCIa_uf8-bYdWR85vx6-dWqDg"
    engine = "aa2313d6c88d1bf22"
    try:
        finder = SongLyrics(key, engine)
        output = finder.get_lyrics(title)
        text_area.delete("1.0", tk.END)
        display = output['lyrics'].replace('. ', '.\n').replace('? ', '?\n').replace('! ', '!\n').replace('\\n', '\n')
        text_area.insert(tk.END, display)
    except Exception as err:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, f"Error: {str(err)}")

app = tk.Tk()
app.geometry('600x500')
app.title('Lyric Hunter')

tk.Label(app, text="Song Title:", font=('Arial', 14)).pack(pady=10)

input_box = tk.StringVar()
tk.Entry(app, textvariable=input_box, width=40).pack(pady=5)

tk.Button(app, text="Find Lyrics", command=fetch_lyrics).pack(pady=10)

text_area = tk.Text(app, wrap='word', bg="white", font=("Calibri", 12), padx=10, pady=10)
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

app.mainloop()
