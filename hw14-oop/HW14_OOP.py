import numpy as np
from datetime import datetime

class MyCustomError(ValueError):
    pass


class User():
    def __init__(self, name):
        self.name = name


class Booking():
    def __init__(self, user, equipment, start_time, end_time):
        self.user = user.name
        self.equipment = equipment
        self.start_time = start_time
        self.end_time = end_time

    def is_intersect(self, booking_history):
        for booking in booking_history:
            if self.equipment == booking.equipment:
                if self.start_time < booking.end_time and booking.start_time < self.end_time:
                    raise MyCustomError(f"Equipment {self.equipment} is not available from {self.start_time} to {self.end_time}. It is booked by {booking.user}")
                    return True
        return False

    def is_busy(self, user_name, booking_history):
        for booking in booking_history:
            if self.user == user_name:
                if self.start_time < booking.end_time and booking.start_time < self.end_time:
                    raise MyCustomError(f"You are busy from {self.start_time} to {self.end_time}. You will work on {booking.equipment}")
                    return True
        return False


class LabEquipment():
    def __init__(self):
        self.equipment = ["amplificator", "tem", "laminar", "microscope"]
        self.booking_history = []

    def _parse_time(self, time_str):
        return datetime.strptime(time_str, '%Y-%m-%d %H:%M')

    def is_available(self, user, equipment_name, start_time, end_time):
        if equipment_name not in self.equipment:
            raise MyCustomError(f"Error: There is no such equipment as {equipment_name}. Available options are {self.equipment}")
            return False

        start_time_dt = self._parse_time(start_time)
        end_time_dt = self._parse_time(end_time)
        
        new_booking = Booking(user, equipment_name, start_time_dt, end_time_dt)
        
        if new_booking.is_intersect(self.booking_history) or new_booking.is_busy(user.name, self.booking_history):
            return False
        
        return True

    def book(self, user, equipment_name, start_time, end_time):
        start_time_dt = self._parse_time(start_time)
        end_time_dt = self._parse_time(end_time)
        
        if self.is_available(user, equipment_name, start_time, end_time):
            self.booking_history.append(Booking(user, equipment_name, start_time_dt, end_time_dt))
            print("Successful!")

class InvalidCommandError(ValueError):
    pass

class MemoryOverflowError(Exception):
    pass

class GenCodeInterpreter:
    def __init__(self):
        self.memory = [0] * 5000
        self.pointer = 0
        self.buffer = ""

    def eval(self, program):
        self.buffer = ""
        for command in program:
            if command == 'A':
                self.pointer += 1
                if self.pointer >= len(self.memory):
                    raise MemoryOverflowError("Pointer exceeded memory size")
            elif command == 'T':
                self.pointer -= 1
                if self.pointer < 0:
                    raise MemoryOverflowError("Pointer is negative")
            elif command == 'G':
                self.memory[self.pointer] += 1
            elif command == 'C':
                self.memory[self.pointer] -= 1
            elif command == 'N':
                char = chr(self.memory[self.pointer])
                self.buffer += char
            else:
                raise InvalidCommandError(f"Invalid command: {command}")
        
        return self.buffer


def meet_the_dunders():
    res = 0

    matrix = []
    for idx in range(0, 100, 10):
        matrix.__iadd__([list(range(idx, idx + 10))])

        
    def func_1(x):
        return x in range(1, 5, 2)
        
    def func_2(x):
        result = []
        iterator = selected_columns_indices.__iter__()
        while True:
            try:
                col = iterator.__next__()
                result.append(x[col])
            except StopIteration:
                break
        return result

    selected_columns_indices = list(filter(func_1, range(matrix.__len__())))
    
    selected_columns = map(func_2, matrix)

    arr = np.array(list(selected_columns))

    mask = arr.__getitem__((slice(None), 1)).__mod__(3).__eq__(0)
    new_arr = arr.__getitem__(mask)

    product = new_arr.__matmul__(new_arr.T)

    if ((product[0] < 1000)).all() and (product[2] > 1000).any():
        res = ((product.mean().__floordiv__(10)).__mod__(100)).__int__()
    return res