class Solution:

  def shipWithinDays(self, weights: List[int], days: int) -> int:
    l, r = max(weights), sum(weights)
    res = r

    def canCarry(cap):
      ships, currCap = 1, cap
      for w in weights:
        if currCap - w < 0:
          ships += 1
          currCap = cap
        currCap -= w
      return ships <= days

    while l <= r:  # Fixed: changed to l <= r to check all potential values
      cap = (l + r) // 2
      if canCarry(cap):
        res = cap  # Found a valid capacity, record it...
        r = cap - 1  # ...and try to find a smaller one on the left
      else:
        l = cap + 1  # Capacity too small, need a larger one on the right
    return res