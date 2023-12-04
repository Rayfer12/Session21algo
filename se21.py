class Foodinnit:
    def __init__(self, item_name, amount_ordered):
        self._item_name = item_name
        self._amount_ordered = amount_ordered
        self._standard_price_per_pound = self._get_standard_price_per_pound()
        self._calculated_price = None

    def _get_standard_price_per_pound(self):
        if self._item_name == "Dry Cured Iberian Ham":
            return 177.80
        elif self._item_name == "Wagyu Steaks":
            return 450.00
        elif self._item_name == "Matsutake Mushrooms":
            return 272.00
        elif self._item_name == "Kopi Luwak Coffee":
            return 306.50
        elif self._item_name == "Moose Cheese":
            return 487.20
        elif self._item_name == "White Truffles":
            return 3600.00
        elif self._item_name == "Blue Fin Tuna":
            return 3603.00
        elif self._item_name == "Le Bonnotte Potatoes":
            return 270.81
        else:
            return 0

    def cost_of_ordered_food(self):
        self._calculated_price = self._amount_ordered * self._standard_price_per_pound
        return self._calculated_price