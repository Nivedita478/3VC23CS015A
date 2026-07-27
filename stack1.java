public class StackArray {

    // Array to store stack elements
    int[] stack = new int[5];

    // Top points to the last inserted element
    int top = -1;

    // Push operation
    void push(int data) {
        if (top == stack.length - 1) {
            System.out.println("Stack Overflow");
        } else {
            stack[++top] = data;
            System.out.println(data + " pushed into stack");
        }
    }

    // Pop operation
    void pop() {
        if (top == -1) {
            System.out.println("Stack Underflow");
        } else {
            System.out.println("Deleted: " + stack[top--]);
        }
    }

    // Display stack elements
    void display() {
        if (top == -1) {
            System.out.println("Stack is Empty");
        } else {
            System.out.println("Stack elements are:");
            for (int i = top; i >= 0; i--) {
                System.out.println(stack[i]);
            }
        }
    }

    // Main method
    public static void main(String[] args) {

        StackArray s = new StackArray();

        s.push(10);
        s.push(20);
        s.push(30);

        s.display();

        s.pop();

        s.display();
    }
}