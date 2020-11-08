from parser import Parser
from bot import Bot
from config import Config


def create_dairy(cfg, bot, data):
    # Перебор списка инофрмации о предметах
    for el in data:
        # Добавляю список, который будет носить название предмета
        bot.add_list(idBoard=cfg.BOARD_ID, name_list=el['name_subject'])
        id_list = bot.get_lists(cfg.BOARD_ID).json()[0]['id']

        # Перебираю список преподов, так как по одному преподу их может быть несколько
        for proffesor in el['teachers']:
            # Создаю карточку, которая носит имя препода
            bot.create_card(list_id = id_list, name_card = '👤 '+proffesor['name'])
            id_card = bot.get_cards(id_list).json()[-1]['id']

            # Добавляю комментарий, в котором будет ссылка на расписание этого препода
            bot.add_comment(id_card=id_card, text=f"Расписание препода: {proffesor['url']}")

        # Создаю вторую карточку в списке, в которой будет находится план сдачи материала преподу
        bot.create_card(list_id = id_list, name_card = '📈 План')


def del_dairy(cfg, bot):
    for lst in bot.get_lists(cfg.BOARD_ID).json():
        bot.delete_list(lst['id'])


def main():
    # Подключение классов
    cfg = Config()
    p = Parser()
    bot = Bot(token=cfg.API_TOKEN, key=cfg.API_KEY)

    # Получение данных о предметах
    data = p.get_subjects_info(cfg.GROUP_ID)

    # Создание дневника
    create_dairy(cfg, bot, data)

    # Удаление дневника
    # del_dairy(cfg, bot)


if __name__ == '__main__':
    main()
