from db.utils import Database
def create_city(tx, city):
    d = tx.run('''CREATE (c:City {name: $name,state:$state,latitude: $latitude,longitude:$longitude})
              RETURN c.name''',
               {'name':city.name, 'state':city.state,
                'latitude':city.latitude,'longitude':city.longitude}
           )
    d = d.single()
    return d

def query(tx,name,state):

    q = 'Match(c:City{name:$name,state:$state}) return c'

    tx.run(q,{'name':name,'state':state})


class CityConnection():
    def __init__(self,km_rect=None,km_driving=None,travel_time=None):
        self.km_rect=km_rect
        self.km_driving= km_driving
        self.travel_time = travel_time

class City():
    def __init__(self,name=None,state=None,latitude=None,longitude=None):
        self.name = name
        self.state = state
        self.latitude =latitude
        self.longitude =longitude

    def save(self,driver=None):
        if not driver:
            driver = Database().driver
        with driver.session() as session:
            return session.write_transaction(create_city,self)


    @classmethod
    def search(cls,city_instance,driver=None):
        if not driver:
            driver = Database().driver
        with driver.session() as session:
            return session.read_transaction(query,city_instance.name,city_instance.state)





