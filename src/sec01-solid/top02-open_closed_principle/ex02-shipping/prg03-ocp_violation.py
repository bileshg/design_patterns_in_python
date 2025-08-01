class Order:
    """Enables order creation"""
    def __init__(self, weight: float, distance: float):
        self.weight = weight
        self.distance = distance


class ShippingCostCalculator:

    def __init__(self, order: Order, shipping_method: str):
        self.order = order
        self.shipping_method = shipping_method

    # Violates OCP by defining the cost calculation hardcoded in the class.
    # Adding new shipping methods therefore requires changes to this class.
    def calculate_shipping_cost(self):
        if self.shipping_method == 'standard':
            return self.order.weight * 0.5 + self.order.distance * 0.1
        elif self.shipping_method == 'express':
            return self.order.weight * 0.8 + self.order.distance * 0.3
        else:
            raise ValueError("Invalid shipping method")
