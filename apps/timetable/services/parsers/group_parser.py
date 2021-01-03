import requests
from bs4 import BeautifulSoup


class GroupParser:
    def get_name_group(self, soup: BeautifulSoup):
        element = soup.find('h3', {'class': 'text-center'})
        if element:
            return element.text

    def parse_name_group(self, string: str) -> str:
        return string.split('"')[1]

    def get_group_by_id(self, id_group: int):
        html = requests.get(
            f'https://timetable.pallada.sibsau.ru/timetable/group/{id_group}'
        ).text

        soup = BeautifulSoup(html, 'html.parser')
        group = self.get_name_group(soup)

        if group:
            return id_group, self.parse_name_group(group)

    def get_groups(self):
        for group_id in range(15_000):
            group = self.get_group_by_id(group_id)
            if group:
                yield group
