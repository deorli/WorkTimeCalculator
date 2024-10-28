import tkinter
import customtkinter
import os

from tkinter import filedialog, messagebox  # Import messagebox here
from settlement_folder import SettlementFolder


class TimeTrackingConfig(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        # Configure grid layout
        self.grid_columnconfigure(0, weight=0)  # Folder label column doesn't expand
        self.grid_columnconfigure(1, weight=1)  # Folder entry column expands

        # Folder selection label
        self.folder_label = customtkinter.CTkLabel(
            self, text="Select Annual Billing Folder:"
        )
        self.folder_label.grid(row=0, column=0, pady=(10, 5), sticky="w")  # Align to the west (left)

        # Entry field for folder path
        self.folder_entry = customtkinter.CTkEntry(self, placeholder_text="Folder path")
        self.folder_entry.grid(row=0, column=1, pady=(10, 5), sticky="ew")  # Fill horizontally

        # Button to browse for folder
        self.browse_button = customtkinter.CTkButton(
            self, text="Browse", command=self.browse_folder
        )
        self.browse_button.grid(row=1, column=1, pady=(0, 5), sticky="e")  # Align to the east (right)

        # Button to save configuration
        self.save_button = customtkinter.CTkButton(
            self, text="Save Configuration", command=self.save_configuration
        )
        self.save_button.grid(row=3, column=0, columnspan=2, pady=(10, 10))  # Center the save button across columns

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_entry.delete(0, tkinter.END)  # Clear the entry field
            self.folder_entry.insert(0, folder_selected)  # Insert selected folder path

    def save_configuration(self):
        settlement_folder = SettlementFolder()
        settlement_folder.create_folder()