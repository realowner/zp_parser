from peewee import *
from .BaseModel import *

class CategoryModel(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=255)
    image = CharField(max_length=255)
    slug = CharField(max_length=255)
    icon = CharField(max_length=255)

    @staticmethod
    def create_category():
        
        row = CategoryModel(
            
        )
        row.save()

        return row

    class Meta():
        db_table = "category"
        order_by = ('id',)