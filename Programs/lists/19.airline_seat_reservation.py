# Airline Seat Reservation

# Represent seats as a matrix.

# Support:-

# Book Seat
# Cancel Seat
# Show Available Seats
# Show Occupied Seats
# Find Adjacent Seats

def search(list,num):
    flag = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if(list[i][j] == num):
                flag = 1
                break
        if (flag==1):
            break            
    if(flag==1):
        return True
    else:
        return False

def index(list,num):
    flag = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if(list[i][j]==num):
                flag = 1
                break
        if(flag==1):
            break
    return i,j            

print("""Support:-

Book Seat ------------1
Cancel Seat-----------2
Show Available Seats--3
Show Occupied Seats---4
Find Adjacent Seats---5
To Exit---------------0      
      """)

booked = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
available = [[1,2,3],[11,12,13],[21,22,23],[31,32,33],[41,42,43],[51,52,53],[61,62,63],[71,72,73]]

op = -1
while (op!=0):
    op = input("Enter operation: ")
    if(op.isdigit()):
        op = int(op)
        if(op<6):
            if (op==1):
                print("Enter seat numbers to be booked separated by spaces: ")
                seats = list(map(int,input().split()))
                if (len(seats)>3):
                    print("Only 3 seats can be booked at maximum at a time")
                else:
                    for seat in seats:
                        if (search(available,seat)):
                            i,j = index(available,seat)
                            available[i][j] = 0
                            booked[i][j] = seat
                            print(f"Seat No.{seat} booked successfully!")
                        else:
                            if (search(booked,seat)):
                                print(f"Seat No.{seat} can't be booked as it is already booked!")
                            else:
                                print(f"Seat No.{seat} can't be booked!")
                                print("Please enter valid seat number")                                             
            elif (op==2):
                print("Enter seats to be cancelled: ")
                seats = list(map(int,input().split()))
                if (len(seats)>3):
                    print("Only 3 seats can be cancelled at a time")
                else:
                    for seat in seats:
                        if(search(booked,seat)):
                            i,j = index(booked,seat)
                            available[i][j] = seat
                            booked[i][j] = 0
                            print(f"Seat No.{seat} cancelled successfully!")
                        else:
                            if(search(available,seat)):
                                print(f"Seat No.{seat} can't be cancelled as it is not booked!")
                            else:
                                print(f"Seat No.{seat} can't be cancelled!")
                                print("Please enter valid seat number")                                   
            elif (op==3):
                
                print("Available Seats: ")
                for row in available:
                    print(*row)
            elif (op==4):
                print("Occupied Seats: ")
                for row in booked:
                    print(*row)
            # elif (op==5):
            #     seat = input("Enter seat number to find its adjacent available seats: ")
            #     if (seat.isdigit()==False):
            #         print("Please input valid seat number")
            #     else:
            #         seat = int(seat)
            #         if (1<=seat<=16):
                                                   


