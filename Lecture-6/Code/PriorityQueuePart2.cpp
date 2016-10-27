std::priority_queue<queue_entry,
  std::vector<queue_entry>, LessByFirst> pq;

// insert element with priority 5
pq.emplace(5, "A");

{
  // access first element
  const queue_entry& e = pq.top();

  // do not access e beyond this scope
  // without copying / moving
}
// remove the first element (e)
pq.pop();