import random
target = random.randint(1,100)
count = 1
user_guess = int(input('猜猜数字是多少[1-100]:'))
while True:
    if user_guess == target:
        print(f'恭喜你,猜中了!共猜了{count}次')
        break
    elif user_guess > target:
        print('太大了,请重新输入')
        user_guess = int(input())
    else:
        print('太小了,请重新输入')
        user_guess = int(input())
    count += 1
