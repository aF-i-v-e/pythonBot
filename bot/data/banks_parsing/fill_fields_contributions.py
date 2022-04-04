class FillFiledContributions:
    def __init__(self, obj):
        obj.contribution.set_contribution_percentage(obj.get_contribution_percentage())
        obj.contribution.set_contribution_minimum_amount(obj.get_contribution_minimum_amount())
        obj.contribution.set_contribution_term(obj.get_contribution_term())
        obj.contribution.set_replenishment_in_process(obj.get_replenishment_in_process())
        obj.contribution.set_bank_name(obj.get_bank_name())
        obj.contribution.set_contribution_name(obj.get_contribution_name())
        obj.contribution.set_service_price(obj.get_service_price())
