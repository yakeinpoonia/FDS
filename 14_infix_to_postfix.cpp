#include<bits/stdc++.h>
using namespace std;

class Stack{
    private:
        int top;
        int capacity;
        char* array;

    public:
        Stack(int size){
            capacity = size;
            top = -1;
            array = new char[capacity];
        }

        bool isEmpty(){
            return top == -1;
        }

        bool isFull(){
            return top == capacity - 1;
        }

        void push(char ch){
            if(isFull()){
                cout << "Stack is overflow" << endl;
                return;
            }
            top++;
            array[top] = ch;
        }

        char pop(){
            if(isEmpty()){
                cout << "Stack is underflow" << endl;
                return '\0';  // Return null character for underflow
            }
            return array[top--];
        }

        char peek(){
            if(isEmpty()){
                cout << "Stack is underflow" << endl;
                return '\0';  // Return null character for underflow
            }
            return array[top];
        }
};

bool isBalanced(string& expr){
    Stack s(expr.length());
    for (char ch : expr){
        if(ch == '(' || ch == '{' || ch == '['){
            s.push(ch);
        }
        else if(ch == ')' || ch == '}' || ch == ']'){
            if(s.isEmpty() || (ch == ')' && s.peek() != '(') || (ch == '}' && s.peek() != '{') || (ch == ']' && s.peek() != '[')){
                return false;
            }
            s.pop();
        }
    }
    return s.isEmpty();
}

int precedence(char op){
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    if (op == '^') return 3;
    return 0;
}

string infixToPostfix(string& infix){
    Stack operators(infix.length());
    string postfix;

    for(char ch : infix){
        if(isalnum(ch)){  // If the character is an operand (number or variable)
            postfix += ch;
        }
        else if(ch == '('){  // If the character is '(', push it to the stack
            operators.push(ch);
        }
        else if(ch == ')'){  // If the character is ')', pop until '('
            while(!operators.isEmpty() && operators.peek() != '('){
                postfix += operators.pop();
            }
            operators.pop();  // pop the '('
        }
        else{  // If the character is an operator
            while(!operators.isEmpty() && precedence(operators.peek()) >= precedence(ch)){
                postfix += operators.pop();
            }
            operators.push(ch);  // Push the current operator to the stack
        }
    }

    // Pop all remaining operators
    while(!operators.isEmpty()){
        postfix += operators.pop();
    }

    return postfix;
}

int main() {
    string expression;
    cout << "Enter an infix expression: ";
    getline(cin, expression);

    // Check if the expression is well-parenthesized
    if (isBalanced(expression)) {
        cout << "The expression is well-parenthesized." << endl;

        // Convert to postfix
        string postfix = infixToPostfix(expression);
        cout << "Postfix expression: " << postfix << endl;
    } else {
        cout << "The expression is not well-parenthesized." << endl;
    }

    return 0;
}

