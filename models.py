from sqlalchemy import Column, String, Integer, DateTime, Double, ForeignKey
from database import Base

class Factory(Base):
    __tablename__ = "Factory"
    id = Column(String(50), primary_key=True)
    name = Column(String(100))
    location = Column(String(100))
    create_time = Column(DateTime)

class Machine(Base):
    __tablename__ = "Machine"
    id = Column(String(50), primary_key=True)
    factory_id = Column(String(50), ForeignKey("Factory.id"))
    type = Column(String(50))
    description = Column(String(255))
    create_time = Column(DateTime)

class Order(Base):
    __tablename__ = "Order"
    id = Column(String(50), primary_key=True)
    machine_id = Column(String(50), ForeignKey("Machine.id"))
    create_time = Column(DateTime)
    order_no = Column(Double)
    timestamp = Column(DateTime)
    start_time = Column(DateTime)
    runtime_robot = Column(Integer)
    robot_cycletime_1 = Column(Integer)
    bag = Column(Integer)
    bag_pallet_l = Column(Integer)
    bag_pallet_r = Column(Integer)

class OrderDetail(Base):
    __tablename__ = "Order_detail"
    id = Column(String(50), primary_key=True)
    loose_bag_l = Column(Integer)
    loose_bag_r = Column(Integer)
    order_id = Column(String(50), ForeignKey("Order.id"))
    order_no = Column(Double)
    waittime_belt_l = Column(Integer)
    waittime_belt_r = Column(Integer)
    waittime_xlift_l = Column(Integer)
    waittime_xlift_r = Column(Integer)
    waittime_camera_l = Column(Integer)
    waittime_camera_r = Column(Integer)
    waittime_pallet_l = Column(Integer)
    waittime_pallet_r = Column(Integer)
    waittime_alarm_l = Column(Integer)
    waittime_alarm_r = Column(Integer)
    waittime_reset_connection_l = Column(Integer)
    waittime_reset_connection_r = Column(Integer)
    create_time = Column(DateTime)
    runtime_x_lift_l = Column(Integer)
    runtime_x_lift_r = Column(Integer)
    runtime_camera_l = Column(Integer)
    runtime_camera_r = Column(Integer)
