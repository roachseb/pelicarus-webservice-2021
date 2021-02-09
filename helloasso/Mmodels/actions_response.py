
class Action_Response():
    def __init__(self, resources, pagination=None):

        self.resources = [Resource(**x) for x in resources]
        self.pagination = Pagination(**pagination)


class Resource():
    def __init__(self, amount, custom_infos, date, email, id,
                 id_campaign, id_organism, status, type,
                 first_name=None, last_name=None, id_payment=None, option_label=None):
        self.id = id
        self.id_campaign = id_campaign
        self.id_organism = id_organism
        self.id_payment = id_payment
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.date = date
        self.status = status
        self.option_label = option_label
        self.type = type
        self.amount = amount
        self.custom_infos = [Custom_info(**x) for x in custom_infos]


class Pagination():
    def __init__(self, page, max_page, results_per_page):
        self.page = page
        self.max_page = max_page
        self.results_per_page = results_per_page


class Custom_info():
    def __init__(self, label, value):
        self.label = label
        self.value = value
