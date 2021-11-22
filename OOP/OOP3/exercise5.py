class Travel:
    """The travel record"""
    def __init__(self, mileage=0.0, times=list(), cities=list()):
        self.days=0
        self.mileage=mileage
        self.times = times
        self.cities = cities

        self.compute_days()
    
    def __str__(self):
        return f"Traveled {len(self.cities)} cities with {self.mileage} miles and {self.days} days."
    
    def __add__(self, other):
        times = self.times + other.times
        cities = self.cities + other.cities
        mileage = self.mileage + other.mileage
        ans = Travel(mileage, times, cities)
        return ans

    def compute_days(self):
        hours = sum(self.times)
        self.days = round(hours/24)

    def add_record(self, city, mile, time):
        self.cities.append(city)
        self.times.append(time)
        self.mileage+=mile
        self.compute_days()

record1 = Travel(mileage=200.0, times=[14, 20, 4], cities=["Boston", "Worcester", "Wellesley"])
print(record1)
record1.add_record("Springfield", 60, 46)
print(record1)

record2 = Travel()
record2.add_record("New Bedford", 100, 12)
record2.add_record("Cambridge", 45, 30)
print(record2)

record3 = record1+record2
print(record3)
record3.add_record("Salem", 78, 16)
print(record3)