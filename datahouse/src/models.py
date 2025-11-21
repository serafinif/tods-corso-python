from dataclasses import dataclass

@dataclass
class House:
    price: float
    bedrooms: int
    bathrooms: float
    sqft_living: float
    sqft_lot: float
    floors: float
    waterfront: int
    view: int
    condition: int
    grade: int
    yr_built: int
    yr_renovated: int
    zipcode: int

    @property
    def price_per_sqm(self):
        """Ritorna prezzo per mq (1 mq = 10.764 piedi²)."""
        if self.sqft_living == 0:
            return 0
        return self.price / (self.sqft_living / 10.764)

    def is_modern(self):
        """True se costruita o ristrutturata dopo il 2000."""
        return self.yr_renovated >= 2000 or self.yr_built >= 2000
