#include <iostream>
using namespace std;

class Deque {
private:
    int *arr;
    int size;
    int front, rear;

public:
    // Constructor to initialize the deque with given size
    Deque(int n) {
        size = n;
        arr = new int[size];  // Dynamically allocate memory for the deque
        front = rear = -1;  // Initial state is empty
    }

    // Destructor to free the allocated memory
    ~Deque() {
        delete[] arr;
    }

    // Check if the deque is full
    bool isFull() {
        return (front == 0 && rear == size - 1) || (front == rear + 1);
    }

    // Check if the deque is empty
    bool isEmpty() {
        return front == -1;
    }

    // Insert an element at the front of the deque
    void insertFront(int item) {
        if (isFull()) {
            cout << "Deque is full! Cannot insert element at front." << endl;
        } else {
            if (front == -1) {  // If the deque is empty
                front = rear = 0;
            } else if (front == 0) {
                front = size - 1;  // Wrap around to the end
            } else {
                front--;  // Move front to the previous position
            }
            arr[front] = item;
            cout << "Inserted " << item << " at front." << endl;
        }
    }

    // Insert an element at the rear of the deque
    void insertRear(int item) {
        if (isFull()) {
            cout << "Deque is full! Cannot insert element at rear." << endl;
        } else {
            if (front == -1) {  // If the deque is empty
                front = rear = 0;
            } else if (rear == size - 1) {
                rear = 0;  // Wrap around to the front
            } else {
                rear++;  // Move rear to the next position
            }
            arr[rear] = item;
            cout << "Inserted " << item << " at rear." << endl;
        }
    }

    // Remove an element from the front of the deque
    int deleteFront() {
        if (isEmpty()) {
            cout << "Deque is empty! Cannot delete element from front." << endl;
            return -1;  // Indicate failure
        } else {
            int removedItem = arr[front];
            if (front == rear) {  // Only one element left
                front = rear = -1;  // Reset to empty state
            } else if (front == size - 1) {
                front = 0;  // Wrap around to the front
            } else {
                front++;  // Move front to the next position
            }
            cout << "Deleted " << removedItem << " from front." << endl;
            return removedItem;
        }
    }

    // Remove an element from the rear of the deque
    int deleteRear() {
        if (isEmpty()) {
            cout << "Deque is empty! Cannot delete element from rear." << endl;
            return -1;  // Indicate failure
        } else {
            int removedItem = arr[rear];
            if (front == rear) {  // Only one element left
                front = rear = -1;  // Reset to empty state
            } else if (rear == 0) {
                rear = size - 1;  // Wrap around to the back
            } else {
                rear--;  // Move rear to the previous position
            }
            cout << "Deleted " << removedItem << " from rear." << endl;
            return removedItem;
        }
    }

    // Display all elements in the deque
    void display() {
        if (isEmpty()) {
            cout << "Deque is empty!" << endl;
        } else {
            cout << "Deque elements are: ";
            int i = front;
            while (true) {
                cout << arr[i] << " ";
                if (i == rear) break;
                i = (i + 1) % size;  // Wrap around if we reach the end
            }
            cout << endl;
        }
    }
};

// Main function to test the Deque class
int main() {
    Deque dq(5);  // Create a deque of size 5

    dq.insertRear(10);  // Insert at rear
    dq.insertRear(20);
    dq.insertFront(5);  // Insert at front
    dq.insertFront(2);
    dq.insertRear(30);

    dq.display();  // Output: 2 5 10 20 30

    dq.deleteFront();  // Output: Deleted 2 from front
    dq.deleteRear();   // Output: Deleted 30 from rear

    dq.display();  // Output: 5 10 20

    return 0;
}