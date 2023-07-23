class SumofSubArray:
    class Sub_array:
        def main(self):
            n = int(input("Enter size: "))
            arr = []
            print("Enter the array")
            for i in range(n):
                arr.append(int(input()))
            sum = 0
            for j in range(n):
                for k in range(j, n):
                    for l in range(j, k+1):
                        sum += arr[l]
            print("The sum is", sum)

SumofSubArray().Sub_array().main()
