/*! \brief Provides a handle for an inserted
 *         queue item.
 *
 * Use this handle to update or remove
 * the queue item.
 */
template <typename T>
typedef struct {
  int key;  /**< the priority */
  T value;  /**< the value */
  int heapIndex;  /**< the array index */
} priority_queue_item;