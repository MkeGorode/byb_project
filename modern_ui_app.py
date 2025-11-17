"""
Modern UI Application with Google Material Design / Microsoft Fluent Design principles
Focusing on: Clean aesthetics, proper spacing, modern colors, and intuitive user experience
"""

import tkinter as tk
from tkinter import messagebox


class ModernUI:
    """Modern UI Framework with Material Design / Fluent Design principles"""
    
    # Modern Color Palette (Google Material Design inspired)
    COLORS = {
        'primary': '#1a73e8',          # Google Blue
        'primary_dark': '#1557b0',     # Darker Blue
        'primary_light': '#e8f0fe',    # Light Blue background
        'accent': '#34a853',           # Google Green
        'accent_dark': '#2d8e47',      # Darker Green
        'error': '#ea4335',            # Google Red
        'warning': '#fbbc04',          # Google Yellow
        'background': '#ffffff',       # White
        'surface': '#f8f9fa',          # Light Gray
        'text_primary': '#202124',     # Dark Gray
        'text_secondary': '#5f6368',   # Medium Gray
        'border': '#dadce0',           # Border Gray
        'hover': '#f1f3f4',            # Hover state
    }
    
    # Modern Typography
    FONTS = {
        'heading1': ('Segoe UI', 24, 'bold'),
        'heading2': ('Segoe UI', 18, 'bold'),
        'heading3': ('Segoe UI', 14, 'bold'),
        'body': ('Segoe UI', 11),
        'body_bold': ('Segoe UI', 11, 'bold'),
        'caption': ('Segoe UI', 9),
        'button': ('Segoe UI', 10, 'bold'),
    }
    
    # Modern Spacing (following 8px grid system)
    SPACING = {
        'xs': 4,
        'sm': 8,
        'md': 16,
        'lg': 24,
        'xl': 32,
        'xxl': 48,
    }
    
    # Common Placeholders
    PLACEHOLDERS = {
        'name': 'Enter your name',
        'email': 'your.email@example.com',
    }
    
    @staticmethod
    def create_button(parent, text, command=None, style='primary', width=None):
        """Create a modern styled button"""
        if style == 'primary':
            bg = ModernUI.COLORS['primary']
            fg = '#ffffff'
            hover_bg = ModernUI.COLORS['primary_dark']
        elif style == 'accent':
            bg = ModernUI.COLORS['accent']
            fg = '#ffffff'
            hover_bg = ModernUI.COLORS['accent_dark']
        elif style == 'secondary':
            bg = ModernUI.COLORS['surface']
            fg = ModernUI.COLORS['text_primary']
            hover_bg = ModernUI.COLORS['hover']
        else:
            bg = ModernUI.COLORS['primary']
            fg = '#ffffff'
            hover_bg = ModernUI.COLORS['primary_dark']
        
        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg,
            fg=fg,
            font=ModernUI.FONTS['button'],
            relief=tk.FLAT,
            padx=ModernUI.SPACING['md'],
            pady=ModernUI.SPACING['sm'],
            cursor='hand2',
            borderwidth=0,
            highlightthickness=0,
        )
        
        if width:
            button.config(width=width)
        
        # Add hover effect
        def on_enter(e):
            button.config(bg=hover_bg)
        
        def on_leave(e):
            button.config(bg=bg)
        
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        
        return button
    
    @staticmethod
    def create_card(parent, title=None, **kwargs):
        """Create a modern card container"""
        card = tk.Frame(
            parent,
            bg=ModernUI.COLORS['background'],
            relief=tk.FLAT,
            borderwidth=1,
            highlightbackground=ModernUI.COLORS['border'],
            highlightthickness=1,
            **kwargs
        )
        
        if title:
            title_label = tk.Label(
                card,
                text=title,
                font=ModernUI.FONTS['heading3'],
                bg=ModernUI.COLORS['background'],
                fg=ModernUI.COLORS['text_primary'],
                anchor='w',
            )
            title_label.pack(
                fill=tk.X,
                padx=ModernUI.SPACING['md'],
                pady=(ModernUI.SPACING['md'], ModernUI.SPACING['sm'])
            )
        
        return card
    
    @staticmethod
    def create_entry(parent, placeholder='', width=None):
        """Create a modern styled entry field"""
        entry_frame = tk.Frame(parent, bg=ModernUI.COLORS['background'])
        
        entry = tk.Entry(
            entry_frame,
            font=ModernUI.FONTS['body'],
            bg=ModernUI.COLORS['background'],
            fg=ModernUI.COLORS['text_primary'],
            relief=tk.SOLID,
            borderwidth=1,
            highlightbackground=ModernUI.COLORS['border'],
            highlightcolor=ModernUI.COLORS['primary'],
            highlightthickness=1,
        )
        
        if width:
            entry.config(width=width)
        
        entry.pack(fill=tk.X, padx=2, pady=2)
        
        # Placeholder functionality
        if placeholder:
            entry.insert(0, placeholder)
            entry.config(fg=ModernUI.COLORS['text_secondary'])
            
            def on_focus_in(e):
                if entry.get() == placeholder:
                    entry.delete(0, tk.END)
                    entry.config(fg=ModernUI.COLORS['text_primary'])
            
            def on_focus_out(e):
                if not entry.get():
                    entry.insert(0, placeholder)
                    entry.config(fg=ModernUI.COLORS['text_secondary'])
            
            entry.bind('<FocusIn>', on_focus_in)
            entry.bind('<FocusOut>', on_focus_out)
        
        return entry_frame, entry
    
    @staticmethod
    def create_label(parent, text, style='body'):
        """Create a modern styled label"""
        if style == 'heading1':
            font = ModernUI.FONTS['heading1']
            color = ModernUI.COLORS['text_primary']
        elif style == 'heading2':
            font = ModernUI.FONTS['heading2']
            color = ModernUI.COLORS['text_primary']
        elif style == 'heading3':
            font = ModernUI.FONTS['heading3']
            color = ModernUI.COLORS['text_primary']
        elif style == 'caption':
            font = ModernUI.FONTS['caption']
            color = ModernUI.COLORS['text_secondary']
        else:
            font = ModernUI.FONTS['body']
            color = ModernUI.COLORS['text_primary']
        
        label = tk.Label(
            parent,
            text=text,
            font=font,
            bg=ModernUI.COLORS['background'],
            fg=color,
            anchor='w',
        )
        
        return label


class ModernApplication:
    """Sample Modern Application demonstrating the UI framework"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Modern UI Application")
        self.root.geometry("800x600")
        self.root.configure(bg=ModernUI.COLORS['surface'])
        
        # Make window resizable
        self.root.resizable(True, True)
        
        self.create_ui()
    
    def create_ui(self):
        """Create the modern user interface"""
        
        # Main container with padding
        main_container = tk.Frame(
            self.root,
            bg=ModernUI.COLORS['surface'],
        )
        main_container.pack(fill=tk.BOTH, expand=True, padx=ModernUI.SPACING['lg'], pady=ModernUI.SPACING['lg'])
        
        # Header section
        header = tk.Frame(main_container, bg=ModernUI.COLORS['surface'])
        header.pack(fill=tk.X, pady=(0, ModernUI.SPACING['lg']))
        
        title = ModernUI.create_label(header, "Modern UI Application", style='heading1')
        title.pack(anchor='w')
        
        subtitle = ModernUI.create_label(
            header,
            "Built with Google Material Design & Microsoft Fluent Design principles",
            style='caption'
        )
        subtitle.pack(anchor='w', pady=(ModernUI.SPACING['xs'], 0))
        
        # Content area with cards
        content = tk.Frame(main_container, bg=ModernUI.COLORS['surface'])
        content.pack(fill=tk.BOTH, expand=True)
        
        # Left column
        left_column = tk.Frame(content, bg=ModernUI.COLORS['surface'])
        left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, ModernUI.SPACING['sm']))
        
        # Card 1: Input Form
        form_card = ModernUI.create_card(left_column, title="User Input")
        form_card.pack(fill=tk.X, pady=(0, ModernUI.SPACING['md']))
        
        form_content = tk.Frame(form_card, bg=ModernUI.COLORS['background'])
        form_content.pack(fill=tk.X, padx=ModernUI.SPACING['md'], pady=(0, ModernUI.SPACING['md']))
        
        # Name field
        name_label = ModernUI.create_label(form_content, "Name:", style='body')
        name_label.pack(anchor='w', pady=(ModernUI.SPACING['sm'], ModernUI.SPACING['xs']))
        
        name_frame, self.name_entry = ModernUI.create_entry(form_content, placeholder=ModernUI.PLACEHOLDERS['name'])
        name_frame.pack(fill=tk.X, pady=(0, ModernUI.SPACING['sm']))
        
        # Email field
        email_label = ModernUI.create_label(form_content, "Email:", style='body')
        email_label.pack(anchor='w', pady=(ModernUI.SPACING['sm'], ModernUI.SPACING['xs']))
        
        email_frame, self.email_entry = ModernUI.create_entry(form_content, placeholder=ModernUI.PLACEHOLDERS['email'])
        email_frame.pack(fill=tk.X, pady=(0, ModernUI.SPACING['sm']))
        
        # Message field
        message_label = ModernUI.create_label(form_content, "Message:", style='body')
        message_label.pack(anchor='w', pady=(ModernUI.SPACING['sm'], ModernUI.SPACING['xs']))
        
        self.message_text = tk.Text(
            form_content,
            font=ModernUI.FONTS['body'],
            bg=ModernUI.COLORS['background'],
            fg=ModernUI.COLORS['text_primary'],
            relief=tk.SOLID,
            borderwidth=1,
            highlightbackground=ModernUI.COLORS['border'],
            highlightcolor=ModernUI.COLORS['primary'],
            highlightthickness=1,
            height=5,
            wrap=tk.WORD,
        )
        self.message_text.pack(fill=tk.X, pady=(0, ModernUI.SPACING['md']))
        
        # Button group
        button_frame = tk.Frame(form_content, bg=ModernUI.COLORS['background'])
        button_frame.pack(fill=tk.X)
        
        submit_btn = ModernUI.create_button(button_frame, "Submit", command=self.on_submit, style='primary')
        submit_btn.pack(side=tk.LEFT, padx=(0, ModernUI.SPACING['sm']))
        
        clear_btn = ModernUI.create_button(button_frame, "Clear", command=self.on_clear, style='secondary')
        clear_btn.pack(side=tk.LEFT)
        
        # Right column
        right_column = tk.Frame(content, bg=ModernUI.COLORS['surface'])
        right_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(ModernUI.SPACING['sm'], 0))
        
        # Card 2: Information
        info_card = ModernUI.create_card(right_column, title="Design Features")
        info_card.pack(fill=tk.X, pady=(0, ModernUI.SPACING['md']))
        
        info_content = tk.Frame(info_card, bg=ModernUI.COLORS['background'])
        info_content.pack(fill=tk.X, padx=ModernUI.SPACING['md'], pady=(0, ModernUI.SPACING['md']))
        
        features = [
            "✓ Modern color palette (Google Material Design)",
            "✓ Clean typography (Segoe UI font family)",
            "✓ 8px grid spacing system",
            "✓ Card-based layouts",
            "✓ Hover effects on interactive elements",
            "✓ Proper visual hierarchy",
            "✓ Responsive design patterns",
            "✓ Accessible color contrast",
        ]
        
        for feature in features:
            feature_label = ModernUI.create_label(info_content, feature, style='body')
            feature_label.pack(anchor='w', pady=(ModernUI.SPACING['xs'], 0))
        
        # Card 3: Actions
        action_card = ModernUI.create_card(right_column, title="Quick Actions")
        action_card.pack(fill=tk.X)
        
        action_content = tk.Frame(action_card, bg=ModernUI.COLORS['background'])
        action_content.pack(fill=tk.X, padx=ModernUI.SPACING['md'], pady=(0, ModernUI.SPACING['md']))
        
        action_label = ModernUI.create_label(
            action_content,
            "Perform quick actions:",
            style='body'
        )
        action_label.pack(anchor='w', pady=(ModernUI.SPACING['sm'], ModernUI.SPACING['md']))
        
        info_btn = ModernUI.create_button(
            action_content,
            "Show Info",
            command=self.show_info,
            style='primary',
            width=20
        )
        info_btn.pack(anchor='w', pady=(0, ModernUI.SPACING['sm']))
        
        success_btn = ModernUI.create_button(
            action_content,
            "Success Message",
            command=self.show_success,
            style='accent',
            width=20
        )
        success_btn.pack(anchor='w', pady=(0, ModernUI.SPACING['sm']))
        
        warning_btn = ModernUI.create_button(
            action_content,
            "About",
            command=self.show_about,
            style='secondary',
            width=20
        )
        warning_btn.pack(anchor='w')
        
        # Status bar
        self.create_status_bar()
    
    def create_status_bar(self):
        """Create a modern status bar"""
        status_bar = tk.Frame(
            self.root,
            bg=ModernUI.COLORS['surface'],
            height=30,
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        separator = tk.Frame(status_bar, bg=ModernUI.COLORS['border'], height=1)
        separator.pack(side=tk.TOP, fill=tk.X)
        
        self.status_label = ModernUI.create_label(
            status_bar,
            "Ready",
            style='caption'
        )
        self.status_label.pack(
            side=tk.LEFT,
            padx=ModernUI.SPACING['md'],
            pady=ModernUI.SPACING['xs']
        )
    
    def on_submit(self):
        """Handle submit button click"""
        name = self.name_entry.get()
        email = self.email_entry.get()
        message = self.message_text.get("1.0", tk.END).strip()
        
        # Check if fields are empty or contain placeholder text
        if not name or name == ModernUI.PLACEHOLDERS['name']:
            messagebox.showwarning("Validation Error", "Please enter your name.")
            return
        
        if not email or email == ModernUI.PLACEHOLDERS['email']:
            messagebox.showwarning("Validation Error", "Please enter your email.")
            return
        
        if not message:
            messagebox.showwarning("Validation Error", "Please enter a message.")
            return
        
        # Show success message
        messagebox.showinfo(
            "Success",
            f"Form submitted successfully!\n\nName: {name}\nEmail: {email}\nMessage: {message[:50]}..."
        )
        
        self.status_label.config(text="Form submitted successfully!")
    
    def on_clear(self):
        """Handle clear button click"""
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, ModernUI.PLACEHOLDERS['name'])
        self.name_entry.config(fg=ModernUI.COLORS['text_secondary'])
        
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, ModernUI.PLACEHOLDERS['email'])
        self.email_entry.config(fg=ModernUI.COLORS['text_secondary'])
        
        self.message_text.delete("1.0", tk.END)
        
        self.status_label.config(text="Form cleared")
    
    def show_info(self):
        """Show info message"""
        messagebox.showinfo(
            "Information",
            "This is a modern UI application built with Tkinter.\n\n"
            "It demonstrates Material Design and Fluent Design principles."
        )
    
    def show_success(self):
        """Show success message"""
        messagebox.showinfo(
            "Success",
            "Operation completed successfully!\n\n"
            "This demonstrates a success notification."
        )
    
    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo(
            "About",
            "Modern UI Application v2.0\n\n"
            "Design Principles:\n"
            "• Google Material Design\n"
            "• Microsoft Fluent Design\n\n"
            "Features modern colors, typography, and spacing."
        )


def main():
    """Main application entry point"""
    root = tk.Tk()
    app = ModernApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
