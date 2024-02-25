import random

import customtkinter

from ctkgridlayout import CTkGridLayout, CTkScrollableGridLayout

if __name__ == "__main__":
    def random_color() -> str: return f"#{''.join([random.choice('123456789ABCDEF') for _ in range(6)])}"


    root = customtkinter.CTk()
    root.geometry("640x480")
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    main_grid = CTkScrollableGridLayout(master=root, column_count=5, spacing=15, padding=50)
    main_grid.add_items([customtkinter.CTkLabel(main_grid, fg_color=random_color(), text='') for i in range(25)])
    main_grid.grid(row=0, column=0, sticky="nsew")

    controls = CTkGridLayout(master=root, column_count=2, spacing=5, padding=10)
    controls.add_items(
        [
            customtkinter.CTkButton(
                master=controls,
                text="NEW ITEM",
                command=lambda: main_grid.add_item(customtkinter.CTkLabel(master=main_grid, fg_color=random_color(), text=""))
            ),
            customtkinter.CTkButton(
                master=controls,
                text="NEW 10 ITEMS",
                command=lambda: main_grid.add_items([customtkinter.CTkLabel(main_grid, fg_color=random_color(), text='') for _ in range(10)])
            ),
            customtkinter.CTkLabel(
                master=controls, text="PADDING"
            ),
            customtkinter.CTkSlider(
                master=controls,
                height=25,
                from_=0,
                to=20,
                number_of_steps=100,
                command=lambda x: main_grid.update_layout(padding=int(x))
            ),
            customtkinter.CTkLabel(
                master=controls, text="SPACING"
            ),
            customtkinter.CTkSlider(
                master=controls,
                height=25,
                from_=0,
                to=20,
                number_of_steps=20,
                command=lambda x: main_grid.update_layout(spacing=int(x))
            ),
            customtkinter.CTkLabel(
                master=controls, text="COLUMN_COUNT"
            ),
            customtkinter.CTkOptionMenu(
                master=controls,
                height=25,
                values=['1', '2', '3', '7', '10', str(main_grid.items_count)],
                command=lambda x: main_grid.update_layout(column_count=int(x))
            ),
        ]
    )
    controls.grid(row=1, column=0, sticky="nsew")

    root.mainloop()
