def passThePillow(n: int, time: int):

    if n == time:
        return time - 1
    forward = True
    pointer = 1

    while time > 0:
        print(f"pointer:{pointer}")

        # Beginning of list.
        if pointer == 1 and forward == False:
            forward = True
            pointer += 1
            time -= 1

        # End of list.
        elif pointer == n and forward == True:
            forward = False
            pointer -= 1
            time -= 1

        # Going forward.
        elif forward:
            pointer += 1
            time -= 1

        # Going backward.
        elif not forward:
            pointer -= 1
            time -= 1

    return pointer




def main():
    # print(f"Result: {passThePillow(4,5)} Expected: 2")
    # print(f"Result: {passThePillow(3,2)} Expected: 3")
    # print(f"Result: {passThePillow(3,3)} Expected: 3")
    # print(f"Result: {passThePillow(18,38)} Expected: 5")
    print(f"Result: {passThePillow(2,341)} Expected: 2")

main() 

    # peopleList = []
    # for person in range(n):
    #     peopleList.append(person+1)
    # print(peopleList)

    # if time > n:
    #     amount = int(time / n)
    #     print(f"amount:{amount}")

    #     evenOdd = 0
    #     if amount == 1:
    #         evenOdd = 1
    #     elif amount > 1:
    #         evenOdd = 2 % amount
    #         if evenOdd == 2:
    #             evenOdd = 0
    #     print(f"evenOdd:{evenOdd}")

    #     print(f"time:{time}")
    #     print(f"n*amount:{n*amount}")

    #     if evenOdd == 1:
    #         remainder = time - ((n - 1) * amount)
    #         print(f"remainder:{remainder}")
    #         return peopleList[-(remainder+1)]
    #     elif evenOdd == 0:
    #         remainder = time - ((n) * amount)
    #         print(f"remainder:{remainder}")
    #         return peopleList[remainder]


    # elif time < n:
    #     return peopleList[time]
    
    # elif time == n:
    #     return peopleList[time-1]