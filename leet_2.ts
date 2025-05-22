class Node {
  data: number;
  next: Node | null;

  constructor(data: number) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  head: Node | null;

  constructor() {
    this.head = null;
  }

  insertNewNode(data: number): void {
    const node = new Node(data);

    if (this.head === null) {
      this.head = node;
      return;
    }

    let current = this.head;
    while (current.next !== null) {
      current = current.next;
    }
    current.next = node;
  }

  toArray(): number[] {
    const result: number[] = [];
    let current = this.head;
    while (current !== null) {
      result.push(current.data);
      current = current.next;
    }
    return result;
  }
}

class Solution {
  addTwoNumbers(l1: Node | null, l2: Node | null): Node | null {
    let val1 = "";
    let val2 = "";

    let current1 = l1;
    let current2 = l2;

    while (current1 !== null) {
      val1 += current1.data.toString();
      current1 = current1.next;
    }

    while (current2 !== null) {
      val2 += current2.data.toString();
      current2 = current2.next;
    }

    const total =
      BigInt(val1.split("").reverse().join("")) +
      BigInt(val2.split("").reverse().join(""));
    const resultStr = total.toString().split("").reverse();

    const dummy = new Node(0);
    let current: Node = dummy;

    for (const digit of resultStr) {
      current.next = new Node(parseInt(digit));
      current = current.next;
    }

    return dummy.next;
  }
}


const l = new LinkedList();
l.insertNewNode(2);
l.insertNewNode(4);
l.insertNewNode(3);

const m = new LinkedList();
m.insertNewNode(5);
m.insertNewNode(6);
m.insertNewNode(4);

const s = new Solution();
let result = s.addTwoNumbers(l.head, m.head);

const resultArray: number[] = [];
while (result !== null) {
  resultArray.push(result.data);
  result = result.next;
}
console.log(resultArray);
