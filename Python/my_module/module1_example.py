# NOTE: __file__ : la ten file cua module hien tai
# NOTE: __name__ : la chuoi "__main__" cua module hien tai

print(f"__file__ is:'{__file__}', __name__ is '{__name__}'")

def func(a,b):
    print("a + b:= ", a + b)

if __name__ == "__main__":
    func(4,5)