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
    whereClause_id = ""

    if id is not None:
        whereClause_id = f"and m.id = {id}"

    return f"""
        select
            *
        from
            member m
            join level l on m.levelFK = l.id
            join degree d on m.degreeFK = d.id
        where
            1 = 1
            {whereClause_id}
        """
