import datetime


def create_test_data():
    test_data = []

    from backend.models.topic import Topic  # pylint: disable=import-error
    test_data.extend([
        Topic(id=1,
              name='Weight tracking',
              question=None,
              supportedUnit='kg',
              combinationOperation='avg',
              last_updated=_create_datetime(minute=30)),
        Topic(id=2,
              name='Food spending',
              question='What food was purchased?',
              supportedUnit='HUF',
              combinationOperation='sum',
              last_updated=_create_datetime(minute=35)),
        Topic(id=3,
              name='Activity',
              question='What activity was done?',
              supportedUnit='min',
              combinationOperation='sum',
              last_updated=_create_datetime(minute=33)),
    ])

    from backend.models.numericEntry import NumericEntry  # pylint: disable=import-error
    test_data.extend([
        NumericEntry(id=1,
                     topic_id=1,
                     answer=None,
                     value=85,
                     date=datetime.datetime.now(),
                     last_updated=_create_datetime(minute=20)),
        NumericEntry(id=2,
                     topic_id=1,
                     answer=None,
                     value=87,
                     date=datetime.datetime.now(),
                     last_updated=_create_datetime(minute=22)),
        NumericEntry(id=3,
                     topic_id=2,
                     answer='Bananas 400g',
                     value=300,
                     date=datetime.datetime.now(),
                     last_updated=_create_datetime(minute=21)),
        NumericEntry(id=4,
                     topic_id=2,
                     answer='Kefir 2x',
                     value=800,
                     date=datetime.datetime.now(),
                     last_updated=_create_datetime(minute=28)),
        NumericEntry(id=5,
                     topic_id=3,
                     answer='Workout',
                     value=75,
                     date=datetime.datetime.now(),
                     last_updated=_create_datetime(minute=23)),
    ])

    return test_data


def _create_datetime(minute=30):
    return datetime.datetime(year=2022, month=11, day=15, hour=5, minute=minute)
