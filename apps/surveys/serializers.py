def SurveysSeializers(surveys):
    result = []
    for survey in surveys:
        result.append({
            'id': survey.id,
            'name': survey.name,
            'date_to': survey.date_to
        })
    return result
