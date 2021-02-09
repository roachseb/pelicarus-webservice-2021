class Organism_Response():
    def __init__(self, resources, pagination=None):
        self.resources = []
        for resource in resources:
            resource["donate_form"] = resource["donate-form"]
            del(resource["donate-form"])
            self.resources.append(Resource(**resource))
        self.pagination = Pagination(**pagination)

class Pagination():
    def __init__(self, page, max_page, results_per_page):
        self.page = page
        self.max_page = max_page
        self.results_per_page = results_per_page

class Resource():
    def __init__(self, id,name,slug,type,funding,supporters,logo,thumbnail,profile,donate_form):
        self.id=id
        self.name=name
        self.slug =slug 
        self.type =type 
        self.funding =funding 
        self.supporters=supporters
        self.logo =logo 
        self.thumbnail =thumbnail 
        self.profile =profile 
        self.donate_form =donate_form 