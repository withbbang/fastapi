name = "test"


def add_test_mapper(id: int):
    return f"""
        insert into test (id, name) values ({id}, '{name}')
        """
