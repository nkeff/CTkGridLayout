import customtkinter


class CTkGridLayout(customtkinter.CTkFrame):
    def __init__(
            self,
            column_count: int = 1,
            spacing: int = 0,
            padding: int = None,
            **kwargs):
        super().__init__(**kwargs)
        self.column_count = column_count
        self.__spacing = spacing
        self.__padding = padding if padding is not None else spacing
        self.__items: list[customtkinter.CTkBaseClass] = []

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.update_layout()

    @property
    def items_count(self) -> int:
        return len(self.__items)

    @property
    def items(self) -> list[customtkinter.CTkBaseClass]:
        return self.__items

    def add_items(self, items: list[customtkinter.CTkBaseClass]):
        """ add list of items, update function call once """
        self.__items += items
        self.update_layout()

    def add_item(self, item: customtkinter.CTkBaseClass):
        """ add item in grid box """
        self.__items.append(item)
        self.update_layout()

    def update_layout(self, column_count: int = None, spacing: int = None, padding: int = None):
        """ update layout (change column count view, paddings and spacing between items """
        old_column_count = self.column_count
        self.column_count = column_count if column_count is not None else self.column_count
        self.__spacing = spacing if spacing is not None else self.__spacing
        self.__padding = padding if padding is not None else self.__padding
        for i in range(old_column_count + 1):
            self.grid_columnconfigure(i + 1, weight=0)
        for i in range(self.column_count):
            self.grid_columnconfigure(i, weight=1)
        for i, item in enumerate(self.__items):
            item.grid_forget()
            self.grid_rowconfigure(i // self.column_count, weight=1)
            item.grid(
                row=i // self.column_count,
                column=i % self.column_count,
                sticky="nsew",
                padx=(
                    self.__padding if i % self.column_count == 0 else self.__spacing,
                    self.__padding
                    if i % self.column_count == self.column_count - 1
                    else self.__spacing
                    if i % self.column_count == self.column_count - 1
                    else 0
                ),
                pady=(
                    self.__padding if i // self.column_count == 0 else self.__spacing,
                    self.__padding
                    if i // self.column_count == (len(self.__items) - 1) // self.column_count
                    else self.__spacing
                    if i // self.column_count == (len(self.__items) - 1) // self.column_count
                    else 0
                )
            )


class CTkScrollableGridLayout(customtkinter.CTkScrollableFrame):
    def __init__(
            self,
            column_count: int = 1,
            spacing: int = 0,
            padding: int = None,
            **kwargs):
        super().__init__(**kwargs)
        self.column_count = column_count
        self.__spacing = spacing
        self.__padding = padding if padding is not None else spacing
        self.__items: list[customtkinter.CTkBaseClass] = []

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.update_layout()

    @property
    def items_count(self):
        """ return count of items in grid box """
        return len(self.__items)

    @property
    def items(self) -> list[customtkinter.CTkBaseClass]:
        return self.__items

    def add_items(self, items: list[customtkinter.CTkBaseClass]):
        self.__items += items
        self.update_layout()

    def add_item(self, item: customtkinter.CTkBaseClass):
        self.__items.append(item)
        self.update_layout()

    def update_layout(self, column_count: int = None, spacing: int = None, padding: int = None):
        old_column_count = self.column_count
        self.column_count = column_count if column_count is not None else self.column_count
        self.__spacing = spacing if spacing is not None else self.__spacing
        self.__padding = padding if padding is not None else self.__padding
        for i in range(old_column_count + 1):
            self.grid_columnconfigure(i + 1, weight=0)
        for i in range(self.column_count):
            self.grid_columnconfigure(i, weight=1)
        for i, item in enumerate(self.__items):
            item.grid_forget()
            self.grid_rowconfigure(i // self.column_count, weight=1)
            item.grid(
                row=i // self.column_count,
                column=i % self.column_count,
                sticky="nsew",
                padx=(
                    self.__padding if i % self.column_count == 0 else self.__spacing,
                    self.__padding
                    if i % self.column_count == self.column_count - 1
                    else self.__spacing
                    if i % self.column_count == self.column_count - 1
                    else 0
                ),
                pady=(
                    self.__padding if i // self.column_count == 0 else self.__spacing,
                    self.__padding
                    if i // self.column_count == (len(self.__items) - 1) // self.column_count
                    else self.__spacing
                    if i // self.column_count == (len(self.__items) - 1) // self.column_count
                    else 0
                )
            )
