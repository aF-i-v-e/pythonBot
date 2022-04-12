import copy


class FillFiledContributions:
    def __init__(self, obj):
        obj.contribution.set_percent(obj.get_percent())
        obj.contribution.set_start_sum(obj.get_start_sum())
        obj.contribution.set_replenishment_in_process(obj.get_replenishment_in_process())
        obj.contribution.set_bank_name(obj.get_bank_name())
        obj.contribution.set_contribution_name(obj.get_contribution_name())
        obj.contribution.set_package_services_price(obj.get_package_services_price())

        months_number_list = obj.get_months_number()
        for months_number in months_number_list:
            contribution = copy.deepcopy(obj.contribution)
            contribution.set_months_number(months_number)
            obj.contributions.append(contribution)
