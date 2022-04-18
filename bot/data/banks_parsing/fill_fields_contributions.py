class FillFiledContributions:
    def __init__(self, obj):
        obj.contribution.set_start_sum(obj.get_start_sum())
        obj.contribution.set_bank_name(obj.get_bank_name())
        obj.contribution.set_contribution_name(obj.get_contribution_name())
        obj.contribution.set_package_services_price(obj.get_package_services_price())

