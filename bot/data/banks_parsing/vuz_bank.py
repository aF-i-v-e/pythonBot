from bot.data import contribution


class VuzBank1:
    url = 'https://www.vuzbank.ru/chastnym-klientam/vklady/horoshiy-start'
    contribution = contribution.Contribution()

    def get_contribution(self):
        return self.contribution
