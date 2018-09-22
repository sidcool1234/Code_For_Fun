package problem_set_one;

class LinkedList {
    private Node rootNode;

    LinkedList() {

    }

    public static void main(String[] args) {
        LinkedList l = new LinkedList();
        l.add(1);
        l.add(2);
        l.add(3);
        l.add(4);

        System.out.println(l.delete(2));
//        System.out.println(l.toString());
        System.out.println(l.size());

    }
    void add(Object data) {
        Node newNode = new Node(data);
        if (this.rootNode == null) {
            this.rootNode = new Node(data);
            return;
        }

        Node nextNode = this.rootNode.getNextNode();
        Node currentNode = this.rootNode;
        while(nextNode!=null){
            currentNode = nextNode;
            nextNode = nextNode.getNextNode();
        }
        currentNode.setNextNode(newNode);
    }

    int size(){
        if(this.rootNode == null){
            return 0;
        }
        int count = 1;
        Node nextNode = this.rootNode.getNextNode();
        while(nextNode!=null){
            count++;
            nextNode = nextNode.getNextNode();
        }
        return count;
    }

    Node delete(Object data){
        // todo Handle Null data
        if(this.rootNode == null) return null;
        Node deletedNode = null;
        if(this.rootNode.getData()!=null && this.rootNode.getData().equals(data)){
            deletedNode = this.rootNode;
            this.rootNode = this.rootNode.getNextNode();
            return deletedNode;
        }

        Node nextNode = this.rootNode.getNextNode();
        Node prevNode = this.rootNode;
        while(nextNode!=null){
            if(nextNode.getData()!=null && nextNode.getData().equals(data)){
                deletedNode = nextNode;
                prevNode.setNextNode(nextNode.getNextNode());
                break;
            }
            prevNode = nextNode;
            nextNode = nextNode.getNextNode();
        }
        return deletedNode;
    }

    @Override
    public String toString() {
        return this.rootNode!=null ? this.rootNode.toString() : "Empty List";
    }
}

class Node {
    private Node nextNode;
    private Object data;

    Node(Object data) {
        this.data = data;
    }

    Node getNextNode(){
        return this.nextNode;
    }

    void setNextNode(Node node){
        this.nextNode = node;
    }

    Object getData(){
        return this.data;
    }

    @Override
    public String toString() {
        return "Data: " + data + ", Next Node: " + nextNode;
    }
}