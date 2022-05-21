from bot.business_logic.logic_utils.divide_contributions import identify_suitable_contributions
from bot.data.contributions_manager import Parsing


def get_month_count_from_contributions(user_input):
    parsing = Parsing()
    contributions = parsing.get_list_contributions()
    suitable_contributions = identify_suitable_contributions(contributions, user_input)
    return list(map(lambda contribution: contribution.get_months_number(), suitable_contributions))
