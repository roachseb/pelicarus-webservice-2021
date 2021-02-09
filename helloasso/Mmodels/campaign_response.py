class Campaign_Response():
    def __init__(self, resources, pagination=None):
        self.resources=[Resource(**resource) for resource in resources]
        self.pagination = Pagination(**pagination)
    def __str__(self):
        return self.__dict__.__str__()+'\n'
class Pagination():
    def __init__(self, page, max_page, results_per_page):
        self.page = page
        self.max_page = max_page
        self.results_per_page = results_per_page
    def __str__(self):
        return self.__dict__.__str__()+'\n'


class Resource():
    def __init__(self, 
                id=None,
                name=None,
                slug=None,
                type=None,
                state=None,
                funding=None,
                supporters=None,
                creation_date=None,
                last_update=None,
                url=None,
                id_organism=None,
                slug_organism=None,
                place_address=None,
                place_city=None,
                place_country=None,
                place_name=None,
                place_zipcode=None,
                end_date=None,
                start_date=None
                ):
        self.id = id
        self.name = name
        self.slug = slug
        self.type = type
        self.state = state
        self.funding = funding
        self.supporters = supporters
        self.creation_date = creation_date
        self.last_update = last_update
        self.url = url
        self.id_organism = id_organism
        self.slug_organism = slug_organism
        self.place_name = place_name
        self.place_address = place_address
        self.place_city = place_city
        self.place_zipcode = place_zipcode
        self.place_country = place_country
        self.end_date=end_date
        self.start_date=start_date
    def __str__(self):
        return self.__dict__.__str__()+'\n'
    def __repr__(self):
        return self.__dict__.__str__()