class Pupil():
    def __init__(self, ms, name):
        self.ms = ms
        self.name = name

    def diem_tb(self, *diem):
        diem_trung_binh = 0
        tong_diem = 0

        if len(diem) == 0:
            diem_trung_binh = 0
        else:
            for d in diem:
                tong_diem += d  

        diem_trung_binh = tong_diem / len(diem)
        return diem_trung_binh
    
    def tong_diem(self, *diem):
        return sum(d for d in diem)
    
class Student(Pupil):
    def __init__(self, ms, name, age, gender):
        super().__init__(ms,name) # Pupil.__init__(self,ms,name)
        self.age = age
        self.gender = gender

    # def diem_tb(self, *diem):
    #     return super().diem_tb(*diem)
    
    def tong_diem(self, *diem: float) -> float:
        return sum(diem)
    


pp1 = Pupil("001", "Huy Ta")
print(pp1.ms)
print(pp1.name)
print(pp1.diem_tb(8.25,9.5,10))
print(pp1.tong_diem(8.25,9.5,10))

sv2 = Student("002", "Sen Thoi", 14, "Nam")
print(sv2.ms)
print(sv2.name)
print(sv2.age)
print(sv2.gender)

print(sv2.diem_tb(7.5,8.5,9.5,10))
print(sv2.tong_diem(7.5,8.5,9.5,10))