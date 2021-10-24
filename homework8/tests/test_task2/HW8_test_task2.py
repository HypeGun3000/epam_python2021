from homework8.task2.first_sql_task import TableData


class TestDB:
    presidents = TableData(database_name='example.sqlite',
                           table_name='presidents')

    def test_len_presidents(self):
        assert len(self.presidents) == 3

    def test_call_president(self):
        assert self.presidents['Yeltsin'] == ('Yeltsin', 999, 'Russia')

    def test_call_president_second(self):
        assert self.presidents['Trump'] == ('Trump', 1337, 'US')

    def test_check_for_president_in_presidents(self):
        assert 'Yeltsin' in self.presidents

    def test_check_for_president_not_in_presidents(self):
        assert 'Putin' not in self.presidents

    def test_iteration_of_presidents_column_name(self):
        count_of_all_presidents = []
        for president in self.presidents:
            print(president['name'])
        assert len(count_of_all_presidents) == 3
