import datetime


def log_path(log_path):
    def logger(old_fu):
        def new_fu(*args, **kwargs):
            to_log = old_fu(*args, **kwargs)
            args = f"{locals().get('args')} {locals().get('kwargs')}"
            log_info = [
                f'Время запуска: {datetime.datetime.now()}',
                f'Имя функции: {old_fu.__name__}',
                f'Аргументы: {args}',
                f'Результат: {to_log}\n'
            ]
            with open(str(log_path), "a", encoding='utf-8') as f:
                f.write('\n'.join(log_info))
        return new_fu
    return logger
# ===================================================================


class Contact:
    def __init__(self, f_name, l_name, phone, *args, **kwargs):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.favorite = None
        self.additional_info = []
        for favorite in args:
            self.favorite = favorite
        for add_info_name, add_info_value in kwargs.items():
            self.additional_info.append(f'{add_info_name}: {add_info_value}')
        self.list_adds = '\n'.join(self.additional_info)

    def __str__(self):
        return f'Имя: {self.f_name}\n' \
               f'Фамилия: {self.l_name}\n' \
               f'Телефон: {self.phone}\n' \
               f'В избранных: {self.favorite}\n' \
               f'Дополнительная информация:\n{self.list_adds}'


class PhoneBook:
    def __init__(self, name):
        self.book_name = name
        self.contacts = []

    @log_path("log.txt")
    def print_contacts(self):
        for i in self.contacts:
            print('===========')
            print(i)
        pass

    @log_path("log.txt")
    def add_contact(self, f_name, l_name, phone, *args, **kwargs):
        contact = Contact(f_name, l_name, phone, *args, **kwargs)
        self.contacts.append(contact)
        pass


MyPhoneBook = PhoneBook("Черная Книжечка")

if __name__ == '__main__':
    MyPhoneBook.add_contact('John', 'Smith', '+71234567809', 'да', telegram='@johny', email='johny@smith.com')
    MyPhoneBook.print_contacts()