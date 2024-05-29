from abc import ABC, abstractmethod

# 결제 전략 패턴 정의
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Card")

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Cash")

class GiftPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Gift Card")

# 결제 전략 생성 팩토리
class PaymentFactory:
    def create_payment(self, method):
        method = method.lower()
        if method == "card" or method == "creditcard":
            return CardPayment()
        elif method == "cash":
            return CashPayment()
        elif method == "gift":
            return GiftPayment()
        elif method == "debitcard":
            return CardPayment()  # Assuming same handling as CardPayment
        else:
            raise ValueError(f"Unknown payment method: {method}")

# 싱글톤 패턴을 이용한 재무 상태 클래스
class FinancialStatementSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.total_amount = 0
        return cls._instance

    def update(self, amount):
        self.total_amount += amount
        print(f"Updated financial statement: total amount is now {self.total_amount}")

# 옵저버 패턴을 위한 추상 클래스
class PaymentObserver(ABC):
    @abstractmethod
    def update(self, amount):
        pass

# 재무 상태 옵저버 클래스
class FinancialStatementObserver(PaymentObserver):
    def __init__(self):
        self.financial_statement = FinancialStatementSingleton()

    def update(self, amount):
        self.financial_statement.update(amount)

# 결제 클래스
class Payment:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, amount):
        for observer in self.observers:
            observer.update(amount)

    def make_payment(self, amount, payment_strategy):
        payment_strategy.pay(amount)
        self.notify_observers(amount)
