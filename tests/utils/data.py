import datetime


def create_test_data():
    test_data = []

    from backend.models.topic import Topic  # pylint: disable=import-error
    test_data.extend([
        Topic(id=1, name='Weight tracking', contextTitle=None,
              supportedUnit='kg', combinationOperation='avg'),
        Topic(id=2, name='Food spending', contextTitle='Food name',
              supportedUnit='HUF', combinationOperation='sum'),
        Topic(id=3, name='Activity', contextTitle='Activity name',
              supportedUnit='min', combinationOperation='sum'),
    ])

    from backend.models.numericEntry import NumericEntry  # pylint: disable=import-error
    test_data.extend([
        NumericEntry(id=1, topic_id=1, context=None,
                     value=85, date=datetime.datetime.now()),
        NumericEntry(id=2, topic_id=1, context=None,
                     value=87, date=datetime.datetime.now()),
        NumericEntry(id=3, topic_id=2, context='Bananas 400g',
                     value=300, date=datetime.datetime.now()),
        NumericEntry(id=4, topic_id=2, context='Kefir 2x',
                     value=800, date=datetime.datetime.now()),
        NumericEntry(id=5, topic_id=3, context='Workout',
                     value=75, date=datetime.datetime.now()),
    ])

    return test_data
