import pytest
from channels.testing import WebsocketCommunicator

from chatterino.chats.consumers import ChatConsumer


@pytest.mark.asyncio
async def test_chat_consumer_ws():
    communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), "")
    connected, subprotocol = await communicator.connect()
    assert connected
