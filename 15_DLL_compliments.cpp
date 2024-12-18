#include <iostream>
#include <string>
using namespace std;

// Node structure for the doubly linked list
struct Node {
    int data;
    Node* prev;
    Node* next;

    Node(int val) : data(val), prev(nullptr), next(nullptr) {}
};

// Class for managing the binary number using a doubly linked list
class BinaryNumber {
private:
    Node* head;
    Node* tail;

public:
    BinaryNumber() : head(nullptr), tail(nullptr) {}

    // Function to append a binary digit to the list
    void append(int digit) {
        if (digit != 0 && digit != 1) {
            cout << "Invalid binary digit. Only 0 or 1 allowed.\n";
            return;
        }
        Node* newNode = new Node(digit);
        if (!head) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }

    // Function to display the binary number
    void display() {
        Node* current = head;
        while (current) {
            cout << current->data;
            current = current->next;
        }
        cout << endl;
    }

    // Function to compute 1's complement
    void onesComplement() {
        Node* current = head;
        while (current) {
            current->data = 1 - current->data;
            current = current->next;
        }
    }

    // Function to compute 2's complement
    void twosComplement() {
        onesComplement(); // Compute 1's complement first

        // Add 1 to the binary number
        Node* current = tail;
        int carry = 1;
        while (current && carry) {
            int sum = current->data + carry;
            current->data = sum % 2;
            carry = sum / 2;
            current = current->prev;
        }

        // If carry is still 1, prepend a new node
        if (carry) {
            Node* newNode = new Node(1);
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
    }

    // Destructor to free memory
    ~BinaryNumber() {
        Node* current = head;
        while (current) {
            Node* temp = current;
            current = current->next;
            delete temp;
        }
    }
};

int main() {
    BinaryNumber binary;

    cout << "Enter binary number as a string: ";
    string input;
    cin >> input;

    for (char ch : input) {
        if (ch == '0' || ch == '1') {
            binary.append(ch - '0');
        } else {
            cout << "Invalid input. Only binary digits (0 or 1) are allowed.\n";
            return 1;
        }
    }

    cout << "Original Binary Number: ";
    binary.display();

    binary.onesComplement();
    cout << "1's Complement: ";
    binary.display();

    binary.twosComplement();
    cout << "2's Complement: ";
    binary.display();

    return 0;
}
