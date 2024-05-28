from abc import ABC, abstractmethod

# Strategy 패턴: 결제 수단별 결제 처리
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

# Factory 패턴: 결제 수단 객체 생성
class PaymentFactory:
    def create_payment(self, method):
        if method == "card":
            return CardPayment()
        elif method == "cash":
            return CashPayment()
        elif method == "gift":
            return GiftPayment()
        else:
            raise ValueError("Unknown payment method")

# Singleton 패턴: 재무제표 관리
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

# Observer 패턴: 결제 내역 관찰
class PaymentObserver(ABC):
    @abstractmethod
    def update(self, amount, method):
        pass

class FinancialStatementObserver(PaymentObserver):
    def __init__(self):
        self.financial_statement = FinancialStatementSingleton()

    def update(self, amount, method):
        self.financial_statement.update(amount)

class Payment:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, amount, method):
        for observer in self.observers:
            observer.update(amount, method)

    def make_payment(self, amount, payment_strategy):
        payment_strategy.pay(amount)
        self.notify_observers(amount, payment_strategy)

# 시스템 동작 예제
if __name__ == "__main__":
    # 결제 팩토리 생성
    payment_factory = PaymentFactory()
    
    # 재무제표 관찰자 생성
    financial_observer = FinancialStatementObserver()
    
    # 결제 시스템 생성
    payment_system = Payment()
    payment_system.add_observer(financial_observer)
    
    # 카드 결제 예제
    card_payment = payment_factory.create_payment("card")
    payment_system.make_payment(100, card_payment)
    
    # 현금 결제 예제
    cash_payment = payment_factory.create_payment("cash")
    payment_system.make_payment(50, cash_payment)
    
    # 기프트 카드 결제 예제
    gift_payment = payment_factory.create_payment("gift")
    payment_system.make_payment(30, gift_payment)
