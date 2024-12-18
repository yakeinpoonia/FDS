#include <iostream>
using namespace std;

// Node structure for the doubly linked list
struct Node {
    int data;
    Node* prev;
    Node* next;

    Node(int value) : data(value), prev(nullptr), next(nullptr) {}
};

class DoublyLinkedList {
public:
    Node* head;
    Node* tail;

    DoublyLinkedList() : head(nullptr), tail(nullptr) {}

    void append(int value) {
        Node* newNode = new Node(value);
        if (!head) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }

    void display() {
        Node* temp = head;
        while (temp) {
            cout << temp->data;
            temp = temp->next;
        }
        cout << endl;
    }

    void prepend(int value) {
        Node* newNode = new Node(value);
        if (!head) {
            head = tail = newNode;
        } else {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
    }
};

DoublyLinkedList addBinary(DoublyLinkedList& list1, DoublyLinkedList& list2) {
    DoublyLinkedList result;
    Node* ptr1 = list1.tail;
    Node* ptr2 = list2.tail;

    int carry = 0;
    while (ptr1 || ptr2 || carry) {
        int sum = carry;

        if (ptr1) {
            sum += ptr1->data;
            ptr1 = ptr1->prev;
        }

        if (ptr2) {
            sum += ptr2->data;
            ptr2 = ptr2->prev;
        }

        result.prepend(sum % 2); // Add the remainder to the result
        carry = sum / 2;        // Update the carry
    }

    return result;
}

int main() {
    DoublyLinkedList binary1, binary2;

    // Example binary numbers: 1011 (11 in decimal) and 1101 (13 in decimal)
    binary1.append(1);
    binary1.append(0);
    binary1.append(1);
    binary1.append(1);

    binary2.append(1);
    binary2.append(1);
    binary2.append(0);
    binary2.append(1);

    cout << "Binary 1: ";
    binary1.display();

    cout << "Binary 2: ";
    binary2.display();

    DoublyLinkedList result = addBinary(binary1, binary2);

    cout << "Sum: ";
    result.display();

    return 0;
}
