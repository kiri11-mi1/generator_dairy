from bs4 import BeautifulSoup
import requests
import re


class Parser:
    '''Парсер расписания СибГУ'''

    def get_day_timetable(self, numb_week, day, id):
        response = requests.get(
            f'https://timetable.pallada.sibsau.ru/timetable/group/{id}'
        ).text
        soup = BeautifulSoup(response, 'html.parser')
        return soup.select(f'#week_{numb_week}_tab > div.day.{day} > div.body')


    def is_weekend(self, day_timetable):
        return len(day_timetable) == 0


    def get_subjects(self, line):
        div_row = line.find('div', {'class': 'row'})
        return div_row.find_all('div')


    def get_name_subjects(self, line):
        result = []
        for sub_subject in self.get_subjects(line):
            name = sub_subject.find('span', {'class': 'name'}).text
            result.append(name)
        return result


    def get_all_names_subjects(self, id):
        subjects = []
        for numb_week in range(1, 3):
            for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
                day_timetable = self.get_day_timetable(numb_week, day, id)
                if self.is_weekend(day_timetable):
                    continue
                
                for line in day_timetable[0].find_all('div', {'class': 'line'}):
                    for sub in self.get_name_subjects(line):
                        subjects.append(sub.capitalize())
        return set(subjects)
