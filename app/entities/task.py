class Task():
    def __init__(self, title, description, expiration_date, priority, user):
        self.__title = title
        self.__description = description
        self.__expiration_date = expiration_date
        self.__priority = priority
        self.__user = user

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def expiration_date(self):
        return self.expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        self.__expiration_date = expiration_date

    @property
    def priority(self):
        return self.priority

    @priority.setter
    def priority(self, priority):
        self.__priority = priority

    @property
    def priority(self):
        return self.user

    @priority.setter
    def priority(self, user):
        self.__user = user
