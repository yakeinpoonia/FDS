#include <bits/stdc++.h>
using namespace std;

class Stack {
private:
    int top;
    int capacity;
    string* array;

public:
    Stack(int size) {
        capacity = size;
        top = -1;
        array = new string[capacity];
    }

    bool isEmpty() {
        return top == -1;
    }

    void push(string str) {
        if (top == capacity - 1) {
            cout << "Stack overflow" << endl;
            return;
        }
        top++;
        array[top] = str;
    }

    string pop() {
        if (isEmpty()) {
            cout << "Stack underflow" << endl;
            return "";
        }
        return array[top--];
    }

    string peek() {
        if (isEmpty()) {
            cout << "Stack underflow" << endl;
            return "";
        }
        return array[top];
    }
};

// Postfix to Infix Conversion
string postfixToInfix(string& postfix) {
    Stack s(postfix.length());

    for (char ch : postfix) {
        if (isalnum(ch)) {  // If the character is an operand, push it onto the stack
            s.push(string(1, ch));
        } else {  // If the character is an operator
            string operand2 = s.pop();
            string operand1 = s.pop();
            string temp = "(" + operand1 + ch + operand2 + ")";
            s.push(temp);  // Push the resulting infix expression back to the stack
        }
    }
    return s.peek();  // The final result is in the stack
}

// Postfix to Prefix Conversion
string postfixToPrefix(string& postfix) {
    Stack s(postfix.length());

    // Traverse the postfix expression from left to right
    for (char ch : postfix) {
        if (isalnum(ch)) {  // If the character is an operand, push it onto the stack
            s.push(string(1, ch));
        } else {  // If the character is an operator
            string operand2 = s.pop();
            string operand1 = s.pop();
            string temp = ch + operand1 + operand2;  // Prefix: operator followed by operands
            s.push(temp);  // Push the resulting prefix expression back to the stack
        }
    }
    return s.peek();  // The final result is in the stack
}

int main() {
    string expression;
    int choice;
    
    cout << "Enter a postfix expression: ";
    getline(cin, expression);
    
    cout << "Choose conversion type: \n";
    cout << "1. Postfix to Infix\n";
    cout << "2. Postfix to Prefix\n";
    cout << "Enter your choice (1 or 2): ";
    cin >> choice;
    
    if (choice == 1) {
        string infix = postfixToInfix(expression);
        cout << "Infix expression: " << infix << endl;
    } else if (choice == 2) {
        string prefix = postfixToPrefix(expression);
        cout << "Prefix expression: " << prefix << endl;
    } else {
        cout << "Invalid choice! Please enter 1 or 2." << endl;
    }

    return 0;
}
