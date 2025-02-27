## 1. Discuss your solution’s time complexity. What tradeoffs did you make?
  - Time complexity is O(n) for counting votes, bills. O(N/B) for bulk inserts, where N is the number of rows, and B is the batch size.
  - Used Raw SQL instead of ORM, it's more efficient, but is less readable.
  - Bulk inserts over single inserts, reduces database round trips, insert more faster, but requires more memory.
## 2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?
  - Implement the Expand and Contract pattern, also known as Parallel Change, to gradually evolve the database and application without breaking the existing functionality.
## 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?
  - Modify the application to accept a list
  - Add new use cases to generate CSVs for legislators or bills
  - Add new endpoints to the API to generate CSVs for legislators or bills
## 4. How long did you spend working on the assignment?
  - 12 hours more or less.