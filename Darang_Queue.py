# Darang Queue py 
# Practical exam midterms, Data Structures and Algorithms, BSCS-SE CS101
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def running_average(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        total = sum(self.items)
        average = total / len(self.items)
        print(f"Running Average: {average:.2f}")
        return average

    def traverse_running_average(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        total = 0
        for i, val in enumerate(self.items, start=1):
            total += val
            average = total / i
            print(f"Running Average: {average:.2f}")

def menu():
    print("\nQueue Operations Menu: ")
    print("[+] Enqueue (format: + number)")
    print("[-] Dequeue (format: -)")
    print("[#] Stop (format: #)")
    print("------------------------------------------")


def main():
    queue = Queue()
    print("Enter operations (use + {number} to enqueue, - to dequeue, # to stop):")

    while True:
        menu()
        user_input = input("Enter your choice: ").strip()

        if user_input.startswith('+'):
            try:
                number_str = user_input[1:].strip()
                number = int(number_str)
                if not number_str:
                    raise ValueError
                number= int(number_str)
                queue.enqueue(number)
                print(f"Enqueued: {number}")
                queue.running_average()
            except ValueError:
                print("Invalid input. Please enter a valid number after '+'.")

        elif user_input == '-':
            dequeued = queue.dequeue()
            if dequeued is not None:
                print(f"Dequeued: {dequeued}")

        elif user_input == '#':
            print("Stopping the program.")
            print("\nFinal Running Averages:")
            queue.traverse_running_average()
            break

        else:
            print("Invalid input. Please enter a valid operation.")

if __name__ == "__main__":
    main()

    # 10 50 30