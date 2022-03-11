from neomodel import (
    StructuredNode,
    StringProperty,
    Relationship,
    config,
    UniqueIdProperty,
    FloatProperty,
    StructuredRel
)
import os
config.DATABASE_URL = os.environ['NEO4J_URI'].format(
    os.environ['NEO4J_USER'],
    os.environ['NEO4J_PASSWORD']
)


class CityConnection(StructuredRel):
    km_rect = FloatProperty()
    km_driving= FloatProperty()
    travel_time = FloatProperty()

class City(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True,required=True)
    state = StringProperty(required=True)
    connects_with = Relationship('City', 'CONNECTS_WITH',model=CityConnection)
    latitude =FloatProperty(required=True)
    longitude =FloatProperty(required=True)


