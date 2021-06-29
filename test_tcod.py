#!/usr/bin/env python3
# Make sure 'dejavu10x10_gs_tc.png' is in the same directory as this script.
import tcod

WIDTH, HEIGHT = 80, 60  # Console width and height in tiles.


def main() -> None:
    """Script entry point."""
    # Load the font, a 32 by 8 tile font with libtcod's old character layout.
    tileset = tcod.tileset.load_tilesheet(
        "arial10x10.png", 32, 8, tcod.tileset.CHARMAP_TCOD,
    )
    # Create the main console.
    console = tcod.Console(WIDTH, HEIGHT, order="F")
    # Create a window based on this console and tileset.
    with tcod.context.new(  # New window for a console of size columns×rows.
        columns=console.width, rows=console.height, tileset=tileset,
    ) as context:
        while True:  # Main loop, runs until SystemExit is raised.
            console.clear()
            console.print(x=0, y=0, string="Hello World!")
            context.present(console)  # Show the console.

            for event in tcod.event.wait():
                context.convert_event(event)  # Sets tile coordinates for mouse events.
                print(event)  # Print event information to stdout.
                if event.type == "QUIT":
                    raise SystemExit()
        # The window will be closed after the above with-block exits.


if __name__ == "__main__":
    main()