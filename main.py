from parser import Parser
from bot import Bot
from config import Config


def main():
    cfg = Config()
    p = Parser()
    bot = Bot(token=cfg.API_TOKEN, key=cfg.API_KEY)
    
    # list_id = '5fa56083506a4d34d2218e0d'

    # Генерация дневника
    for name_sub in p.get_all_names_subjects(cfg.GROUP_ID):
        bot.add_list(idBoard=cfg.BOARD_ID, name_list=name_sub)
    
    # Удаление дневника
    for lst in bot.get_lists(cfg.BOARD_ID).json():
        bot.delete_list(lst['id'])


if __name__ == '__main__':
    main()
