import datetime
import json
import hashlib


def log_path(log_path):
    def logger(old_fu):
        def new_fu(*args, **kwargs):
            to_log = old_fu(*args, **kwargs)
            args = locals().get('args')
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


@log_path("log.txt")
def generate_pairs(path):
    country_list = []
    with open(path, encoding="utf-8") as data:
        json_data = json.load(data)
        for country in json_data:
            country_list += country['translations']['rus']['common'].split('%')
    countries = iter(country_list)
    counter = 0
    while counter < 250:
        country = countries.__next__()
        pair = f'{country} - https://ru.wikipedia.org/wiki/{country.replace(" ", "_")}\n'
        with open('country pairs.txt', "a", encoding='utf-8') as f:
            f.write(str(pair))
        counter += 1
        yield pair


if __name__ == "__main__":
    for pair in generate_pairs('countries.json'):
        print(hashlib.md5(pair.encode('utf-8')).hexdigest())