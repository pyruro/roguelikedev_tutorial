#!/usr/bin/env python3
import copy

import tcod

from engine import Engine
import entity_factories
from game_map import GameMap
from input_handlers import EventHandler
from procgen import generate_dungeon


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        "dejavu16x16_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = copy.deepcopy(entity_factories.player)
    # int() because python3 doesn't truncate division by default and tcod needs int

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        player=player
    )

    engine = Engine(event_handler=event_handler, game_map=game_map, player=player)

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