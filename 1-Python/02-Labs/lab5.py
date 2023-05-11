out=0

while(out != 'y'):
        
        print("Functions:\n 1-lower() \n 2-join() \n 3-islower()")

        func = input("Please enter function number: ")
        
        if func == '1':
            data = "HELLO WORLD"
            print("Before use function :")
            print(data)
            output = data.lower()
            print("After use function :")
            print(output)
        elif func == '2':
            data = ("aaa", "bbb", "ggg")
            print("Before use function :")
            print(data)
            output = "#".join(data)
            print("After use function :")
            print(output)

        else:
            data = "hello world!"
            print("Before use function :")
            print(data)
            output = data.islower()
            print("After use function :")
            print(output)

        out = input("U want to Out Press Y: ")