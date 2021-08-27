from api_pallada import API
from typing import Optional


def get_marks(api: API) -> list:
    tmp_result = dict()

    tmp = api.search_read(
        'portfolio_science.grade_view',
        [[['ID_student', '!=', '']]],
        {'fields': ['discipline', 'grade', 'term', 'test_type', 'coursework_theme']},
    )

    for discipline in tmp:
        if not discipline['discipline']:
            continue
        item = {
            'name': discipline['discipline'].strip(),
            'coursework': discipline.get('coursework_theme'),
            'mark': discipline['grade'].strip(),
            'type': discipline['test_type'].strip(),
        }
        # Артем просил, чтоб прилетало не false, как это возвращает паллада, а null
        item['coursework'] = item['coursework'] if item['coursework'] else None
        term = discipline['term'].strip()
        if term in tmp_result:
            tmp_result[term].append(item)
        else:
            tmp_result[term] = [item]

    result = []
    for term in sorted(tmp_result.keys()):
        result.append({
            'term': term,
            'items': sorted(tmp_result[term], key=lambda x: x['type']),
        })
    return result


def get_attestation(api) -> list:
    result = []
    tmp = api.search_read(
        'portfolio_science.grade_attistation_view',
        [[['nzkn', '=', api.login]]],
        {'fields': ['dis', 'forma', 'att1', 'att2', 'att3', 'att']},
    )

    for att in tmp:
        att1 = att['att1'].split('/')[0].strip() if att.get('att1') else '-'
        att2 = att['att2'].split('/')[0].strip() if att.get('att2') else '-'
        att3 = att['att3'].split('/')[0].strip() if att.get('att3') else '-'
        att_res = att['att'].split('/')[0].strip() if att.get('att') else '-'
        forma = att['forma'].strip() if isinstance(att['forma'], str) else '-'
        result.append({
            'name': att['dis'].strip(),
            'type': forma,
            'att1': att1,
            'att2': att2,
            'att3': att3,
            'att': att_res,
        })
    return result


def get_gradebook(api: API) -> Optional[str]:
    response = api.search_read(
        'portfolio_science.grade_attistation_view',
        [[['nzkn', '!=', '']]],
        {'limit': 10},
    )
    if not len(response):
        return None
    for i in response:
        if nzkn := i.get('nzkn'):
            return nzkn


def get_fio_group_and_average(api: API) -> tuple:
    tmp = api.search_read(
        'portfolio_science.grade_view',
        [[['ID_student', '!=', '']]],
        {'fields': ['ID_student', 'display_name', 'grade']},
    )

    average = 0
    count = 0

    if not tmp:
        return '-', '-', 0

    for i in tmp:
        if not i['grade'][0].isdigit():
            continue
        average += int(i['grade'][0])
        count += 1

    if count:
        average = round(average / count, 2)
    else:
        average = 0

    return tmp[0]['ID_student'], tmp[0]['display_name'], average
