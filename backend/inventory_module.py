class MetaSingleton(type):
  _instances = {}

  def __call__(cls, *args, **kwargs):
      if cls not in cls._instances:
          cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
      return cls._instances[cls]

class InventoryManager(metaclass = MetaSingleton):
  def __init__(self):
    self.inventory = {}
    self.order = {}

  #카페에서 사용할 재고 및 최소 수량 추가
  def add_item(self, item, quantity, threshold):
    self.inventory[item] = quantity
    self.order[item] = threshold

  #재고 업데이트
  def update_inventory(self, item, quantity):
    if item in self.inventory:
      self.inventory[item] += quantity
      self.check_order(item)
    else:
      print(f"{item} not found in inventory.")

  #재고 체크 및 발주 여부 결정
  #재고가 임계점 이하시 자동 발주
  def check_order(self, item):
    if self.inventory[item] <= self.order[item]:
      self.order_item(item)

  #발주 처리
  def order_item(self, item):
    print(f"order {item}")

  def get_inventory(self):
    return self.inventory

if __name__ == "__main__":
  inventory_manager = InventoryManager()

  #재고 추가(항목, 수량, 발주 임계값)
  inventory_manager.add_item("coffee bean", 500, 250)
  inventory_manager.add_item("milk", 400, 150)
  inventory_manager.add_item("green tea powder", 200, 50)
  inventory_manager.add_item("water", 300, 100)
  inventory_manager.add_item("black tea", 150, 50)
  
  print("\ninventory:", inventory_manager.get_inventory())

  #재고 업데이트(항목, 사용 혹은 추가)
  inventory_manager.update_inventory("coffee bean", -350)
  inventory_manager.update_inventory("milk", +100)
  inventory_manager.update_inventory("green tea powder", -50)
  inventory_manager.update_inventory("water", +300)
  inventory_manager.update_inventory("black tea", -150)
  inventory_manager.update_inventory("soda", -150)
  
  #현재 재고 상태 출력(발주 전)
  print("\ninventory update:", inventory_manager.get_inventory())
