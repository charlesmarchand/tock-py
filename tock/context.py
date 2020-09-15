# -*- coding: utf-8 -*-
from re import split
from typing import List, Optional, Type

from intent import Intent
from tock.models import Entity, UserId


class Context:

    def __init__(self, user_id: UserId):
        self.__current_story: Optional[Type] = None
        self.__previous_intent: Optional[Intent] = None
        self.__entities = []
        self.__user_id: UserId = user_id

    def entity(self, entity_type: str) -> Optional[Entity]:
        for entity in reversed(self.entities):
            parts = split(':', entity.type)
            parts.reverse()
            if parts[0] == entity_type:
                return entity

    @property
    def current_story(self):
        return self.__current_story

    @current_story.setter
    def current_story(self, story: Type):
        self.__current_story = story

    @property
    def previous_intent(self):
        return self.__previous_intent

    @previous_intent.setter
    def previous_intent(self, intent: Intent):
        self.__previous_intent = intent

    @property
    def user_id(self):
        return self.__user_id

    def add_entities(self, entities: List[Entity]):
        self.__entities = self.__entities + entities

    @property
    def entities(self):
        return self.__entities


class Contexts:

    def __init__(self):
        self.__contexts: List[Context] = []

    def getcontext(self, user_id: UserId) -> Context:
        for context in self.__contexts:
            if context.user_id == user_id:
                return context

    def registercontext(self, context: Context):
        self.__contexts.append(context)
