import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simpli Music Player")
        self.root.geometry("485x700+290+10")
        self.root.configure(background='#333333')
        self.root.resizable(False, False)
        mixer.init()

        self.playlist = []  # Store the playlist as a list
        self.current_song_index = 0  # Store the index of the currently playing song

        # Create a function to open a file
        def add_music():
            path = filedialog.askdirectory()
            if path:
                try:
                    os.chdir(path)
                    songs = os.listdir(path)

                    for song in songs:
                        if song.endswith(".mp3"):
                            self.playlist.append(song)
                            self.playlist_box.insert(tk.END, song)
                except Exception as e:
                    self.show_error("Error Adding Music", str(e))

        def play_music():
            if self.playlist:
                selected_song = self.playlist[self.current_song_index]
                try:
                    mixer.music.load(selected_song)
                    mixer.music.play()
                except Exception as e:
                    self.show_error("Error Playing Music", str(e))

        def stop_music():
            try:
                mixer.music.stop()
            except Exception as e:
                self.show_error("Error Stopping Music", str(e))

        def pause_music():
            try:
                mixer.music.pause()
            except Exception as e:
                self.show_error("Error Pausing Music", str(e))

        def unpause_music():
            try:
                mixer.music.unpause()
            except Exception as e:
                self.show_error("Error Unpausing Music", str(e))

        def add_to_stack():
            if self.playlist:
                current_song = self.playlist[self.current_song_index]
                self.song_stack.append(current_song)
                self.update_stack_label()

        def play_from_stack():
            if self.song_stack:
                selected_song = self.song_stack.pop()
                try:
                    mixer.music.load(selected_song)
                    mixer.music.play()
                    self.update_stack_label()
                except Exception as e:
                    self.show_error("Error Playing from Stack", str(e))

        def play_next_song():
            if self.playlist:
                self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
                play_music()

        def play_previous_song():
            if self.playlist:
                self.current_song_index = (self.current_song_index - 1) % len(self.playlist)
                play_music()

        def update_stack_label():
            self.stack_label.config(text="Song Stack:\n" + "\n".join(self.song_stack))
 
        def show_error(title, message):
            tk.messagebox.showerror(title, message)

        # GUI Components
        button_play = tk.PhotoImage(file="play1.png")
        tk.Button(self.root, image=button_play, bg="#FFFFFF", bd=0, height=60, width=60,
                  command=play_music).place(x=215, y=487)

        button_stop = tk.PhotoImage(file="stop1.png")
        tk.Button(self.root, image=button_stop, bg="#FFFFFF", bd=0, height=60, width=60,
                  command=stop_music).place(x=130, y=487)

        button_volume = tk.PhotoImage(file="volume.png")
        tk.Button(self.root, image=button_volume, bg="#FFFFFF", bd=0, height=60, width=60,
                  command=unpause_music).place(x=20, y=487)

        button_pause = tk.PhotoImage(file="pause1.png")
        tk.Button(self.root, image=button_pause, bg="#FFFFFF", bd=0, height=60, width=60,
                  command=pause_music).place(x=300, y=487)

        menu_image = tk.PhotoImage(file="menu.png")
        tk.Label(self.root, image=menu_image).place(x=0, y=580, width=485, height=120)

        frame_music = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        frame_music.place(x=0, y=585, width=485, height=100)

        tk.Button(self.root, text="Browse Music", width=59, height=1, font=("calibri", 12, "bold"),
                  fg="Black", bg="#FFFFFF", command=add_music).place(x=0, y=550)

        scroll = tk.Scrollbar(frame_music)
        self.playlist_box = tk.Listbox(frame_music, width=100, font=("Times new roman", 10),
                                  bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
        scroll.config(command=self.playlist_box.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.playlist_box.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.song_stack = []
        self.stack_label = tk.Label(self.root, text="Song Stack:")
        self.stack_label.place(x=0, y=680, width=485, height=20)

        add_to_stack_button = tk.Button(self.root, text="Add to Stack", width=59, height=1, font=("calibri", 12, "bold"),
                                        fg="Black", bg="#FFFFFF", command=add_to_stack)
        add_to_stack_button.place(x=0, y=650)

        play_stack_button = tk.Button(self.root, text="Play from Stack", width=59, height=1, font=("calibri", 12, "bold"),
                                      fg="Black", bg="#FFFFFF", command=play_from_stack)
        play_stack_button.place(x=0, y=720)

        play_next_button = tk.Button(self.root, text="Next Song", width=59, height=1, font=("calibri", 12, "bold"),
                                    fg="Black", bg="#FFFFFF", command=play_next_song)
        play_next_button.place(x=0, y=750)

        play_previous_button = tk.Button(self.root, text="Previous Song", width=59, height=1, font=("calibri", 12, "bold"),
                                    fg="Black", bg="#FFFFFF", command=play_previous_song)
        play_previous_button.place(x=0, y=780)

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()
