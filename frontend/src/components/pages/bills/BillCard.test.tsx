import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import BillCard from './BillCard'
import { BillDetail } from '../../../models/BillModels'

describe('BillCard', () => {
  const mockBillDetail: BillDetail = {
    bill: {
      id: 1,
      title: 'Test Bill',
      primary_sponsor: 'John Doe'
    },
    supporters: 10,
    opposers: 5
  }

  it('renders bill information correctly', () => {
    render(<BillCard billDetail={mockBillDetail} />)
    
    expect(screen.getByText('1 - Test Bill')).toBeInTheDocument()
    expect(screen.getByText(/Primary Sponsor: John Doe/)).toBeInTheDocument()
    expect(screen.getByText(/Supporters: 10/)).toBeInTheDocument()
    expect(screen.getByText(/Opposers: 5/)).toBeInTheDocument()
  })

  it('renders with zero supporters and opposers', () => {
    const billWithZeros: BillDetail = {
      bill: {
        id: 2,
        title: 'Another Bill',
        primary_sponsor: 'Jane Smith'
      },
      supporters: 0,
      opposers: 0
    }

    render(<BillCard billDetail={billWithZeros} />)
    
    expect(screen.getByText('2 - Another Bill')).toBeInTheDocument()
    expect(screen.getByText(/Supporters: 0/)).toBeInTheDocument()
    expect(screen.getByText(/Opposers: 0/)).toBeInTheDocument()
  })

  it('renders with long bill title', () => {
    const billWithLongTitle: BillDetail = {
      bill: {
        id: 3,
        title: 'A Very Long Bill Title That Might Wrap or Be Truncated',
        primary_sponsor: 'Test Sponsor'
      },
      supporters: 100,
      opposers: 50
    }

    render(<BillCard billDetail={billWithLongTitle} />)
    
    expect(screen.getByText(/A Very Long Bill Title That Might Wrap or Be Truncated/)).toBeInTheDocument()
  })
})

