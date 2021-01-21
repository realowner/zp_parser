from peewee import *
from .BaseModel import *

# class GeobaseModel(BaseModel):
#     id = PrimaryKeyField(null=False)
#     name = CharField(max_length=50, null=False)
#     status = IntegerField(default=1)
#     country_id = IntegerField(default=None)

#     @staticmethod
#     def create_geobase_item():
        
#         row = GeobaseModel(
            
#         )
#         row.save()

#         return row

#     class Meta():
#         db_table = "geobase_region"
#         order_by = ('id',)

class GeobaseModel(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=50, null=False)
    prepositional = CharField(max_length=255)
    image = CharField(max_length=255)
    region_id = IntegerField()
    status =IntegerField()
    slug = CharField(max_length=255)
    meta_title = CharField(max_length=255)

    @staticmethod
    def create_geobase_item():

        row = GeobaseModel(

        )
        row.save()

        return row

    class Meta():
        db_table = "geobase_city"
        order_by = ('id',)