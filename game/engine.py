from __future__ import annotations

import random

import game.entity
import game.game_map


class Engine:
    """
    The Engine class is missing its constructor method __init__ which will normally be defined in all other classes.
    It is excluded here because the objects held by Engine will need Engine to already exist for they can be created
    """
    game_map: game.game_map.GameMap
    player: game.entity.Entity
    rng: random.Random

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()
