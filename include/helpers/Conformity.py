
class Conformity:

    def employment_type(self, received_id):

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
            appropriate_id = None

        return appropriate_id

    def work_experience(self, received_id):
        
        if received_id == 3000:
            appropriate_id = 0
        elif received_id == 3001:
            appropriate_id = 0
        elif received_id == 3002:
            appropriate_id = 1
        elif received_id == 3003:
            appropriate_id = 2
        elif received_id == 3004:
            appropriate_id = 3
        else:
            appropriate_id = None

        return appropriate_id

