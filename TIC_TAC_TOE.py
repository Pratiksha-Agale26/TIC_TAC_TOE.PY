def sum(a,b,c):
    return a+b+c

def game(x_user,z_user):
    zero="x" if x_user[0] else("0" if z_user[0] else 0)
    one="x" if x_user[1] else("0" if z_user[1] else 1)
    two="x" if x_user[2] else("0" if z_user[2] else 2)
    three="x" if x_user[3] else("0" if z_user[3] else 3)
    four="x" if x_user[4] else("0" if z_user[4] else 4)
    five="x" if x_user[5] else("0" if z_user[5] else 5)
    six="x" if x_user[6] else("0" if z_user[6] else 6)
    seven="x" if x_user[7] else("0" if z_user[7] else 7)
    eight="x" if x_user[8] else("0" if z_user[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")
    print(f"--|---|---")

def winner(x_user,z_user):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(x_user[win[0]],x_user[win[1]],x_user[win[2]])==3):
            print("x won the match")
            return 1
        if (sum(z_user[win[0]],z_user[win[1]],z_user[win[2]])==3):
            print("0 won the match")
            return 0
    return -1

x_user=[0,0,0,0,0,0,0,0,0]
z_user=[0,0,0,0,0,0,0,0,0]
turn=1  #1 for x and 0 for 0
print("welcome to Tic Tac Toe")
while (True):
    game(x_user,z_user)
    if (turn==1):
        print("x's chance")
        value=int(input("please enter a value:"))
        x_user[value]=1
    else:
        print("0's chance")
        value=int(input("please enter a value"))
        z_user[value]=1
    cwin=winner(x_user,z_user)
    if (cwin != -1):
        print("match over")
        break
    turn=1-turn


