from peewee import *
from .BaseModel import *

class IdGeoRelationModel(BaseModel):
    id = PrimaryKeyField(null=False)
    id_api_geo = IntegerField()
    id_geo = IntegerField()
    name = CharField(max_length=50)

    @staticmethod
    def create_geo_relation(api_geo, db_geo, name):
        
        row = IdGeoRelationModel(
            id_api_geo = api_geo,
            id_geo = db_geo,
            name = name,
        )
        row.save()

        return row

    class Meta():
        db_table = "id_geo_relation"
        order_by = ('id_geo',)