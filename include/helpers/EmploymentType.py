
class EmploymentType:

    def conformity(self, received_id):

        if received_id == 309:
            appropriate_id = 2
        elif received_id == 310:
            appropriate_id = 4
        elif received_id == 462:
            appropriate_id = 5
        elif received_id == 312:
            appropriate_id = 6
        elif received_id == 311:
            appropriate_id = 7
        else:
            appropriate_id = 0

        return appropriate_id