class Stack:
    def __init__(self):
        self.stack = []

    def push(self, application):
        self.stack.append(application)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, request):
        self.queue.append(request)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0


class HomeRentalPlatform:
    def __init__(self):
        self.application_stack = Stack()
        self.rental_request_queue = Queue()
        self.available_homes = []

    def apply_for_rental(self, application):
        self.application_stack.push(application)
        self.rental_request_queue.enqueue(application)
        print(f"Applied for rental: {application}")

    def undo_last_application(self):
        last_application = self.application_stack.pop()
        if last_application:
            # Optionally, remove from the rental request queue if needed
            self.rental_request_queue.dequeue()  # Assuming it's the same order
            print(f"Undid last application: {last_application}")
        else:
            print("No applications to undo.")

    def add_home(self, home):
        self.available_homes.append(home)
        print(f"Added home: {home}")

    def remove_home(self, home):
        if home in self.available_homes:
            self.available_homes.remove(home)
            print(f"Removed home: {home}")
        else:
            print("Home not found.")

    def list_available_homes(self):
        print("Available homes:")
        for home in self.available_homes:
            print(f"- {home}")
if __name__ == "__main__":
    platform = HomeRentalPlatform()

  
    platform.add_home("3-bedroom apartment in downtown")
    platform.add_home("2-bedroom house with garden")
    platform.add_home("1-bedroom studio near campus")

    
    platform.list_available_homes()

    
    platform.apply_for_rental("Application 1: 3-bedroom apartment")
    platform.apply_for_rental("Application 2: 2-bedroom house")

    
    platform.undo_last_application()

    
    platform.list_available_homes()

    
    platform.remove_home("2-bedroom house with garden")

    
    platform.list_available_homes()
