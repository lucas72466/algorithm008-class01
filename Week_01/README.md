# 算法训练营week1笔记

## 数组 array
* 一种连续的线性表结构
* 使用一段连续的内存空间来存储数据（通常是同种类型） --> 使得数组有一个强大的特性--随机访问（数组下标就是值距离数组开头元素的偏移量，利用偏移量和基地址进行寻址）
* 可以借助 CPU 的缓存机制，预读数组中的数据，访问效率更高
* 连续的存储空间也带来了限制 --> 低效的插入和删除
    * 插入： 需要将插入索引处以及之后的数据都向后挪动， 当插入在数组头部时需要拷贝整个数组， 插入数组尾部则不需要挪动， 平均的时间复杂度为O(n)
    * ----> 一种可能的改进思路：如果不关心元素的顺序， 可以将原来索引处的元素放到末尾， 再赋值新元素， 时间复杂度降至O(1)
    * ----> 另一种改进思路: 在开头处空出一部分空间，手动维护head，tail，方便prepend
    * 删除： 类似于插入， 复杂度也是O(n)
    * ----> 一种改进思路： 先记录下删除的数据， 进行索引的维护， 当数组空间不足时再一次性触发真正的删除操作 （lazy)
* 动态数组实现--resize （注意resize的条件， 避免复杂度的震荡）

### 代表性问题
运用双指针


## 链表 Linked List
* 通过指针“穿针引线”将零散的内存块串联在以前行程的数据结构， 不需要连续的内存空间
* 在实现上通常会加入dummy_head来实现节点操作的统一
* 失去了随机访问的特性，查找的复杂度高， 但删除和添加都可以以O(1)的复杂度来实现
* 天然具有递归的性质：每次递归缩小链表的规模
* 天然支持动态扩容
* 适合插入，删除频繁的场景， 但是会造成内存碎片
* 应用：LRU Cache

### 单链表 
![单链表](https://img.halfrost.com/Blog/ArticleTitleImage/136_0.png)
节点除了保存自身信息外还会保存指向下一个节点的指针， 尾结点指向NULL

### 双向链表
![双向链表](https://www.java2blog.com/wp-content/uploads/2017/09/DoublyLinkedList.png)
* 在单链表的基础上加入了prev节点，指向当前节点的前驱节点
* 虽然比单向链表多了额外的空间开销， 但是更具有灵活性 ==》 空间换时间

### 循环链表
![循环链表](https://lh3.googleusercontent.com/proxy/IgGHqfKwN-EgfmVBGBcy-WPLZMzi8flc6b0swKrJdelPkymhHNBcrvZxXwraTOsyUj1yskeqo8ssE0sS71OoYc0ayasDpiYC9jYR4liATQ)
* 适合处理具有环形结构特点的数据， 例如约瑟夫问题
* 让尾指针指向头结点
* 从循环链表中的任何一个结点出发都能找到任何其他结点

### 代表性问题
* [206反转链表](https://leetcode.com/problems/reverse-linked-list/) （利用栈，递归方法， 双指针迭代）
* [141环形链表](https://leetcode.com/problems/linked-list-cycle/) （快慢指针， 哈希法）
* [21合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) (递归，迭代)
* [24成对交换节点](https://leetcode.com/problems/swap-nodes-in-pairs/)
...

### 注意事项
链表为空时？链表只有一个节点时？ 头指针和尾指针时？--》 注意边界问题， 提高代码健壮性

## 跳表 skip list -- 给链表加速
![跳表](https://lotabout.me/2018/skip-list/skip-list-back-search.svg)引用自：https://lotabout.me/2018/skip-list/
* 升维思想+空间换时间
* 对标AVL （跳表原理简单，更容易实现） -- redis中的应用
* 产生若干层稀疏的链表来跳过部分元素，通过多级索引之间下沉来加速查找的过程
* 查找的时间复杂度与索引层数有关，O（logn）


## 栈 stack
* LIFO后进先出
* 是一种“操作受限”的线性表， 只允许在栈顶插入和删除， 可以基于链表（链式栈）或数组（顺序栈）进行封装
* 两个基本操作：入栈 push()和出栈 pop()
* 只需要维护栈顶，空间复杂度为O(1)， 插入删除也为O(1)（如果需要动态扩容则需要考虑拷贝的开销）
* 经典应用场景：函数调用栈，表达式求值，括号匹配，撤销回退功能

## 队列 Queue
* FIFO先进先出
* 也是操作受限的线性表数据结构， 基于不同的实现可以分为顺序队列和链式队列
* 两个基本操作：入队 enqueue()和出队 dequeue()， 需要维护两个指针：一个是 head 指针，指向队头；一个是 tail 指针，指向队尾。
* 避免数据搬移--循环队列（注意确定好队空和队满的判定条件， 队列为空条件是head==tail， 队列为满的条件是(tail+1)%n==head）
* 阻塞队列--“生产者-消费者问题”
* 并发队列--线程安全的队列

## 双端队列 Deque
* 两端都可以进行入队和出队操作的队列
* TODO： 分析C++和python的实现 [LeetCode题目](https://leetcode.com/problems/design-circular-deque/)

## 优先队列 Priority Queue
* 与普通队列的区别在于如何出队--根据优先级进行出队，不再是先入先出，而是允许优先级高的元素进行“插队” 
* 如何定义优先级？ 让调用者自行决定“大”和“小”的规则， 可以将比较函数当做参数传递--反转代码解释权的思想
* 可以基于栈，二分搜索树等结构进行实现
* TODO：分析源码

# 本周LeetCode刷题的一些感悟：
## 仔细审题，关注边界问题和特殊用例
看题时多对自己问问题，例如元素是否有序，是否要求原地操作， 数据有什么特征， 定义闭区间还是开区间， 数组为空的情况下怎么处理， 要的是元素本身还是索引值。。。
## 从简单入手，巧用数学归纳（发现重复性，找到子问题）
在LeetCode做爬楼梯的题目时一头雾水，找不到思路， 看完题解恍然大悟。 可以从最简单的情况下开始举几个例子， 找到规律来进行推广。 发现问题的重复性， 回归计算机的本质--做重复性的任务（if-else，loop，recursion),再复杂的任务也是要回归到这里
## 用辅助指针协助解题
快慢指针，双指针等巧妙地解题， 在链表题里用指针来临时存储节点信息，方便操作
## 缩减搜索空间
在Leetcode 11-盛最多水的容器的问题时， 双指针向中间进行夹逼， 每次移动指针都是在搜索空间上去削减， 相比于暴力法的无脑枚举，可以节省很多不必要的开销。--对暴力法进行剪枝操作
## 画图辅助理解
在写链表题的时候很绕，就可以画图来模拟指针的移动，让思路更加清晰
## 自顶向下的编码方式
开始时抓大放小， 关注代码整体的逻辑，再去完成辅助函数逻辑。
