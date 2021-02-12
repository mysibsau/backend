from api_pallada import API


def get_gradebook(api: API):
    return api.search_read(
        'portfolio_science.grade_attistation_view',
        [[['nzkn', '!=', '']]],
        {'limit': 1},
    )[0]['nzkn']


def get_fio_group_and_average(api: API):
    tmp = api.search_read(
        'portfolio_science.grade_view',
        [[['ID_student', '!=', '']]],
        {'fields': ['ID_student', 'display_name', 'grade']},
    )

    average = 0
    count = 0

    for i in tmp:
        if not i['grade'][0].isdigit():
            continue
        average += int(i['grade'][0])
        count += 1

    average = round(average / count, 2)

    return tmp[0]['ID_student'], tmp[0]['display_name'], average
