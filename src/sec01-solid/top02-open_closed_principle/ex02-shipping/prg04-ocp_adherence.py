from abc import ABC, abstractmethod

class Order:
    """Enables order creation"""
    def __init__(self, weight: float, distance: float):
        self.weight = weight
        self.distance = distance


class ShippingStrategy(ABC):
    """Interface for shipping strategies"""
    @abstractmethod
    def calculate_cost(self, order) -> float:
        pass


class StandardShipping(ShippingStrategy):
    """Implementation of ShippingStrategy for standard shipping"""
    def calculate_cost(self, order: Order) -> float:
        """Calculates the cost for an order for standard shipment"""
        # Standard shipping cost calculation logic
        return order.weight * 0.5 + order.distance * 0.1


class ExpressShipping(ShippingStrategy):
    """Implementation of ShippingStrategy for express shipping"""
    def calculate_cost(self, order: Order):
        """Calculates the cost for an order for express shipment"""
        # Express shipping cost calculation logic
        return order.weight * 0.8 + order.distance * 0.3

class ShippingCostCalculator:
    """
    Calculator class which takes a certain shipping strategy to make the required calculations.
    """
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def calculate_shipping_cost(self, order: Order) -> float:
        """Calculates the actual shipping costs for an order"""
        return self.strategy.calculate_cost(order)


def driver():
    """Driver function to demonstrate the Open/Closed Principle"""
    # instantiate an order
    order = Order(weight=10, distance=100)

    # get calculators corresponding to different shipping methods
    standard_calculator = ShippingCostCalculator(StandardShipping())
    express_calculator = ShippingCostCalculator(ExpressShipping())

    # print shipping costs for the order per shipping method
    print("Standard Shipping Cost:", standard_calculator.calculate_shipping_cost(order))
    print("Express Shipping Cost:", express_calculator.calculate_shipping_cost(order))

if __name__ == "__main__":
    driver()
