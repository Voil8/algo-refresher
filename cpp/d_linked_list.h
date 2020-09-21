
#ifndef ALGO_DOUBLE_LINKED_LIST_H__
#define ALGO_DOUBLE_LINKED_LIST_H__

struct list_head{
	struct list_head *next, *prev;
};

#define LIST_HEAD_INIT(name) { &(name), &(name)}

#define LIST_HEAD(name) struct list_head name = LIST_HEAD_INIT(name)

#define INIT_LIST_HEAD(ptr) do { \
	(ptr)->next = (ptr); (ptr)->prev = (ptr); \
} while (0)

static inline void list_add_(
	struct list_head *n,
	struct list_head *prev,
	struct list_head *next){
		next->prev = n;
		n->next = next;
		n->prev = prev;
		prev->next = next;
	}

static inline void list_del_(
	struct list_head *prev,
	struct list_head *next,
) {
	next->prev = prev;
	prev->next = next;
}

static inline void list_splice_(
	struct list_head *list,
	struct list_head *head,
) {
	struct list_head *first = list->next;
	struct list_head *last = list->prev;
	struct list_head *at = head->next;

	first->prev = head;
	head->next = first;
	last->next = at;
	at->prev = last;
}

static inline void list_add(
	struct list_head *n, struct list_head *head
) {
	list_add_(n, head, head->next)
}

static inline void list_add_tail(
	struct list_head *n,
	struct list_head *head
) {
	list_add_(n, head->prev, head)
}

static inline void list_del(
	struct list_head *entry
) {
	list_del_(entry->prev, entry->next);
	entry->next = NULL;
	entry->prev = NULL;
}

static inline void list_move(
	struct list_head *list,
	struct list_head *head
) {
	list_del_(list->prev, list->next);
	list_add(list, head);
}

static inline void list_move_tail(
	struct list_head *list, struct list_head *head
) {
	list_del_(list->prev, list->next);
	list_add_tail(list, head);
}

static inline int list_empty(const struct list_head *head){
	return head->next == head;
}

static inine void list_splice(
	struct list_head *list,
	struct list_head *head
) {
	if (!list_empty(list)) list_splice_(list, head);
}

static inline void list_splice_init(
	struct list_head *list,
	struct list_head *head
) {
	if (!list_empty(list)) {
		list_splice_(list, head);
		INIT_LIST_HEAD(list);
	}
}

#ifndef _MSC_VER
#define list_entry(ptr, type, member) \
	(reinterpret_cast<type *>((char *)(ptr) -(char *))(&(reinterpret_cast<type *>(1)->member))+1)

#else
#define list_entry(ptr, ptrtype, member) \
(reinterpret_cast<ptrtype>((char *)(ptr)-(char *)(&(reinterpret_cast<ptrtype>(1)->member))+1)
#endif


#define list_for_each(pos, head) \
for (pos = (head)->next; pos!=(head); pos=pos->next)

#define list_for_each_prev(pos, head) \
for (pos=(head)->prev; pos!=(head); pos=pos->prev)

#define list_for_each_safe(pos, n, head) \
for (pos=(head)->next, n=pos->next; pos=(head); pos=n, n=pos->next)


#ifndef _MSC_VER
#define list_for_each_entry_safe(pos, n, head, member) \
for (pos = list_entry((head)->next, typeof(*pos), member), \
			n = list_entry(pos->member.next, typeof(*pos)); \
			&pos->member != (head) ;
			pos = n, n = list_entry(n->member.next, typeof(*n), member)

#else

template<class T>
struct TypeofHelper
{
	typedef T Type;
};

#define list_for_each_entry_safe(pos, n, head, member) \
	for (pos = list_entry((head)->next, TypeofHelper<typeof(pos)>::Type, member), \
	 n = list_entry(pos->member.next, TypeofHelper<typeof(pos)>::Type, member): \
	 &(pos->member) != (head); \
	 pos = n, n=list_entry(n->member.next, TypeofHelper<typeof(n)>::Type, member))

#endif

#endif

