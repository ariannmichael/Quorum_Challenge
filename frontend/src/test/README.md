# Frontend Testing

This project uses [Vitest](https://vitest.dev/) for unit testing and [React Testing Library](https://testing-library.com/react) for component testing.

## Running Tests

```bash
# Run all tests
npm test

# Run tests in watch mode
npm test

# Run tests with UI
npm run test:ui

# Run tests with coverage
npm run test:coverage
```

## Test Structure

Tests are located alongside the components they test, using the `.test.tsx` or `.test.ts` extension:

```
src/
├── components/
│   └── pages/
│       ├── bills/
│       │   ├── Bills.tsx
│       │   ├── Bills.test.tsx
│       │   ├── BillCard.tsx
│       │   └── BillCard.test.tsx
│       └── legislators/
│           ├── Legislators.tsx
│           ├── Legislators.test.tsx
│           ├── LegislatorCard.tsx
│           └── LegislatorCard.test.tsx
├── services/
│   ├── api.ts
│   └── api.test.ts
└── utils/
    ├── downloadCSV.ts
    └── downloadCSV.test.ts
```

## Writing Tests

### Component Tests

```typescript
import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import MyComponent from './MyComponent'

describe('MyComponent', () => {
  it('renders correctly', () => {
    render(<MyComponent />)
    expect(screen.getByText('Hello')).toBeInTheDocument()
  })
})
```

### Testing with API Mocks

```typescript
import { vi } from 'vitest'
import * as api from '../services/api'

vi.mock('../services/api', () => ({
  getData: vi.fn()
}))

// In your test
vi.mocked(api.getData).mockResolvedValue({ data: [] })
```

### Testing Async Components

```typescript
import { waitFor } from '@testing-library/react'

it('loads data asynchronously', async () => {
  render(<MyComponent />)
  
  await waitFor(() => {
    expect(screen.getByText('Loaded')).toBeInTheDocument()
  })
})
```

## Test Coverage

Current test coverage includes:
- ✅ Component rendering
- ✅ API service calls
- ✅ User interactions
- ✅ Edge cases (empty data, errors)
- ✅ Utility functions

## Best Practices

1. **Test user behavior, not implementation details**
2. **Use descriptive test names**
3. **Mock external dependencies (API calls)**
4. **Test edge cases and error scenarios**
5. **Keep tests simple and focused**

