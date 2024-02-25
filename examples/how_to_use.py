import customtkinter

from ctkgridlayout import CTkGridLayout

if __name__ == "__main__":
    root = customtkinter.CTk()
    root.geometry("640x480")
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    GRID_VIEW = CTkGridLayout(master=root, column_count=2, spacing=15, padding=50)
    GRID_VIEW.add_items([
        customtkinter.CTkLabel(GRID_VIEW, text='first', fg_color='green'),
        customtkinter.CTkLabel(GRID_VIEW, text='second', fg_color='green'),
        customtkinter.CTkLabel(GRID_VIEW, text='third', fg_color='green'),
        customtkinter.CTkLabel(GRID_VIEW, text='fourth', fg_color='green'),
        customtkinter.CTkLabel(GRID_VIEW, text='fifth', fg_color='green'),
    ])
    GRID_VIEW.grid(row=0, column=0, sticky="nsew")
    root.mainloop()
