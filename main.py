#!/usr/bin/env python3
import tcod

from engine import Engine
from entity import Entity
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

    tileset = tcod.tileset.load_tilesheet(
        "dejavu16x16_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', (255, 255, 255))
    npc = Entity(int(screen_width / 2), int(screen_height / 2 - 10), '@', (255, 255, 0))
    # int() because python3 doesn't truncate division by default and tcod needs int
    entities = {npc, player}

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        player=player
    )

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