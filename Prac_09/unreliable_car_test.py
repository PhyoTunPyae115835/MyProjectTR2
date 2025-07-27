from Prac_09.unreliable_car import UnreliableCar

def main():
    # Create cars with different reliability
    reliable_car = UnreliableCar("Reliable", 100, 90)
    unreliable_car = UnreliableCar("Unreliable", 100, 10)

    # Try driving both several times
    print("Reliable Car Test:")
    for i in range(5):
        distance = reliable_car.drive(30)
        print(f"Attempt {i+1}: Drove {distance}km")

    print("\nUnreliable Car Test:")
    for i in range(5):
        distance = unreliable_car.drive(30)
        print(f"Attempt {i+1}: Drove {distance}km")

main()
