from bot.business_logic.find_best_contribution import find_best_contribution
from bot.data.contributions_manager import Parsing
from bot.response.bot_response_constants import BotResponseConstants


def create_response_with_contribution(user_input):
    parsing = Parsing()
    contributions = parsing.get_list_contributions()
    user_output = find_best_contribution(contributions, user_input)
    if user_output is None:
        return user_input.get_string_representation() + BotResponseConstants.sorry_response
    return user_output.get_string_representation()
