def get_all_members_mapper():
    return """
        select
            *
        from
            member m
            join level l on m.levelFK = l.id
            join degree d on m.degreeFK = d.id
        """


def get_member_mapper(id: int):
    return f"""
        select
            *
        from
            member m
            join level l on m.levelFK = l.id
            join degree d on m.degreeFK = d.id
        where
            m.id = {id}
    """
