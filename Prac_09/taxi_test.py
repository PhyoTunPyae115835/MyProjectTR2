from Prac_09.taxi import Taxi

def main():
    # Create a new taxi
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km
    my_taxi.drive(40)

    # Print details and current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Start new fare and drive 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Print details and current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

main()
