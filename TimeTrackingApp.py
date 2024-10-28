import customtkinter
from time_tracking_config import TimeTrackingConfig  # Adjust the import based on your project structure

customtkinter.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

class TimeTrackingApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Time Tracking Application")
        self.geometry("1100x580")
        self.minsize(1100, 580)  # Set minimum window size

        # Configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1)

        # Sidebar title
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Time Tracker",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Sidebar buttons for tabs
        self.dashboard_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Dashboard", command=self.open_dashboard
        )
        self.dashboard_button.grid(row=1, column=0, padx=20, pady=10)

        self.report_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Report", command=self.open_report
        )
        self.report_button.grid(row=2, column=0, padx=20, pady=10)

        self.sessions_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Sessions", command=self.open_sessions
        )
        self.sessions_button.grid(row=3, column=0, padx=20, pady=10)

        self.statistics_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Statistics", command=self.open_statistics
        )
        self.statistics_button.grid(row=4, column=0, padx=20, pady=10)

        self.config_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Configuration", command=self.open_config
        )
        self.config_button.grid(row=5, column=0, padx=20, pady=10)

        self.help_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Help", command=self.open_help
        )
        self.help_button.grid(row=6, column=0, padx=20, pady=10)

        # Appearance mode toggle
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w"
        )
        self.appearance_mode_label.grid(row=8, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame, values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event
        )
        self.appearance_mode_optionmenu.set("Dark")  # Set default mode to Dark
        self.appearance_mode_optionmenu.grid(row=9, column=0, padx=20, pady=(10, 10))
    
        # Scaling option
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w"
        )
        self.scaling_label.grid(row=10, column=0, padx=20, pady=(10, 0))

        self.scaling_optionmenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event
        )
        self.scaling_optionmenu.set("100%")  # Set default scaling to 100%
        self.scaling_optionmenu.grid(row=11, column=0, padx=20, pady=(10, 20))

        # Main content area
        self.main_content_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_content_frame.grid(row=0, column=1, rowspan=4, sticky="nsew",
                                     padx=10, pady=10)

        # Placeholder main content
        self.main_label = customtkinter.CTkLabel(
            self.main_content_frame, text="Welcome to Time Tracker!",
            font=customtkinter.CTkFont(size=24, weight="bold")
        )
        self.main_label.pack(pady=(30, 20))

    def open_dashboard(self):
        self.main_label.configure(text="Dashboard: Overview of current progress")

    def open_report(self):
        self.main_label.configure(text="Report: View time tracking report")

    def open_sessions(self):
        self.main_label.configure(text="Sessions: Manage and review sessions")

    def open_statistics(self):
        self.main_label.configure(text="Statistics: View time and productivity trends")

    def open_config(self):
        # Clear the main content frame
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()

        # Create an instance of the TimeTrackingConfig class
        config_view = TimeTrackingConfig(self.main_content_frame)  # Pass the main content frame as the master
        
        # Pack the configuration view into the main content frame
        config_view.pack(fill="both", expand=True)

    def open_help(self):
        self.main_label.configure(text="Help: Learn more about how to use the app")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

# Run the app
if __name__ == "__main__":
    app = TimeTrackingApp()
    app.mainloop()
