#!/usr/bin/env python3
import tcod


def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)  # int() because python3 doesn't truncate division by default and tcod needs int
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="The Rogue @nt",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")  # "F" changes the default numpy order [y,x]
        while True:  # Starts the game loop
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)  # Updates the screen

            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()


if __name__ == "__main__":
    main()