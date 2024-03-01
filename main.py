import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from styles import setup_button_styles

# шаблон
class Character:
    def __init__(self, name, strength, agility, intelligence, image_path):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.image = PhotoImage(file=image_path)
    
    def get_stats(self):
        return f"Сила: {self.strength}\nЛовкость: {self.agility}\nИнтеллект: {self.intelligence}"

class Warrior(Character):
    def __init__(self):
        super().__init__(name="Воин", strength=10, agility=5, intelligence=2, image_path="C:/dev/projects/RPG/src/npc/warrior.png")

class Rogue(Character):
    def __init__(self):
        super().__init__(name="Разбойник", strength=6, agility=10, intelligence=4, image_path="C:/dev/projects/RPG/src/npc/rogue.png")

class Mage(Character):
    def __init__(self):
        super().__init__(name="Маг", strength=3, agility=4, intelligence=10, image_path="C:/dev/projects/RPG/src/npc/mage.png")

class Paladin(Character):
    def __init__(self):
        super().__init__(name="Паладин", strength=8, agility=4, intelligence=6, image_path="C:/dev/projects/RPG/src/npc/paladin.png")

class Archer(Character):
    def __init__(self):
        super().__init__(name="Лучник", strength=5, agility=8, intelligence=5, image_path="C:/dev/projects/RPG/src/npc/archer.png")


# ui
class GameApp:
    def __init__(self, root):
        self.root = root
        self.characters = [Warrior(), Rogue(), Mage(), Paladin(), Archer()]
        self.character_choice = tk.IntVar(value=0)
        self.init_ui()
    
    def init_ui(self):
        setup_button_styles()
        self.root.title("ConsoleRPG by Stepan")
        self.root.iconbitmap("C:/dev/projects/RPG/src/favicon/favicon.ico")
        self.root.geometry("700x700")
        self.root.resizable(False, False)

        self.background_image = tk.PhotoImage(file="C:/dev/projects/RPG/src/background/background.png")
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.lower()
         
        
        self.header_image = PhotoImage(file="C:/dev/projects/RPG/src/header/header.png")
        self.header = tk.Label(self.root, image=self.header_image, width=700, height=190)
        self.header.pack()
        
        self.start_button = ttk.Button(self.root, text="Начать", command=self.start_game)
        self.start_button.pack(pady=25)
        
        self.exit_button = ttk.Button(self.root, text="Выйти", command=self.exit_game)
        self.exit_button.pack(pady=5)
    
    def start_game(self):
        self.start_button.pack_forget()
        self.exit_button.pack_forget()
        self.select_character()
    
    def exit_game(self):
        self.root.destroy()
    
    
    def select_character(self):
        self.character_frame = tk.Frame(self.root)
        self.character_frame.pack()
        
        tk.Label(self.character_frame, font=("Arial 18"), text="Выбери своего героя").pack()
        
        for index, char in enumerate(self.characters):
            rb_image = PhotoImage(file=f"C:/dev/projects/RPG/src/npc_avatar/{char.name.lower()}.png")
            rb = ttk.Radiobutton(self.character_frame, text=char.name, variable=self.character_choice, value=index, 
                                 compound='left', image=rb_image)
            rb.image = rb_image  # память
            rb.pack(anchor='w')
        
        self.select_button = ttk.Button(self.character_frame, text="Выбрать", command=self.confirm_selection)
        self.select_button.pack(pady=10)
    
    
    def confirm_selection(self):
        chosen_index = self.character_choice.get()
        self.show_stats(self.characters[chosen_index])
    
    def show_stats(self, character):
        self.character_frame.pack_forget()
        
        self.avatar = tk.Label(self.root, image=character.image, width=300, height=300)
        self.avatar.image = character.image
        self.avatar.pack()
        
        self.stats = tk.Label(self.root, font=("Arial 16"),text=character.get_stats())
        self.stats.pack()
        
        self.back_button = ttk.Button(self.root, text="Назад", command=self.back_to_select)
        self.back_button.pack(pady=25)
    
    def back_to_select(self):
        self.avatar.pack_forget()
        self.stats.pack_forget()
        self.back_button.pack_forget()
        self.select_character()

def main():
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
