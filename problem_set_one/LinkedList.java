package problem_set_one;

import java.util.HashSet;
import java.util.Set;

public class LinkedList {
    private Node rootNode;

    LinkedList() {

    }

    public void add(Object data) {
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

    public int size(){
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

    public Node delete(Object data){
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

    public void removeDuplicates(){
        if(this.rootNode == null) return;

        Node currentNode = this.rootNode;
        final Set<Object> set = new HashSet<>();

        set.add(currentNode.getData());

        Node nextNode = this.rootNode.getNextNode();
        while(nextNode!=null){
            if(!set.contains(nextNode.getData())){
                set.add(nextNode.getData());
                currentNode = nextNode;
            }else{
                currentNode.setNextNode(nextNode.getNextNode());
            }
            nextNode = nextNode.getNextNode();
        }
    }

    @Override
    public String toString() {
        return this.rootNode!=null ? this.rootNode.toString() : "Empty List";
    }

    private class Node {
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
}

