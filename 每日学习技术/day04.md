# day04

## 链表

```javascript
// 节点
class Node {
  constructor(element) {
    this.element = element;
    this.next = null;
  }
}

/**
 * 功能描述
 * push 向链表尾部添加一个新元素
 * insert 向链表的特定位置插入一个新的元素
 * getElementAt 返回链表特定位置的元素
 * remove 从链表移除一个元素
 * indexOf 返回指定元素在链表中的索引。如果链表中没有该元素则返回 -1
 * removeAt 从链表的特定位置移除一个元素
 * isEmpty 如果链表中不包含任何元素，则返回true，否则返回false
 * size 返回链表包含的元素个数
 * toString 返回表示整个链表的字符串，让其只输出元素的值
 */

// 链表
class LinkedList {

  constructor(equalsFn) {
    this.count = 0;
    this.head = null;
    this.equalsFn = equalsFn;
  }

  push(element) {
    const node = new Node(element);
    let current;
    if (this.head === null) {
      this.head = node;
    } else {
      current = this.head;
      while (current.next !== null) {
        current = current.next;
      }
      current.next = node;
    }

    this.count ++;
  }

  insert(element, index) {
    if (index >= 0 && index <= this.count) {
      const node = new Node(element);
      if (index === 0) {
        const current = this.head;
        node.next = current;
        this.head = node;
      } else {
        const previous = this.getElementAt(index -1);
        const current = previous.next;
        node.next = current;
        previous.next = node;
      }
      this.count ++;
      return true;
    }
    return false;
  }

  getElementAt(index) {
    if (index >= 0 && index <= this.count) {
      let node = this.head;
      for (let i = 0; i < index && node != null; i ++) {
        node = node.next;
      }
      return node;
    }
    return undefined;
  }

  remove(index) {
    if (index >= 0 && index <= this.count) {

      let current;
      
      if (index === 0) {
        current = this.head;
        this.head = current.next;
      } else {
        const previous = this.getElementAt(index);
        current = previous.next;
        previous.next = current.next;
      }

      this.count --;
      return current.element;
    }
  }

  indexOf(element) {
    if (this.head === null) {
      return -1;
    } else {
      let current = this.head;
      for (let index = 0; index <= this.count; index ++) {
        if (current.element === element) {
          return index;
        } else {
          current = current.next;
        }
      }
    }

    return -1;
  }

  removeAt(index) {
    if (index >= 0 && index < this.count) {
      // 从头开始
      let current = this.head;
      if (index === 0) {
        this.head = current.next;
      } else {
        let previous;
        for (let i = 0; i < index; i ++) {
          previous = current;
          current = current.next;
        }

        previous.next = current.next;
      }

      this.count --;

      return current.element;
    }

    return undefined;
  }

  isEmpty() {
    return this.head === null;
  }

  size() {
    return this.count;
  }

  toString() {
    if (this.head === null) {
      return "";
    } else {
      let result = "";
      
      for (let index = 0; index <= this.count; index ++) {
        result += index + "" + this.getElementAt(index);
      }

      return result;
    }
  }
}
```             

