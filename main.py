#!/usr/bin/env python3
import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', (255, 255, 255))
    npc = Entity(int(screen_width / 2), int(screen_height / 2 - 10), '@', (255, 255, 0))
    # int() because python3 doesn't truncate division by default and tcod needs int
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="The Rogue @nt",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")  # "F" changes the default numpy order [y,x]

        while True:  # Starts the game loop
            engine.render(console=root_console, context=context)  # Draw, Updates and clean the screen

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()