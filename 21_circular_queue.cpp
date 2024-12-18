#include <iostream>
using namespace std;

// Define the maximum size of the circular queue
#define SIZE 5

class CircularQueue {
private:
    int front;   // Points to the front element of the queue
    int rear;    // Points to the rear element of the queue
    int arr[SIZE]; // Array to store queue elements

public:
    // Constructor to initialize queue
    CircularQueue() {
        front = -1;
        rear = -1;
    }

    // Function to check if the queue is empty
    bool isEmpty() {
        return (front == -1);
    }

    // Function to check if the queue is full
    bool isFull() {
        return ((rear + 1) % SIZE == front);
    }

    // Function to add an element to the queue
    void enqueue(int value) {
        if (isFull()) {
            cout << "Queue is full. Cannot enqueue " << value << ".\n";
            return;
        }

        // If the queue is empty, update front
        if (isEmpty()) {
            front = 0;
        }

        // Update rear and add the element
        rear = (rear + 1) % SIZE;
        arr[rear] = value;
        cout << "Enqueued: " << value << "\n";
    }

    // Function to remove an element from the queue
    int dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty. Cannot dequeue.\n";
            return -1;
        }

        int value = arr[front]; // Store the value to return

        // If there is only one element, reset front and rear
        if (front == rear) {
            front = -1;
            rear = -1;
        } else {
            // Move front to the next position
            front = (front + 1) % SIZE;
        }

        cout << "Dequeued: " << value << "\n";
        return value;
    }

    // Function to display the elements of the queue
    void display() {
        if (isEmpty()) {
            cout << "Queue is empty.\n";
            return;
        }

        cout << "Queue elements: ";
        int i = front;
        while (true) {
            cout << arr[i] << " ";
            if (i == rear) {
                break;
            }
            i = (i + 1) % SIZE;
        }
        cout << "\n";
    }
};

int main() {
    CircularQueue cq;

    // Example operations
    cq.enqueue(10);
    cq.enqueue(20);
    cq.enqueue(30);
    cq.enqueue(40);
    cq.enqueue(50);

    // This enqueue will fail as the queue is full
    cq.enqueue(60);

    cq.display();

    cq.dequeue();
    cq.dequeue();

    cq.display();

    cq.enqueue(60);
    cq.enqueue(70);

    cq.display();

    return 0;
}
