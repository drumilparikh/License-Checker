def test():
    for i in range(5):
        print(i)
        if(i==3):
            print("Done")
            return i
            print("Still Here")

print(test())
