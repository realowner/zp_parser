from peewee import *
from .BaseModel import *

class IdCategoryRelationModel(BaseModel):
    id = PrimaryKeyField(null=False)
    id_api_category = IntegerField()
    id_category = IntegerField()
    name = CharField(max_length=50)

    @staticmethod
    def create_category_relation(api_category, db_category, name):
        
        row = IdCategoryRelationModel(
            id_api_category = api_category,
            id_category = db_category,
            name = name,
        )
        row.save()

        return row

    class Meta():
        db_table = "id_category_relation"
        order_by = ('id_category',)