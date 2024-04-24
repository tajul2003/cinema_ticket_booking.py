class Star_Cinema:
    hall_list = []
    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)
class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def book_seats(self, show_id, seats_to_book):
        if show_id not in [show[0] for show in self._show_list]:
            print("Error: Invalid show ID.")
            return
        for seat in seats_to_book:
            row, col = seat
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                print("Error: Invalid seat.")
                return
            if self._seats[show_id][row][col] == 'Booked':
                print("Error: Seat already booked.")
                return
        for seat in seats_to_book:
            row, col = seat
            self._seats[show_id][row][col] = 'Booked'
        print("Seats booked successfully.")
        
    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [['Free' for _ in range(self._cols)] for _ in range(self._rows)]    

    def view_show_list(self):
        print("Shows running in Hall", self._hall_no)
        for show in self._show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in [show[0] for show in self._show_list]:
            print("Error: Invalid show ID.")
            return
        print("Available seats for show", show_id, ":")
        for i in range(self._rows):
            for j in range(self._cols):
                if self._seats[show_id][i][j] == 'Free':
                    print(f"Row {i}, Col {j} - Free")
                else:
                    print(f"Row {i}, Col {j} - Booked")

def main():
    hall_A = Hall(5, 5, 1)
    hall_A.entry_show('111', 'Jawan Maji', '11:00 AM')
    hall_A.entry_show('333', 'Sujon Maji', '02:00 PM')

    while True:
        print("\n----Welcome to Star Cinema----\nOptions:")
        print("1. View all shows Today")
        print("2. View available Seats")
        print("3. Book Ticket")
        print("4. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            hall_A.view_show_list()
        elif choice == '2':
            show_id = input("Enter show ID: ")
            hall_A.view_available_seats(show_id)
        elif choice == '3':
            show_id = input("Enter show ID: ")
            num_seat = int(input("Enter the number of seats to book: "))
            seat_to_book = []
            for _ in range(num_seat):
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
                seat_to_book.append((row, col))
            hall_A.book_seats(show_id, seat_to_book)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
