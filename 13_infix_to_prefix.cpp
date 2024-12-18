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
                return '\0';
            }
            return array[top--];
        }

        char peek(){
            if(isEmpty()){
                cout << "Stack is underflow" << endl;
                return '\0';
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

string infixToPrefix(string& infix){
    // Reverse the expression
    string reversedInfix = infix;
    reverse(reversedInfix.begin(), reversedInfix.end());

    // Swap parentheses after reversing
    for(char& ch : reversedInfix){
        if(ch == '('){
            ch = ')';
        }
        else if(ch == ')'){
            ch = '(';
        }
    }

    Stack operators(reversedInfix.length());
    string prefix;

    // Process the reversed expression
    for(char ch : reversedInfix){
        if(isalnum(ch)){
            prefix += ch;
        }
        else if(ch == '('){
            operators.push(ch);
        }
        else if(ch == ')'){
            while(!operators.isEmpty() && operators.peek() != '('){
                prefix += operators.pop();
            }
            operators.pop();  // pop the '('
        }
        else{
            while(!operators.isEmpty() && precedence(operators.peek()) > precedence(ch)){
                prefix += operators.pop();
            }
            operators.push(ch);
        }
    }

    // Pop all remaining operators
    while(!operators.isEmpty()){
        prefix += operators.pop();
    }

    // Reverse the result to get the correct prefix notation
    reverse(prefix.begin(), prefix.end());
    return prefix;
}

int main() {
    string expression;
    cout << "Enter an infix expression: ";
    getline(cin, expression);  // Use getline to handle multi-word expressions

    // Check if the expression is well-parenthesized
    if (isBalanced(expression)) {
        cout << "The expression is well-parenthesized." << endl;

        // Convert to prefix
        string prefix = infixToPrefix(expression);
        cout << "Prefix expression: " << prefix << endl;
    } else {
        cout << "The expression is not well-parenthesized." << endl;
    }

    return 0;
}
