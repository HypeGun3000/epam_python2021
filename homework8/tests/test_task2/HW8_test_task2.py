from homework8.task2.first_sql_task import TableData


class TestDB:
    presidents = TableData(database_name='example.sqlite', table_name='presidents')

    def test_data_fetchall(self):
        assert self.presidents.data == [('Yeltsin', 999, 'Russia'),
                                        ('Trump', 1337, 'US'),
                                        ('Big Man Tyrone', 101,
                                         'Kekistan')]

    def test_len_presidents(self):
        assert len(self.presidents) == 3

    def test_call_president(self):
        assert self.presidents['Yeltsin'] == ('Yeltsin', 999, 'Russia')

    def test_check_for_president_in_presidents(self):
        assert 'Yeltsin' in self.presidents

    def test_check_for_president_not_in_presidents(self):
        assert not 'Putin' in self.presidents

    def test_iteration_of_presidents_column_name(self):
        count_of_all_presidents = []
        for president in self.presidents:
            count_of_all_presidents.append(president['name'])
        assert len(count_of_all_presidents) == 3
