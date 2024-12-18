#include <iostream>
#include <cmath>
using namespace std;

// Define a structure for polynomial terms
struct Node {
    int coeff;  // Coefficient of the term
    int exp;    // Exponent of the term
    Node* next; // Pointer to the next term
};

// Function to create a new node
Node* createNode(int coeff, int exp) {
    Node* newNode = new Node();
    newNode->coeff = coeff;
    newNode->exp = exp;
    newNode->next = nullptr;
    return newNode;
}

// Function to input a polynomial
Node* inputPolynomial() {
    Node* head = nullptr;
    Node* temp = nullptr;
    int coeff, exp, n;
    
    cout << "Enter the number of terms in the polynomial: ";
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        cout << "Enter coefficient and exponent: ";
        cin >> coeff >> exp;
        
        Node* newNode = createNode(coeff, exp);
        if (head == nullptr) {
            head = newNode;
            temp = head;
        } else {
            temp->next = newNode;
            temp = temp->next;
        }
    }
    
    return head;
}

// Function to output a polynomial
void outputPolynomial(Node* head) {
    if (head == nullptr) {
        cout << "Polynomial is empty." << endl;
        return;
    }
    
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->coeff << "x^" << temp->exp;
        if (temp->next != nullptr)
            cout << " + ";
        temp = temp->next;
    }
    cout << endl;
}

// Function to evaluate a polynomial at a given value of x
int evaluatePolynomial(Node* head, int x) {
    int result = 0;
    Node* temp = head;
    
    while (temp != nullptr) {
        result += temp->coeff * pow(x, temp->exp);
        temp = temp->next;
    }
    
    return result;
}

// Function to add two polynomials
Node* addPolynomials(Node* poly1, Node* poly2) {
    Node* result = nullptr;
    Node* temp = nullptr;
    
    while (poly1 != nullptr && poly2 != nullptr) {
        if (poly1->exp > poly2->exp) {
            Node* newNode = createNode(poly1->coeff, poly1->exp);
            if (result == nullptr) {
                result = newNode;
                temp = result;
            } else {
                temp->next = newNode;
                temp = temp->next;
            }
            poly1 = poly1->next;
        } else if (poly1->exp < poly2->exp) {
            Node* newNode = createNode(poly2->coeff, poly2->exp);
            if (result == nullptr) {
                result = newNode;
                temp = result;
            } else {
                temp->next = newNode;
                temp = temp->next;
            }
            poly2 = poly2->next;
        } else {
            int sum = poly1->coeff + poly2->coeff;
            if (sum != 0) {
                Node* newNode = createNode(sum, poly1->exp);
                if (result == nullptr) {
                    result = newNode;
                    temp = result;
                } else {
                    temp->next = newNode;
                    temp = temp->next;
                }
            }
            poly1 = poly1->next;
            poly2 = poly2->next;
        }
    }
    
    while (poly1 != nullptr) {
        Node* newNode = createNode(poly1->coeff, poly1->exp);
        if (result == nullptr) {
            result = newNode;
            temp = result;
        } else {
            temp->next = newNode;
            temp = temp->next;
        }
        poly1 = poly1->next;
    }
    
    while (poly2 != nullptr) {
        Node* newNode = createNode(poly2->coeff, poly2->exp);
        if (result == nullptr) {
            result = newNode;
            temp = result;
        } else {
            temp->next = newNode;
            temp = temp->next;
        }
        poly2 = poly2->next;
    }
    
    return result;
}

int main() {
    cout << "Polynomial 1:" << endl;
    Node* poly1 = inputPolynomial();
    
    cout << "Polynomial 2:" << endl;
    Node* poly2 = inputPolynomial();
    
    cout << "Polynomial 1: ";
    outputPolynomial(poly1);
    
    cout << "Polynomial 2: ";
    outputPolynomial(poly2);
    
    int x;
    cout << "Enter the value of x to evaluate Polynomial 1: ";
    cin >> x;
    cout << "Result of Polynomial 1 at x = " << x << " is: " << evaluatePolynomial(poly1, x) << endl;
    
    cout << "Enter the value of x to evaluate Polynomial 2: ";
    cin >> x;
    cout << "Result of Polynomial 2 at x = " << x << " is: " << evaluatePolynomial(poly2, x) << endl;
    
    Node* result = addPolynomials(poly1, poly2);
    cout << "Sum of Polynomials: ";
    outputPolynomial(result);
    
    return 0;
}
