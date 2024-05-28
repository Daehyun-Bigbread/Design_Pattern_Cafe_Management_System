from abc import ABC, abstractmethod

class CafeHandler:
    def __init__(self):
        self.payments = {}

        self.cash_handler = CashHandler(self)
        self.credit_card_handler = CreditCardHandler(self)
        self.debit_card_handler = DebitCardHandler(self)
        self.gifticon_handler = GifticonHandler(self)

        self.cash_handler.set_next(self.credit_card_handler)
        self.credit_card_handler.set_next(self.debit_card_handler)
        self.debit_card_handler.set_next(self.gifticon_handler)

    def add_payment(self, method, amount):
        if method in self.payments:
            self.payments[method] += amount
        else:
            self.payments[method] = amount

    def handle_payment(self, req):
        self.cash_handler.handle(req)

class Handler(ABC):
    def __init__(self, cafe_handler=None):
        self.next_handler = None
        self.cafe_handler = cafe_handler

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, req):
        if self.next_handler:
            return self.next_handler.handle(req)
        print("All handlers failed")
        return None

class CashHandler(Handler):
    def handle(self, req):
        if req["method"] == "cash":
            self.cafe_handler.add_payment(req["method"], req["amount"])
        else:
            super(CashHandler, self).handle(req)

class CreditCardHandler(Handler):
    def handle(self, req):
        if req["method"] == "creditCard":
            self.cafe_handler.add_payment(req["method"], req["amount"])
        else:
            super(CreditCardHandler, self).handle(req)

class DebitCardHandler(Handler):
    def handle(self, req):
        if req["method"] == "debitCard":
            self.cafe_handler.add_payment(req["method"], req["amount"])
        else:
            super(DebitCardHandler, self).handle(req)

class GifticonHandler(Handler):
    def handle(self, req):
        if req["method"] == "gifticon":
            self.cafe_handler.add_payment(req["method"], req["amount"])
        else:
            super(GifticonHandler, self).handle(req)
