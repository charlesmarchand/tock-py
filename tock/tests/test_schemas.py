# -*- coding: utf-8 -*-
import json
import unittest
from datetime import datetime
from unittest import TestCase

from tock.models import ConnectorType, Entity, EntityValue, EntityValueCandidate, Message, UserId, \
    User, RequestContext, PlayerType, Suggestion, I18nText, \
    Sentence, ResponseContext, BotRequest, BotResponse, \
    TockMessage, Card, Attachment, AttachmentType, Action, Carousel, \
    ClientConfiguration, StoryConfiguration
from tock.schemas import ConnectorTypeSchema, EntitySchema, EntityValueSchema, EntityValueCandidateSchema, MessageSchema, UserIdSchema, UserSchema, \
    RequestContextSchema, SuggestionSchema, I18NTextSchema, \
    ResponseContextSchema, BotRequestSchema, BotResponseSchema, TockMessageSchema, \
    CardSchema, SentenceSchema, AttachmentSchema, ActionSchema, CarouselSchema, ClientConfigurationSchema, \
    StoryConfigurationSchema


def given_bot_request() -> BotRequest:
    return BotRequest(
        intent="intent",
        entities=[
            Entity(
                type="type",
                role="role",
                evaluated=True,
                new=False,
                content="content",
                value=EntityValue(
                    type='type', 
                    value='value', 
                    candidates=EntityValueCandidate(
                        value='value', 
                        probability= 1.0
                    )
                )
            )
        ],
        message=Message(
            type="type",
            text="text"
        ),
        story_id="story_id",
        context=RequestContext(
            namespace="namespace",
            language="fr",
            connector_type=ConnectorType(
                id="id",
                user_interface_type="text"
            ),
            user_interface="text",
            application_id="application_id",
            user_id=UserId(
                id="id",
                type=PlayerType.USER
            ),
            bot_id=UserId(
                id="id",
                type=PlayerType.BOT
            ),
            user=User(
                timezone="timezone",
                locale="fr_FR",
                test=False
            )
        )
    )


def given_bot_response() -> BotResponse:
    return BotResponse(
        messages=[
            given_sentence(),
            given_card(),
            given_carousel()
        ],
        story_id="story_id",
        entities=[],
        context=ResponseContext(
            request_id="request_id",
            date=datetime(2020, 1, 1, 0, 0, 0)
        ),
        step="step"
    )


def given_i18n_text(text: str = "text") -> I18nText:
    return I18nText(
        text=text,
        args=["one", "two", "three"],
        to_be_translated=True,
        length=4,
        key="key"
    )


def given_sentence() -> Sentence:
    return Sentence(
        text=given_i18n_text(),
        suggestions=[
            given_suggestion("action1"),
            given_suggestion("action2")
        ],
        delay=0
    )


def given_attachment() -> Attachment:
    return Attachment(
        url="http://image.svg",
        type=AttachmentType.IMAGE
    )


def given_action() -> Action:
    return Action(
        title=given_i18n_text("action"),
        url="http://action.com"
    )


def given_card() -> Card:
    return Card.Builder() \
        .with_title(given_i18n_text()) \
        .with_sub_title(given_i18n_text()) \
        .with_attachment("http://image.svg", AttachmentType.IMAGE) \
        .add_action(given_i18n_text("action"), "http://action.com") \
        .with_delay(0) \
        .build()


def given_carousel() -> Carousel:
    return Carousel.Builder() \
        .add_card(given_card()) \
        .add_card(given_card()) \
        .add_card(given_card()) \
        .build()


def given_user_id(user_id: str = "id1") -> UserId:
    return UserId(
        id=user_id,
        type=PlayerType.USER,
        client_id="client_id"
    )


def given_entity() -> Entity:
    return Entity(
        type="type",
        role="role",
        evaluated=True,
        new=False,
        content="content",
        value=EntityValue(
                type='type', 
                value='value', 
                candidates=EntityValueCandidate(
                    value='value', 
                    probability= 1.0
                )
            )
    )


def given_user() -> User:
    return User(
        timezone="timezone",
        locale="fr_FR",
        test=False
    )


def given_response_context() -> ResponseContext:
    return ResponseContext(
        request_id="request_id",
        date=datetime(2020, 1, 1, 0, 0, 0)
    )


def given_suggestion(title: str = "action") -> Suggestion:
    return Suggestion(
        title=given_i18n_text(title)
    )


def given_message() -> Message:
    return Message(
        type="type",
        text="text"
    )


def given_connector_type() -> ConnectorType:
    return ConnectorType(
        id="id",
        user_interface_type="text"
    )


def given_request_context() -> RequestContext:
    return RequestContext(
        namespace="namespace",
        language="fr",
        connector_type=given_connector_type(),
        user_interface="text",
        application_id="application_id",
        user_id=given_user_id(),
        bot_id=given_user_id(),
        user=given_user()
    )


def given_tock_message() -> TockMessage:
    return TockMessage(
        request_id="request_id",
        bot_request=given_bot_request(),
        bot_response=given_bot_response()
    )


def given_story_configuration() -> StoryConfiguration:
    return StoryConfiguration(
        main_intent="main_intent",
        name="name",
        other_starter_intents=["secondary_intent_1", "secondary_intent_2"],
        secondary_intents=["other_start_intent_1", "other_start_intent_2"],
        steps=[]
    )

 
class TestEntitySchema(TestCase):
    def test_json_serialization(self):
        expected = given_entity()
        schema = EntitySchema()
        result = schema.load(json.loads(schema.dumps(expected)))
        self.assertEqual(expected, result)


class TestMessageSchema(TestCase):
    def test_json_serialization(self):
        expected = given_message()
        schema = MessageSchema()
        result: Message = schema.load(json.loads(schema.dumps(expected)))
        self.assertEqual(expected, result)


class TestConnectorTypeSchema(TestCase):
    def test_json_serialization(self):
        expected = given_connector_type()
        schema = ConnectorTypeSchema()
        result: ConnectorType = schema.load(json.loads(schema.dumps(expected)))
        self.assertEqual(expected, result)


class TestUserIdSchema(TestCase):
    def test_json_serialization(self):
        expected = given_user_id()
        schema = UserIdSchema()
        result: UserId = schema.load(json.loads(schema.dumps(expected)))
        self.assertEqual(expected, result)


class TestUserSchema(TestCase):
    def test_json_serialization(self):
        expected = given_user()
        schema = UserSchema()
        result: User = schema.load(json.loads(schema.dumps(expected)))
        self.assertEqual(expected, result)


class TestRequestContextSchema(TestCase):
    def test_json_serialization(self):
        expected = given_request_context()
        schema = RequestContextSchema()
        result: RequestContext = schema.load(json.loads(schema.dumps(expected)))
        self.assertEqual(expected, result)


class TestSuggestionSchema(TestCase):
    def test_json_serialization(self):
        expected = given_suggestion()
        schema = SuggestionSchema()
        result: Suggestion = schema.load(json.loads(schema.dumps(expected)))
        self.assertEqual(expected, result)


class TestI18nTextSchema(TestCase):
    def test_json_serialization(self):
        expected = given_i18n_text()
        schema = I18NTextSchema()
        result: I18nText = schema.load(json.loads(schema.dumps(expected)))
        self.assertEqual(expected, result)


class TestSentenceSchema(TestCase):
    def test_json_serialization(self):
        expected = given_sentence()
        schema = SentenceSchema()
        dumps = schema.dumps(expected)
        loads = json.loads(dumps)
        result: Sentence = schema.load(loads)
        self.assertEqual(expected, result)


class TestAttachmentSchema(TestCase):
    def test_json_serialization(self):
        expected = given_attachment()
        schema = AttachmentSchema()
        dumps = schema.dumps(expected)
        loads = json.loads(dumps)
        result: Attachment = schema.load(loads)
        self.assertEqual(expected, result)


class TestActionSchema(TestCase):
    def test_json_serialization(self):
        expected = given_action()
        schema = ActionSchema()
        result: Action = schema.load(json.loads(schema.dumps(expected)))
        self.assertEqual(expected, result)


class TestCardSchema(TestCase):
    def test_json_serialization(self):
        expected = given_card()
        schema = CardSchema()
        dumps = schema.dumps(expected)
        loads = json.loads(dumps)
        result: Card = schema.load(loads)
        self.assertEqual(expected, result)


class TestCarouselSchema(TestCase):
    def test_json_serialization(self):
        expected = given_carousel()
        schema = CarouselSchema()
        dumps = schema.dumps(expected)
        loads = json.loads(dumps)
        result: Carousel = schema.load(loads)
        self.assertEqual(expected, result)


class TestResponseContextSchema(TestCase):
    def test_json_serialization(self):
        expected = given_response_context()
        schema = ResponseContextSchema()
        dumps = schema.dumps(expected)
        loads = json.loads(dumps)
        result: Sentence = schema.load(loads)
        self.assertEqual(expected, result)


class TestBotRequestSchema(TestCase):
    def test_json_serialization(self):
        expected = given_bot_request()
        schema = BotRequestSchema()
        dumps = schema.dumps(expected)
        loads = json.loads(dumps)
        result: BotRequest = schema.load(loads)
        self.assertEqual(expected, result)


class TestBotResponseSchema(TestCase):
    def test_json_serialization(self):
        expected = given_bot_response()
        schema = BotResponseSchema()
        dumps = schema.dumps(expected)
        loads = json.loads(dumps)
        result: BotResponse = schema.load(loads)
        self.assertEqual(expected, result)


class TestTockMessageSchema(TestCase):
    def test_json_serialization(self):
        expected = given_tock_message()
        schema = TockMessageSchema()
        dumps = schema.dumps(expected)
        print(dumps)
        result: TockMessage = schema.load(json.loads(dumps))
        self.assertEqual(expected, result)


class TestStoryConfigurationSchema(TestCase):
    def test_json_serialization(self):
        expected = given_story_configuration()
        schema = StoryConfigurationSchema()
        result: TockMessage = schema.load(json.loads(schema.dumps(expected)))
        self.assertEqual(expected, result)


class TestClientConfigurationSchema(TestCase):
    def test_json_serialization(self):
        expected = ClientConfiguration(
            stories=[
                given_story_configuration()
            ]
        )
        schema = ClientConfigurationSchema()
        result: TockMessage = schema.load(json.loads(schema.dumps(expected)))
        self.assertEqual(expected, result)

    def test_payload(self):
        expected = '{"botRequest": {"intent": "greetings", "entities": [], "message": {"type": "text", "text": "yo"}, "storyId": "tock_unknown_story", "context": {"namespace": "elebescond", "language": "fr", "connectorType": {"id": "web", "userInterfaceType": "textChat"}, "userInterface": "textChat", "applicationId": "test-erwan_assistant", "userId": {"id": "test_5dcae4ec816a555b46a4857f_fr__sjniho739", "type": "user"}, "botId": {"id": "test_bot_5dcae4ec816a555b46a4857f_fr", "type": "bot"}, "user": {"timezone": "UTC", "locale": "fr", "test": false}}}, "requestId": "5f788c08c93772446f21d05f"}'
        schema = TockMessageSchema()
        loads: TockMessage = schema.loads(expected)
        result = schema.dumps(loads)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
