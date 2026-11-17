"""Module implementing a PostOffice class for sending, reading, and searching
messages."""

from collections.abc import Iterable
from typing import Any, Optional


class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (Iterable[str]): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental ID of the last message sent.
        boxes (dict[str, list[dict[str, Any]]]): Users' inboxes.
    """

    def __init__(self, usernames: Iterable[str]) -> None:
        self.message_id: int = 0
        self.boxes: dict[str, list[dict[str, Any]]] = {
            user: [] for user in usernames
        }

    def send_message(
            self,
            sender: str,
            recipient: str,
            message_body: str,
            urgent: bool = False,
            title: str = "",
    ) -> int:
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                Urgent messages appear first. Defaults to False.
            title (str, optional): The title of the message. Defaults to "".

        Returns:
            int: The message ID, auto-incremented number.

        Raises:
            KeyError: If the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details: dict[str, Any] = {
            "id": self.message_id,
            "title": title,
            "body": message_body,
            "sender": sender,
            "read": False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(
            self, username: str, num_of_messages: Optional[int] = None
    ) -> list[dict[str, Any]]:
        """Return unread messages from a user's inbox and mark them as read.

        Args:
            username (str): The username whose inbox should be read.
            num_of_messages (int, optional): Maximum number of unread messages
                to return. If None, returns all unread messages.

        Returns:
            list[dict[str, Any]]: The requested unread message dictionaries.

        Raises:
            KeyError: If the username does not exist.
            ValueError: If num_of_messages is negative.
        """
        if num_of_messages is not None and num_of_messages < 0:
            raise ValueError("num_of_messages must be non-negative.")

        unread_messages = [
            message for message in self.boxes[username] if not message["read"]
        ]
        messages_to_read = (
            unread_messages
            if num_of_messages is None
            else unread_messages[:num_of_messages]
        )

        for message in messages_to_read:
            message["read"] = True

        return messages_to_read

    def search_inbox(
            self, username: str, query: str
    ) -> list[dict[str, Any]]:
        """Search a user's inbox for messages containing a substring in title
        or body.

        Args:
            username (str): The username whose inbox should be searched.
            query (str): Substring to search for in message titles or bodies.

        Returns:
            list[dict[str, Any]]: All matching message dictionaries in the
            inbox.

        Raises:
            KeyError: If the username does not exist.
        """
        return [
            message
            for message in self.boxes[username]
            if query in message["title"] or query in message["body"]
        ]


def show_example() -> None:
    """Demonstrate sending, reading, and searching messages in PostOffice."""
    users = ("Newman", "Mr. Peanutbutter")
    post_office = PostOffice(users)
    post_office.send_message(
        sender="Mr. Peanutbutter",
        recipient="Newman",
        message_body="Hello, Newman.",
        title="Greeting",
    )
    print("Read messages:", post_office.read_inbox("Newman", 1))
    print("Search results:", post_office.search_inbox("Newman", "Hello"))


if __name__ == "__main__":
    show_example()
