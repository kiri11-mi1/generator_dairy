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


    def get_teachers(self, line):
        result = []
        for sub_subject in self.get_subjects(line):
            result.append(sub_subject.find('a').text)
        return result
    
    
    def get_proffesor_url(self, line):
        result = []
        for sub_subject in self.get_subjects(line):
            result.append(sub_subject.find('a')['href'])
        return result


    def merge_similar_subjects(self, subjects):
        for i in range(len(subjects)):
            for j in range(len(subjects)):
                if subjects[i]['name_subject'] == subjects[j]['name_subject'] and i != j:
                    subjects[i]['teachers'].append(subjects[j]['teachers'][0])
        return self.delete_repeat_subjects(subjects)


    def delete_repeat_proffesors(self, proffesors):
        used = []
        for p in proffesors:
            if p not in used:
                used.append(p)
        return used


    def delete_repeat_subjects(self, subjects):
        used = []
        for sub in subjects:
            sub['teachers'] = self.delete_repeat_proffesors(
                                    sorted(sub['teachers'], key=lambda k: k['name']))
            if sub not in used:
                used.append(sub)
        return used
        

    def get_subjects_info(self, id):
        subjects = []
        for numb_week in range(1, 3):
            for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
                day_timetable = self.get_day_timetable(numb_week, day, id)
                if self.is_weekend(day_timetable):
                    continue
                
                for line in day_timetable[0].find_all('div', {'class': 'line'}):
                    for name_sub, name_prof, url in zip(self.get_name_subjects(line),
                                                   self.get_teachers(line),
                                                   self.get_proffesor_url(line)):
                        subjects.append({
                            'name_subject': name_sub.capitalize(),
                            'teachers': [{
                                'name': name_prof,
                                'url': 'https://timetable.pallada.sibsau.ru' + url
                            }]
                        })
        return self.merge_similar_subjects(subjects)
