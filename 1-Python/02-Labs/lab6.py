import curses

def main(stdscr):
    # Clear the screen and hide the cursor
    curses.curs_set(0)
    stdscr.clear()

    # Define the initial position of the cursor
    x, y = 0, 0

    # Loop until the user presses the 'q' key
    while True:
        # Move the cursor based on arrow key input
        c = stdscr.getch()
        if c == curses.KEY_UP:
            y = max(y - 1, 0)
        elif c == curses.KEY_DOWN:
            y = min(y + 1, curses.LINES - 1)
        elif c == curses.KEY_LEFT:
            x = max(x - 1, 0)
        elif c == curses.KEY_RIGHT:
            x = min(x + 1, curses.COLS - 1)

        # Clear the screen and redraw the cursor
        stdscr.clear()
        stdscr.addstr(y, x, "X")
        stdscr.refresh()

curses.wrapper(main)
