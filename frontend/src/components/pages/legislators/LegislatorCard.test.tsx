import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import LegislatorCard from './LegislatorCard'
import { LegislatorBills } from '../../../models/LegislatorModels'

describe('LegislatorCard', () => {
  const mockLegislatorBills: LegislatorBills = {
    legislator: {
      id: 1,
      name: 'John Doe'
    },
    supported_bills: 10,
    opposed_bills: 5
  }

  it('renders legislator information correctly', () => {
    render(<LegislatorCard legislatorBills={mockLegislatorBills} />)
    
    expect(screen.getByText('1 - John Doe')).toBeInTheDocument()
    expect(screen.getByText(/Supported Bills: 10/)).toBeInTheDocument()
    expect(screen.getByText(/Opposed Bills: 5/)).toBeInTheDocument()
  })

  it('renders with zero supported and opposed bills', () => {
    const legislatorWithZeros: LegislatorBills = {
      legislator: {
        id: 2,
        name: 'Jane Smith'
      },
      supported_bills: 0,
      opposed_bills: 0
    }

    render(<LegislatorCard legislatorBills={legislatorWithZeros} />)
    
    expect(screen.getByText('2 - Jane Smith')).toBeInTheDocument()
    expect(screen.getByText(/Supported Bills: 0/)).toBeInTheDocument()
    expect(screen.getByText(/Opposed Bills: 0/)).toBeInTheDocument()
  })

  it('renders with large numbers', () => {
    const legislatorWithLargeNumbers: LegislatorBills = {
      legislator: {
        id: 3,
        name: 'Test Legislator'
      },
      supported_bills: 1000,
      opposed_bills: 500
    }

    render(<LegislatorCard legislatorBills={legislatorWithLargeNumbers} />)
    
    expect(screen.getByText(/Supported Bills: 1000/)).toBeInTheDocument()
    expect(screen.getByText(/Opposed Bills: 500/)).toBeInTheDocument()
  })
})

