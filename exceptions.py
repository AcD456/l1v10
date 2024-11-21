class MessengerException(Exception):
    """Базовый класс для всех исключений в Messenger."""
    pass

class UserAlreadyExistsException(MessengerException):
    """Ошибка, когда пользователь с таким именем уже существует."""
    def __init__(self, username):
        self.username = username
        self.message = f"Пользователь с именем '{self.username}' уже существует."
        super().__init__(self.message)

class UserNotFoundException(MessengerException):
    """Ошибка, когда пользователь не найден."""
    def __init__(self, username):
        self.username = username
        self.message = f"Пользователь с именем '{self.username}' не найден."
        super().__init__(self.message)

class ChatNotFoundException(MessengerException):
    """Ошибка, когда чат с указанным ID не найден."""
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.message = f"Чат с ID {self.chat_id} не существует."
        super().__init__(self.message)

class ParticipantNotFoundException(MessengerException):
    """Ошибка, когда участник не найден в чате."""
    def __init__(self, sender, chat_id):
        self.sender = sender
        self.chat_id = chat_id
        self.message = f"Пользователь {self.sender} не является участником чата {self.chat_id}."
        super().__init__(self.message)

class ContactNotFoundException(MessengerException):
    """Ошибка, когда контакт не найден в списке контактов."""
    def __init__(self, contact_name):
        self.contact_name = contact_name
        self.message = f"Контакт {self.contact_name} не найден."
        super().__init__(self.message)