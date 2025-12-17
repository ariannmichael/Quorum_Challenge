# Q&A - Quorum Challenge

## 1. Discuss your solution's time complexity. What tradeoffs did you make?

### Time Complexity Analysis

- **Query Operations**: O(n) for counting votes and bills, where n is the number of records
  - Legislator analytics: Uses subqueries with COUNT aggregations - O(n) where n is the number of vote results
  - Bill analytics: Uses JOINs with GROUP BY and COUNT aggregations - O(n) where n is the number of vote results
- **Bulk Inserts**: O(N/B) where N is the number of rows and B is the batch size (1000 rows per batch)
  - Reduces database round trips significantly compared to single inserts

### Tradeoffs Made

1. **Raw SQL vs Django ORM**
   - **Choice**: Used raw SQL queries for complex analytics
   - **Benefit**: More efficient for complex aggregations and joins, better performance
   - **Tradeoff**: Less readable, harder to maintain, loses some Django ORM benefits (type safety, query optimization)

2. **Bulk Inserts vs Single Inserts**
   - **Choice**: Implemented batch processing with `bulk_create()` (1000 rows per batch)
   - **Benefit**: Reduces database round trips, significantly faster for large CSV imports
   - **Tradeoff**: Requires more memory to hold batches, less granular error handling

3. **Direct Database Queries vs Model Methods**
   - **Choice**: Queries executed directly in views
   - **Benefit**: Simpler structure, follows Django conventions, easier to understand
   - **Tradeoff**: Business logic is in views rather than separate service layer

4. **Monorepo Structure**
   - **Choice**: Organized as a monorepo with unified commands
   - **Benefit**: Easier to manage, consistent tooling, better for small teams
   - **Tradeoff**: Can become complex as project grows

## 2. How would you change your solution to account for future columns that might be requested, such as "Bill Voted On Date" or "Co-Sponsors"?

### Database Schema Evolution Strategy

1. **Django Migrations**
   - Use Django's migration system to add new columns incrementally
   - Create migrations: `python manage.py makemigrations`
   - Apply migrations: `python manage.py migrate`
   - Migrations are version-controlled and can be rolled back if needed

2. **Expand and Contract Pattern (Parallel Change)**
   - **Phase 1 (Expand)**: Add new columns as nullable or with default values
   - **Phase 2 (Migrate)**: Update application code to use new columns, keep old code working
   - **Phase 3 (Contract)**: Remove old columns after all data is migrated
   - This allows zero-downtime deployments

3. **Specific Implementation for New Columns**

   **For "Bill Voted On Date":**
   ```python
   # Add to Bill model
   vote_date = models.DateField(null=True, blank=True)
   
   # Update analytics query to include date
   # Update CSV export to include date column
   ```

   **For "Co-Sponsors":**
   ```python
   # Create new model for many-to-many relationship
   class BillCoSponsor(models.Model):
       bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
       legislator = models.ForeignKey(Legislator, on_delete=models.CASCADE)
       added_date = models.DateField(auto_now_add=True)
   
   # Update queries to include co-sponsors
   # Update CSV export format
   ```

4. **Backward Compatibility**
   - Keep existing API endpoints working
   - Add new optional query parameters for new fields
   - Use serializers to handle optional fields gracefully
   - Update CSV exports to include new columns with proper headers

5. **Testing Strategy**
   - Write migration tests to ensure data integrity
   - Test backward compatibility with existing CSV formats
   - Validate new column data types and constraints

## 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

### Implementation Approach

1. **New API Endpoints**
   ```python
   # In views.py
   class GenerateLegislatorCSVView(APIView):
       def post(self, request):
           legislator_ids = request.data.get('legislator_ids', [])
           # Generate CSV for specific legislators
           # Return CSV file
   
   class GenerateBillCSVView(APIView):
       def post(self, request):
           bill_ids = request.data.get('bill_ids', [])
           # Generate CSV for specific bills
           # Return CSV file
   ```

2. **Query Filtering**
   - Filter legislators/bills by the provided IDs
   - Use Django ORM `filter(id__in=legislator_ids)` for efficient queries
   - Maintain same analytics calculations but only for requested items

3. **CSV Generation Logic**
   - Reuse existing analytics queries with WHERE clauses
   - Generate CSV in-memory using Python's `csv` module
   - Return as HTTP response with appropriate headers
   - Support both individual and bulk generation

4. **API Design**
   ```json
   POST /api/legislators/generate-csv/
   {
     "legislator_ids": [1, 2, 3, 4, 5]
   }
   
   POST /api/bills/generate-csv/
   {
     "bill_ids": [10, 20, 30]
   }
   ```

5. **Error Handling**
   - Validate that all provided IDs exist
   - Handle invalid IDs gracefully
   - Return appropriate error messages
   - Support empty lists (return empty CSV with headers)

6. **Performance Considerations**
   - Use bulk queries to fetch all requested items at once
   - Consider pagination for very large lists
   - Cache frequently requested combinations if needed

## 4. How long did you spend working on the assignment?

- **Initial Implementation**: Approximately 12 hours
  - Setting up Django project structure
  - Implementing models, views, and serializers
  - Creating database migrations
  - Building API endpoints
  - Implementing CSV import/export functionality
  - Writing tests

- **Refactoring to Django Default Structure**: Additional 2-3 hours
  - Converting from DDD/Clean Architecture to Django's standard structure
  - Moving files to appropriate locations
  - Updating imports and references
  - Consolidating use cases into views

- **Monorepo Setup and Docker Configuration**: Additional 3-4 hours
  - Setting up Makefile with unified commands
  - Creating Dockerfiles for backend and frontend
  - Configuring docker-compose.yml
  - Writing comprehensive documentation
  - Setting up environment variable management

- **Testing and Bug Fixes**: Additional 2-3 hours
  - Fixing database connection issues
  - Resolving API endpoint routing problems
  - Improving error handling
  - Adding Docker test commands

**Total Estimated Time**: Approximately 19-22 hours

## 5. Additional Technical Decisions

### Architecture Choices

1. **Django Default Structure**
   - Chose Django's conventional structure over DDD/Clean Architecture
   - Reason: Better alignment with Django best practices, easier for Django developers to understand
   - Tradeoff: Less separation of concerns, but more maintainable for Django projects

2. **Monorepo Organization**
   - Unified project structure with shared tooling
   - Single Makefile for all commands
   - Consistent Docker setup across services
   - Easier dependency management

3. **Database Design**
   - Used integer IDs as primary keys (not auto-incrementing in some cases to match CSV data)
   - Foreign key relationships for data integrity
   - Raw SQL for complex analytics queries
   - Bulk operations for performance

4. **API Design**
   - RESTful endpoints following Django REST Framework conventions
   - Separate endpoints for analytics, import, and export
   - CSV format matching exact requirements
   - Proper HTTP status codes and error handling

5. **Frontend Integration**
   - React with TypeScript for type safety
   - Axios for HTTP requests
   - Bootstrap for responsive UI
   - Environment-based API URL configuration

### Performance Optimizations

1. **Bulk Operations**: Batch size of 1000 rows for efficient database writes
2. **Raw SQL**: Direct queries for complex aggregations avoid ORM overhead
3. **Database Indexing**: Foreign keys provide automatic indexes
4. **Connection Pooling**: Django's database connection pooling handles concurrent requests

### Future Improvements

1. **Caching**: Add Redis for caching frequently accessed analytics
2. **Pagination**: Implement pagination for large result sets
3. **Background Tasks**: Use Celery for async CSV processing
4. **API Versioning**: Add versioning for backward compatibility
5. **Rate Limiting**: Implement rate limiting for API endpoints
6. **Comprehensive Testing**: Add more integration and E2E tests
