public class QueueArray {

    // Create an array of size 5 to store queue elements
    int[] queue = new int[5];

    // front points to the first element
    // rear points to the last inserted element
    int front = 0, rear = -1;

    // Method to insert an element into the queue
    void enqueue(int data) {

        // Check if the queue is full
        if (rear == queue.length - 1)
            System.out.println("Queue Full");
        else
            // Increment rear and insert the element
            queue[++rear] = data;
    }

    // Method to remove an element from the queue
    void dequeue() {

        // Check if the queue is empty
        if (front > rear)
            System.out.println("Queue Empty");
        else
            // Print and remove the front element
            System.out.println("Deleted: " + queue[front++]);
    }

    // Main method
    public static void main(String[] args) {

        // Create Queue object
        QueueArray q = new QueueArray();

        // Insert elements
        q.enqueue(10);
        q.enqueue(20);
        q.enqueue(30);

        // Remove one element
        q.dequeue();
    }
}