class Person:
    """Person attribute container"""

    def __init__(self):
        print("Creating an instance of Person")

        # address
        self.street_address: str | None = None
        self.postcode: str | None = None
        self.city: str | None = None

        # employment info
        self.company_name: str | None = None
        self.position: str | None = None
        self.annual_income: str | int | None = None

    def __str__(self) -> str:
        """Custom string representation for prettiness"""
        return (
            f"Address: {self.street_address}, {self.postcode}, {self.city}\n"
            + f"Employed at {self.company_name} as a {self.postcode} earning {self.annual_income}"
        )
