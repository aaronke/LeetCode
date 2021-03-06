// HashMap, store next and random object reference in the map
// go 3 pass, deep copy node in chain, copy random, change chain to copy next

// HashMap 1, use named object and pre-copy next
public RandomListNode copyRandomList(RandomListNode head) {
    if (head == null)
        return null;
    HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
    RandomListNode cursor = head;
    while (cursor != null) {
        // copy node
        RandomListNode newNode = null;
        if (!map.containsKey(cursor)){
            newNode = new RandomListNode(cursor.label);
            map.put(cursor, newNode);
        }
        else
            newNode = map.get(cursor);
        // copy next
        RandomListNode newNext = null;
        if (cursor.next != null && !map.containsKey(cursor.next)) {
            newNext = new RandomListNode(cursor.next.label);
            map.put(cursor.next, newNext);
        }
        else if (cursor.next != null)
            newNext = map.get(cursor.next);
        newNode.next = newNext;            
        // copy random
        RandomListNode newRandom = null;
        if (cursor.random != null && !map.containsKey(cursor.random)) {
            newRandom = new RandomListNode(cursor.random.label);
            map.put(cursor.random, newRandom);
        }
        else if (cursor.random != null)
            newRandom = map.get(cursor.random);                
        newNode.random = newRandom;
        // move cursor
        cursor = cursor.next;
    }
    return map.get(head);
}

// HashMap 2, anonymous object, and previous copy next
public RandomListNode copyRandomList(RandomListNode head) {
    if (head == null)
        return null;
    HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
    RandomListNode dummy = new RandomListNode(0);
    RandomListNode previous = dummy;
    while (head != null) {
        // copy node
        if (!map.containsKey(head)){
            previous.next = new RandomListNode(head.label);
            map.put(head, previous.next);
        }
        else
            previous.next = map.get(head);
        // copy random
        if (head.random != null && !map.containsKey(head.random)) {
            previous.next.random = new RandomListNode(head.random.label);
            map.put(head.random, previous.next.random);
        }
        else if (head.random != null)
            previous.next.random = map.get(head.random);                
        // move head & previous
        previous = previous.next;
        head = head.next;
    }
    return dummy.next;
}

// 3 pass the list
public RandomListNode copyRandomList(RandomListNode head) {
    if (head == null)
        return null;
    copyNode(head);
    copyRandom(head);
    RandomListNode result = head.next;
    splitChain(head);
    return result;
}
// deep copy each node, connect them in a chain
private void copyNode(RandomListNode head) {
    while (head != null) {
        RandomListNode newNode = new RandomListNode(head.label);
        newNode.next = head.next;
        head.next = newNode;
        head = newNode.next;
    }
}
// copy node's random point
private void copyRandom(RandomListNode head) {
    while(head != null) {
        if (head.random != null)
            head.next.random = head.random.next;
        head = head.next.next;
    }
}
// split chain, make next pointer to the right place
private void splitChain(RandomListNode head) {
    while (head != null) {
        RandomListNode temp = head.next.next;
        if (temp != null)
            head.next.next = temp.next;
        head.next = temp;
        head = head.next;
    }
} 
