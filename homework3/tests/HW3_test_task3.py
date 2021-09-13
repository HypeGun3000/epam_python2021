from homework3.task3.func_fix import make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    }
]


def test_true_data():
    assert make_filter(name="polly", type="bird").apply(sample_data) \
           == [{'is_dead': True, 'kind': 'parrot',
                'type': 'bird', 'name': 'polly'}]


def test_failed_data():
    assert make_filter(name='Johanson', is_dead=False).apply(sample_data) == []
