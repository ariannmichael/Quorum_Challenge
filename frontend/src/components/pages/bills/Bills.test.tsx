import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import Bills from './Bills'
import * as api from '../../../services/api'

// Mock the API module
vi.mock('../../../services/api', () => ({
  getBillsDetails: vi.fn(),
  downloadBills: vi.fn()
}))

describe('Bills', () => {
  const mockBillsData = [
    {
      bill: {
        id: 1,
        title: 'Test Bill 1',
        primary_sponsor: 'John Doe'
      },
      supporters: 10,
      opposers: 5
    },
    {
      bill: {
        id: 2,
        title: 'Test Bill 2',
        primary_sponsor: 'Jane Smith'
      },
      supporters: 20,
      opposers: 15
    }
  ]

  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('renders bills header and download button', () => {
    vi.mocked(api.getBillsDetails).mockResolvedValue({ data: mockBillsData } as any)
    
    render(
      <BrowserRouter>
        <Bills />
      </BrowserRouter>
    )

    expect(screen.getByText('Bills')).toBeInTheDocument()
    expect(screen.getByText('Download CSV')).toBeInTheDocument()
  })

  it('displays bills when data is loaded', async () => {
    vi.mocked(api.getBillsDetails).mockResolvedValue({ data: mockBillsData } as any)
    
    render(
      <BrowserRouter>
        <Bills />
      </BrowserRouter>
    )

    await waitFor(() => {
      expect(screen.getByText('1 - Test Bill 1')).toBeInTheDocument()
      expect(screen.getByText('2 - Test Bill 2')).toBeInTheDocument()
    })
  })

  it('displays "No bills found" when there are no bills', async () => {
    vi.mocked(api.getBillsDetails).mockResolvedValue({ data: [] } as any)
    
    render(
      <BrowserRouter>
        <Bills />
      </BrowserRouter>
    )

    await waitFor(() => {
      expect(screen.getByText('No bills found')).toBeInTheDocument()
    })
  })

  it('calls getBillsDetails on mount', async () => {
    vi.mocked(api.getBillsDetails).mockResolvedValue({ data: mockBillsData } as any)
    
    render(
      <BrowserRouter>
        <Bills />
      </BrowserRouter>
    )

    await waitFor(() => {
      expect(api.getBillsDetails).toHaveBeenCalledTimes(1)
    })
  })
})

