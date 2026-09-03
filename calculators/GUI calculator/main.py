from canvas import app
from buttons import render_number_button_screen, render_operations_buttons, render_deleting_buttons

if __name__ == '__main__':
    render_number_button_screen()
    render_operations_buttons()
    render_deleting_buttons()
    app.mainloop()
